(function () {
  "use strict";

  var $ = function (id) { return document.getElementById(id); };

  function fmt(v, cur) {
    var r = Math.round(v);
    if (cur === "IDR") { return "Rp " + r.toLocaleString("id-ID"); }
    return "$" + Number(v).toLocaleString("en-US", { minimumFractionDigits: 2, maximumFractionDigits: 2 });
  }

  function apy(nominalPct, periods) {
    var r = nominalPct / 100;
    return (Math.pow(1 + r / periods, periods) - 1) * 100;
  }

  function pct(v) {
    return (Math.round(v * 100) / 100).toLocaleString("en-US", { minimumFractionDigits: 2, maximumFractionDigits: 2 }) + "%";
  }

  function update() {
    var nominal = parseFloat($("aa-nominal").value) || 0;
    var periods = parseInt($("aa-frequency").value, 10) || 12;
    var principal = parseFloat($("aa-principal").value) || 0;
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
    $(ids[i]).addEventListener("input", update);
    $(ids[i]).addEventListener("change", update);
  }
  update();
})();
