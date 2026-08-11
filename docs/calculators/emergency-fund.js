(function () {
  "use strict";

  var $ = function (id) { return document.getElementById(id); };

  function fmt(v, cur) {
    var r = Math.round(v);
    if (cur === "IDR") { return "Rp " + r.toLocaleString("id-ID"); }
    return "$" + Number(v).toLocaleString("en-US", { minimumFractionDigits: 2, maximumFractionDigits: 2 });
  }

  function parseAmount(el) {
    var v = String(el.value).replace(/\./g, "").replace(",", ".");
    var n = parseFloat(v);
    return isNaN(n) ? 0 : n;
  }

  function wireThousands(el) {
    el.addEventListener("input", function () {
      var pos = el.selectionStart || el.value.length;
      var raw = el.value;
      var commaIdx = raw.indexOf(",");
      var intPart = commaIdx === -1 ? raw : raw.slice(0, commaIdx);
      var decPart = commaIdx === -1 ? "" : raw.slice(commaIdx + 1).replace(/[^\d]/g, "").slice(0, 2);
      var digits = intPart.replace(/[^\d]/g, "");
      var grouped = digits.replace(/\B(?=(\d{3})+(?!\d))/g, ".");
      var beforeDigits = intPart.slice(0, pos).replace(/[^\d]/g, "").length;
      var sepsBefore = (grouped.slice(0, beforeDigits).match(/\./g) || []).length;
      var formatted = decPart ? grouped + "," + decPart : grouped;
      if (formatted !== raw) {
        el.value = formatted;
        var newPos = Math.min(formatted.length, pos + sepsBefore);
        el.setSelectionRange(newPos, newPos);
      }
    });
  }

  function update() {
    var expenses = parseAmount($("ef-expenses"));
    var stability = $("ef-stability").value;
    var dependents = parseInt($("ef-dependents").value, 10) || 0;
    var insurance = $("ef-insurance").value;
    var cur = $("ef-currency").value;

    var base = stability === "stable" ? 3 : (stability === "volatile" ? 9 : 6);
    var add = dependents + (insurance === "good" ? 0 : (insurance === "partial" ? 1 : 2));
    var min = base;
    var max = Math.min(12, base + add);
    var monthsText = min === max ? min + " months" : min + "\u2013" + max + " months";
    var moneyText = fmt(expenses * min, cur) + (max > min ? " \u2013 " + fmt(expenses * max, cur) : "");

    $("ef-months").textContent = monthsText;
    $("ef-money").textContent = moneyText;

    var reasons = [];
    if (stability === "volatile") { reasons.push("income can fluctuate, so a larger buffer is conventional"); }
    if (stability === "stable") { reasons.push("stable income usually supports a smaller buffer"); }
    if (dependents > 0) { reasons.push(dependents + " dependent(s) add buffer"); }
    if (insurance === "none") { reasons.push("no insurance means more of the risk sits with you"); }
    if (insurance === "good") { reasons.push("strong insurance reduces the buffer needed"); }
    $("ef-reason").textContent = "Why: " + (reasons.length ? reasons.join("; ") : "baseline guidance") + ". An emergency fund covers income shocks (job loss, illness, unexpected repairs) â€” not planned purchases; those belong in a sinking fund.";
  }

  var ids = ["ef-expenses", "ef-stability", "ef-dependents", "ef-insurance", "ef-currency"];
  for (var i = 0; i < ids.length; i++) {
    if (ids[i] === "ef-expenses") { wireThousands($(ids[i])); }
    $(ids[i]).addEventListener("input", update);
    $(ids[i]).addEventListener("change", update);
  }
  update();
})();
