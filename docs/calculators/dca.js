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

  function effectiveMonthly(ratePct) {
    var r = ratePct / 100;
    if (r === 0) { return 0; }
    return Math.pow(1 + r, 1 / 12) - 1;
  }

  function dcaFinal(P, m, ratePct, years, growthPct) {
    var i = effectiveMonthly(ratePct);
    var g = effectiveMonthly(growthPct);
    var months = years * 12;
    var fv = P;
    var mCur = m;
    for (var t = 1; t <= months; t++) {
      fv = fv * (1 + i);
      fv += mCur; // contribution at end of month
      mCur = mCur * (1 + g);
    }
    return fv;
  }

  function update() {
    var P = parseAmount($("dca-initial"));
    var m = parseAmount($("dca-monthly"));
    var rate = parseFloat(String($("dca-rate").value).replace(",", ".")) || 0;
    var years = Math.max(0, Math.min(60, parseInt($("dca-years").value, 10) || 0));
    var growth = parseFloat(String($("dca-growth").value).replace(",", ".")) || 0;
    var cur = $("dca-currency").value;

    var fv = dcaFinal(P, m, rate, years, growth);

    function sumContributions(m0, gPct, yrs) {
      var g = effectiveMonthly(gPct);
      var total = 0, mCur = m0;
      for (var t = 1; t <= yrs * 12; t++) {
        total += mCur;
        mCur = mCur * (1 + g);
      }
      return total;
    }

    var totalInvested = P + sumContributions(m, growth, years);
    var i = effectiveMonthly(rate);
    var lump = totalInvested * Math.pow(1 + i, years * 12);

    $("dca-invested").textContent = fmt(totalInvested, cur);
    $("dca-final").textContent = fmt(fv, cur);
    $("dca-gains").textContent = fmt(Math.max(0, fv - totalInvested), cur) + " gains";
    $("dca-lump").textContent = fmt(lump, cur);
    $("dca-note").textContent = years === 0
      ? "Set an investment period to see results."
      : "Difference after " + years + " years: " + fmt(Math.abs(lump - fv), cur) + " (lump sum " + (lump >= fv ? "ahead" : "behind") + " in this flat-rate scenario).";
  }

  var ids = ["dca-initial", "dca-monthly", "dca-rate", "dca-years", "dca-growth", "dca-currency"];
  for (var i = 0; i < ids.length; i++) {
    if (ids[i] === "dca-initial" || ids[i] === "dca-monthly") { wireThousands($(ids[i])); }
    $(ids[i]).addEventListener("input", update);
    $(ids[i]).addEventListener("change", update);
  }
  update();
})();
