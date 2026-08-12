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

  function band(rate) {
    if (rate < 0) return { label: "Negative", cls: "calc-warn" };
    if (rate < 10) return { label: "Starter", cls: "calc-warn" };
    if (rate < 20) return { label: "Solid", cls: "calc-ok" };
    if (rate < 30) return { label: "Strong", cls: "calc-ok" };
    return { label: "Fast-track", cls: "calc-ok" };
  }

  var chart = null;

  function drawChart(rate, cur) {
    var canvas = $("sr-chart");
    if (chart) { chart.destroy(); }
    chart = new Chart(canvas, {
      type: "bar",
      data: {
        labels: ["You", "20% benchmark"],
        datasets: [
          { label: "Savings rate", data: [Math.max(0, Math.min(100, rate)), 20], backgroundColor: ["#1a73e8", "#dadce0"] }
        ]
      },
      options: {
        indexAxis: "y",
        responsive: true,
        plugins: {
          legend: { display: false },
          tooltip: { callbacks: { label: function (ctx) { return ctx.parsed.x.toFixed(1) + "%"; } } }
        },
        scales: {
          x: { min: 0, max: 100, title: { display: true, text: "Percent of income saved" } },
          y: { ticks: { autoSkip: false } }
        }
      }
    });
  }

  function update() {
    var income = parseAmount($("sr-income"));
    var saved = parseAmount($("sr-saved"));
    var cur = $("sr-currency").value;
    var rate = income > 0 ? (saved / income) * 100 : 0;
    var spent = income - saved;

    var b = band(rate);
    $("sr-rate").textContent = rate.toFixed(1) + "%";
    $("sr-spent").textContent = fmt(spent, cur);
    var bEl = $("sr-band");
    bEl.textContent = b.label;
    bEl.className = "calc-value " + b.cls;
    drawChart(rate, cur);
  }

  var ids = ["sr-income", "sr-saved", "sr-currency"];
  for (var i = 0; i < ids.length; i++) {
    if (ids[i] === "sr-income" || ids[i] === "sr-saved") { wireThousands($(ids[i])); }
    $(ids[i]).addEventListener("input", update);
    $(ids[i]).addEventListener("change", update);
  }
  update();
})();