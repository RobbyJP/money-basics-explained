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

  function fmtMonths(m, cur) {
    var years = Math.floor(m / 12);
    var rem = m % 12;
    if (years === 0) return rem + " mo";
    if (rem === 0) return years + " yr";
    return years + " yr " + rem + " mo";
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

  function monthlyPayment(P, annualRate, months) {
    var i = annualRate / 100 / 12;
    if (i === 0) { return P / months; }
    var g = Math.pow(1 + i, months);
    return P * i * g / (g - 1);
  }

  function simulate(P, annualRate, months, extra) {
    var i = annualRate / 100 / 12;
    var base = monthlyPayment(P, annualRate, months);
    var pay = base + (extra || 0);
    var balance = P;
    var totalInterest = 0;
    var curve = [P];
    var monthsPaid = 0;
    while (balance > 0 && monthsPaid < 600) {
      var interest = balance * i;
      var principal = pay - interest;
      if (principal <= 0) { principal = 0.01; }
      balance = Math.max(0, balance - principal);
      if (balance > 0 && balance < 0.005) { balance = 0; }
      totalInterest += interest;
      monthsPaid++;
      curve.push(Math.round(balance));
    }
    return { base: base, totalInterest: totalInterest, monthsPaid: monthsPaid, curve: curve };
  }

  var chart = null;

  function drawChart(simNoExtra, simWithExtra, cur) {
    var canvas = $("la-chart");
    if (chart) { chart.destroy(); }
    var labels = [];
    var maxLen = Math.max(simNoExtra.curve.length, simWithExtra.curve.length);
    for (var m = 0; m < maxLen; m++) { labels.push(m); }
    var datasets = [
      { label: "Without extra payment", data: simNoExtra.curve, borderColor: "#c5221f", backgroundColor: "rgba(197,34,31,0.08)", borderWidth: 2, pointRadius: 0, tension: 0.1, fill: true }
    ];
    if (simWithExtra.curve.length !== simNoExtra.curve.length) {
      datasets.push({ label: "With extra payment", data: simWithExtra.curve, borderColor: "#1a73e8", backgroundColor: "rgba(26,115,232,0.10)", borderWidth: 2, pointRadius: 0, tension: 0.1, fill: true });
    }
    chart = new Chart(canvas, {
      type: "line",
      data: {
        labels: labels,
        datasets: datasets
      },
      options: {
        responsive: true,
        plugins: {
          legend: { position: "bottom" },
          tooltip: { callbacks: { label: function (ctx) { return ctx.dataset.label + ": " + fmt(ctx.parsed.y, cur); } } }
        },
        scales: {
          x: { title: { display: true, text: "Month" } },
          y: { title: { display: true, text: "Balance" } }
        }
      }
    });
  }

  function update() {
    var P = parseAmount($("la-amount"));
    var rate = parseFloat(String($("la-rate").value).replace(",", ".")) || 0;
    var years = Math.max(1, Math.min(40, parseInt($("la-years").value, 10) || 1));
    var extra = Math.max(0, parseAmount($("la-extra")));
    var cur = $("la-currency").value;
    var months = years * 12;

    var base = monthlyPayment(P, rate, months);
    if (rate === 0 && months > 0 && P > 0) { base = P / months; }
    var noExtra = simulate(P, rate, months, 0);
    var withExtra = simulate(P, rate, months, extra);

    $("la-payment").textContent = fmt(Math.max(base, noExtra.base), cur);
    var interestLabel = $("la-interest");
    if (extra > 0) {
      var saved = noExtra.totalInterest - withExtra.totalInterest;
      interestLabel.textContent = fmt(withExtra.totalInterest, cur) + " (save " + fmt(saved, cur) + ")";
      interestLabel.className = "calc-value calc-ok";
    } else {
      interestLabel.textContent = fmt(noExtra.totalInterest, cur);
      interestLabel.className = "calc-value";
    }
    var payoffLabel = $("la-payoff");
    if (extra > 0) {
      if (withExtra.monthsPaid === noExtra.monthsPaid) {
        payoffLabel.textContent = fmtMonths(noExtra.monthsPaid, cur) + " (extra payment too small to shorten the term)";
      } else {
        payoffLabel.textContent = fmtMonths(withExtra.monthsPaid, cur) + " vs " + fmtMonths(noExtra.monthsPaid, cur);
      }
      payoffLabel.className = "calc-value calc-ok";
    } else {
      payoffLabel.textContent = fmtMonths(noExtra.monthsPaid, cur);
      payoffLabel.className = "calc-value";
    }
    drawChart(noExtra, withExtra, cur);
  }

  var ids = ["la-amount", "la-rate", "la-years", "la-extra", "la-currency"];
  for (var i = 0; i < ids.length; i++) {
    if (ids[i] === "la-amount" || ids[i] === "la-extra") { wireThousands($(ids[i])); }
    $(ids[i]).addEventListener("input", update);
    $(ids[i]).addEventListener("change", update);
  }
  update();
})();