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

  function balanceAfterMonths(P, m, ratePct, months, periodsPerYear) {
    var r = ratePct / 100;
    if (r === 0) { return P + m * months; }
    var i = Math.pow(1 + r / periodsPerYear, periodsPerYear / 12) - 1;
    return P * Math.pow(1 + i, months) + m * (Math.pow(1 + i, months) - 1) / i;
  }

  var chart = null;

  function drawChart(P, m, ratePct, years, periodsPerYear, cur) {
    var labels = [], contribs = [], balances = [];
    for (var y = 0; y <= years; y++) {
      labels.push(y);
      contribs.push(Math.round(P + m * y * 12));
      balances.push(Math.round(balanceAfterMonths(P, m, ratePct, y * 12, periodsPerYear)));
    }
    var canvas = $("ci-chart");
    if (chart) { chart.destroy(); }
    chart = new Chart(canvas, {
      type: "line",
      data: {
        labels: labels,
        datasets: [
          { label: "Total contributions", data: contribs, borderColor: "#9aa0a6", backgroundColor: "rgba(154,160,166,0.15)", borderWidth: 2, pointRadius: 0, tension: 0.2 },
          { label: "Balance", data: balances, borderColor: "#1a73e8", backgroundColor: "rgba(26,115,232,0.10)", borderWidth: 2, pointRadius: 0, tension: 0.2, fill: true }
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
    var P = parseFloat($("ci-initial").value) || 0;
    var m = parseFloat($("ci-monthly").value) || 0;
    var rate = parseFloat($("ci-rate").value) || 0;
    var years = Math.max(0, Math.min(60, parseInt($("ci-years").value, 10) || 0));
    var periods = parseInt($("ci-frequency").value, 10) || 12;
    var cur = $("ci-currency").value;
    var months = years * 12;
    var fv = balanceAfterMonths(P, m, rate, months, periods);
    var contributed = P + m * months;
    $("ci-contributed").textContent = fmt(contributed, cur);
    $("ci-gains").textContent = fmt(Math.max(0, fv - contributed), cur);
    $("ci-final").textContent = fmt(fv, cur);
    drawChart(P, m, rate, years, periods, cur);
  }

  var ids = ["ci-initial", "ci-monthly", "ci-rate", "ci-years", "ci-frequency", "ci-currency"];
  for (var i = 0; i < ids.length; i++) {
    $(ids[i]).addEventListener("input", update);
    $(ids[i]).addEventListener("change", update);
  }
  update();
})();
