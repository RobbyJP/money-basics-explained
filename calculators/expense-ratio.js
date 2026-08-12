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

  function netFinal(P, m, ratePct, feePct, years) {
    var gross = 1 + ratePct / 100;
    var netAnnual = gross * (1 - feePct / 100) - 1; // fee drag on the whole balance
    var i = Math.pow(1 + netAnnual, 1 / 12) - 1;
    var fv = P;
    for (var t = 1; t <= years * 12; t++) {
      fv = fv * (1 + i) + m;
    }
    return fv;
  }

  function update() {
    var P = parseAmount($("er-initial"));
    var m = parseAmount($("er-monthly"));
    var rate = parseFloat(String($("er-rate").value).replace(",", ".")) || 0;
    var feeA = parseFloat(String($("er-feea").value).replace(",", ".")) || 0;
    var feeB = parseFloat(String($("er-feeb").value).replace(",", ".")) || 0;
    var years = Math.max(0, Math.min(60, parseInt($("er-years").value, 10) || 0));
    var cur = $("er-currency").value;

    var finA = netFinal(P, m, rate, feeA, years);
    var finB = netFinal(P, m, rate, feeB, years);
    $("er-fina").textContent = fmt(finA, cur);
    $("er-finb").textContent = fmt(finB, cur);
    $("er-diff").textContent = fmt(Math.max(0, finA - finB), cur);
  }

  var ids = ["er-initial", "er-monthly", "er-rate", "er-feea", "er-feeb", "er-years", "er-currency"];
  for (var i = 0; i < ids.length; i++) {
    if (ids[i] === "er-initial" || ids[i] === "er-monthly") { wireThousands($(ids[i])); }
    $(ids[i]).addEventListener("input", update);
    $(ids[i]).addEventListener("change", update);
  }
  update();
})();
