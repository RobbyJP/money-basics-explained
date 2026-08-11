(function () {
  "use strict";

  var $ = function (id) { return document.getElementById(id); };

  function fmt(v, cur) {
    var r = Math.round(v);
    if (cur === "IDR") { return "Rp " + r.toLocaleString("id-ID"); }
    return "$" + Number(v).toLocaleString("en-US", { minimumFractionDigits: 2, maximumFractionDigits: 2 });
  }

  function update() {
    var expenses = parseFloat($("ef-expenses").value) || 0;
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
    $("ef-reason").textContent = "Why: " + (reasons.length ? reasons.join("; ") : "baseline guidance") + ". An emergency fund covers income shocks (job loss, illness, unexpected repairs) — not planned purchases; those belong in a sinking fund.";
  }

  var ids = ["ef-expenses", "ef-stability", "ef-dependents", "ef-insurance", "ef-currency"];
  for (var i = 0; i < ids.length; i++) {
    $(ids[i]).addEventListener("input", update);
    $(ids[i]).addEventListener("change", update);
  }
  update();
})();
