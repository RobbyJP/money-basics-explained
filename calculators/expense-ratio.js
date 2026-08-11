(function () {
  "use strict";

  var $ = function (id) { return document.getElementById(id); };

  function fmt(v, cur) {
    var r = Math.round(v);
    if (cur === "IDR") { return "Rp " + r.toLocaleString("id-ID"); }
    return "$" + Number(v).toLocaleString("en-US", { minimumFractionDigits: 2, maximumFractionDigits: 2 });
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
    var P = parseFloat($("er-initial").value) || 0;
    var m = parseFloat($("er-monthly").value) || 0;
    var rate = parseFloat($("er-rate").value) || 0;
    var feeA = parseFloat($("er-feea").value) || 0;
    var feeB = parseFloat($("er-feeb").value) || 0;
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
    $(ids[i]).addEventListener("input", update);
    $(ids[i]).addEventListener("change", update);
  }
  update();
})();
