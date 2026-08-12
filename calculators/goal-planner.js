(function () {
  "use strict";

  var $ = function (id) { return document.getElementById(id); };

  function fmt(v, cur) {
    var r = Math.round(v);
    if (cur === "IDR") {
      return "Rp " + r.toLocaleString("id-ID");
    }
    return "$" + Number(v).toLocaleString("en-US", { minimumFractionDigits: 2, maximumFractionDigits: 2 });
  }

  function fmtShort(v, cur) {
    return fmt(v, cur).replace(/\.00$/, "");
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

  function moneyNeeded(target, monthly, ratePct, months) {
    var r = ratePct / 100;
    var fv = monthly * months;
    var mNeeded = monthly;
    var shortfall = 0;
    if (r > 0) {
      var i = Math.pow(1 + r / 12, 12 / 12) - 1;
      var g = Math.pow(1 + i, months);
      fv = monthly * (g - 1) / i;
      mNeeded = target * i / (g - 1);
    } else if (target > 0) {
      mNeeded = target / months;
    }
    shortfall = Math.max(0, target - fv);
    return { fv: fv, mNeeded: mNeeded, shortfall: shortfall };
  }

  var chart = null;

  function drawChart(target, monthly, ratePct, years, cur) {
    var labels = [], balances = [];
    for (var y = 0; y <= years; y++) {
      var b = moneyNeeded(target, monthly, ratePct, y === 0 ? 1 : y * 12);
      labels.push(y);
      balances.push(Math.round(y === 0 ? 0 : b.fv));
    }
    var canvas = $("gp-chart");
    if (chart) { chart.destroy(); }
    chart = new Chart(canvas, {
      type: "line",
      data: {
        labels: labels,
        datasets: [
          { label: "Target", data: labels.map(function () { return target; }), borderColor: "#c5221f", borderDash: [6, 4], borderWidth: 2, pointRadius: 0, fill: false },
          { label: "Projected balance", data: balances, borderColor: "#1a73e8", backgroundColor: "rgba(26,115,232,0.10)", borderWidth: 2, pointRadius: 0, tension: 0.2, fill: true }
        ]
      },
      options: {
        responsive: true,
        plugins: {
          legend: { position: "bottom" },
          tooltip: { callbacks: { label: function (ctx) { return ctx.dataset.label + ": " + fmt(ctx.parsed.y, cur); } } }
        },
        scales: {
          x: { title: { display: true, text: "Year" } },
          y: { title: { display: true, text: "Value" } }
        }
      }
    });
  }

  function update() {
    var target = parseAmount($("gp-target"));
    var monthly = parseAmount($("gp-monthly"));
    var rate = parseFloat($("gp-rate").value) || 0;
    var years = Math.max(0, Math.min(60, parseInt($("gp-years").value, 10) || 0));
    var cur = $("gp-currency").value;
    var months = Math.max(1, years * 12);
    var res = moneyNeeded(target, monthly, rate, months);

    $("gp-projected").textContent = fmt(res.fv, cur);
    $("gp-need").textContent = fmtShort(res.mNeeded, cur);

    var verdict = $("gp-verdict");
    if (target > 0) {
      if (res.shortfall <= 0) {
        var surplus = res.fv - target;
        var pct = Math.round((res.fv / target - 1) * 100);
        verdict.className = "calc-value calc-ok";
        verdict.textContent = "On track (+" + pct + "%)";
        verdict.title = "Projected balance is " + fmt(surplus, cur) + " above your target";
      } else {
        verdict.className = "calc-value calc-warn";
        verdict.textContent = "Short by " + fmtShort(res.shortfall, cur);
        verdict.title = "Save about " + fmtShort(res.mNeeded, cur) + "/month instead";
      }
    } else {
      verdict.className = "calc-value";
      verdict.textContent = "-";
    }
    drawChart(target, monthly, rate, years, cur);
  }

  var ids = ["gp-target", "gp-monthly", "gp-rate", "gp-years", "gp-currency"];
  for (var i = 0; i < ids.length; i++) {
    if (ids[i] === "gp-target" || ids[i] === "gp-monthly") { wireThousands($(ids[i])); }
    $(ids[i]).addEventListener("input", update);
    $(ids[i]).addEventListener("change", update);
  }
  update();
})();