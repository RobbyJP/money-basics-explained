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

  function apy(nominalPct, periods) {
    var r = nominalPct / 100;
    return (Math.pow(1 + r / periods, periods) - 1) * 100;
  }

  function pct(v) {
    return (Math.round(v * 100) / 100).toLocaleString("en-US", { minimumFractionDigits: 2, maximumFractionDigits: 2 }) + "%";
  }

  function update() {
    var nominal = parseFloat(String($("aa-nominal").value).replace(",", ".")) || 0;
    var periods = parseInt($("aa-frequency").value, 10) || 12;
    var principal = parseAmount($("aa-principal"));
    var cur = $("aa-currency").value;

    var eff = apy(nominal, periods);
    var gain = principal * Math.pow(1 + nominal / 100 / periods, periods) - principal;
    var simple = principal * nominal / 100;
    $("aa-apy").textContent = pct(eff);
    $("aa-gain").textContent = "earns " + fmt(gain, cur) + " in a year (" + fmt(gain - simple, cur) + " more than no compounding)";

    $("aa-f1").textContent = pct(apy(nominal, 1));
    $("aa-f4").textContent = pct(apy(nominal, 4));
    $("aa-f12").textContent = pct(apy(nominal, 12));
    $("aa-f365").textContent = pct(apy(nominal, 365));
  }

  var ids = ["aa-nominal", "aa-frequency", "aa-principal", "aa-currency"];
  for (var i = 0; i < ids.length; i++) {
    if (ids[i] === "aa-principal") { wireThousands($(ids[i])); }
    $(ids[i]).addEventListener("input", update);
    $(ids[i]).addEventListener("change", update);
  }
  update();
})();
