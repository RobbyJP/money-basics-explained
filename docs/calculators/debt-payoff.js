(function () {
  "use strict";

  var $ = function (id) { return document.getElementById(id); };

  function fmt(v, cur) {
    var r = Math.round(v);
    if (cur === "IDR") { return "Rp " + r.toLocaleString("id-ID"); }
    return "$" + Number(v).toLocaleString("en-US", { minimumFractionDigits: 2, maximumFractionDigits: 2 });
  }

  function fmtMonths(m) {
    if (m >= 1200) { return "120+ years"; }
    var y = Math.floor(m / 12), mo = m % 12;
    if (y === 0) { return mo + " months"; }
    return mo === 0 ? y + " yrs" : y + " yrs " + mo + " mo";
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

  function debtRow(index, data) {
    var d = data || { name: "", balance: "", apr: "", min: "" };
    var div = document.createElement("div");
    div.className = "dp-row";
    div.id = "dp-row-" + index;
    div.innerHTML =
      '<div class="dp-fields">' +
      '<div class="calc-row"><label>Debt name</label><input class="dp-name" type="text" value="' + d.name + '" placeholder="Credit card"></div>' +
      '<div class="calc-row"><label>Balance</label><input class="dp-balance" type="text" inputmode="decimal" value="' + d.balance + '"></div>' +
      '<div class="calc-row"><label>APR (%)</label><input class="dp-apr" type="number" min="0" step="any" value="' + d.apr + '" inputmode="decimal"></div>' +
      '<div class="calc-row"><label>Minimum payment</label><input class="dp-min" type="text" inputmode="decimal" value="' + d.min + '"></div>' +
      '</div>' +
      '<button type="button" class="calc-btn calc-btn-small dp-remove" aria-label="Remove this debt">&times;</button>';
    div.querySelector(".dp-remove").addEventListener("click", function () {
      div.remove();
      update();
    });
    div.querySelectorAll("input").forEach(function (inp) {
      if (inp.classList.contains("dp-balance") || inp.classList.contains("dp-min")) { wireThousands(inp); }
      inp.addEventListener("input", update);
      inp.addEventListener("change", update);
    });
    return div;
  }

  var nextIndex = 0;
  function addRow(data) {
    $("dp-debts").appendChild(debtRow(nextIndex++, data));
  }

  function readDebts() {
    var out = [];
    document.querySelectorAll("#dp-debts .dp-row").forEach(function (row) {
      out.push({
        name: row.querySelector(".dp-name").value.trim() || "Debt",
        balance: parseAmount(row.querySelector(".dp-balance")),
        apr: parseFloat(row.querySelector(".dp-apr").value) || 0,
        min: parseAmount(row.querySelector(".dp-min"))
      });
    });
    return out;
  }

  function simulate(debts, extraMonthly, strategy) {
    var ds = debts.map(function (d) { return { bal: d.balance, apr: d.apr, min: d.min }; });
    var months = 0, interest = 0;
    while (true) {
      var active = ds.filter(function (x) { return x.bal > 0.01; });
      if (!active.length) { break; }
      if (months >= 1200) { months = 1200; break; }
      months++;
      for (var i = 0; i < ds.length; i++) {
        if (ds[i].bal > 0) {
          var inc = (ds[i].bal * ds[i].apr / 100) / 12;
          ds[i].bal += inc;
          interest += inc;
        }
      }
      var target = null;
      if (strategy === "snowball") {
        var smallest = null;
        for (var j = 0; j < ds.length; j++) {
          if (ds[j].bal > 0.01 && (!smallest || ds[j].bal < smallest.bal)) { smallest = ds[j]; }
        }
        target = smallest;
      } else {
        var highest = null;
        for (var k = 0; k < ds.length; k++) {
          if (ds[k].bal > 0.01 && (!highest || ds[k].apr > highest.apr)) { highest = ds[k]; }
        }
        target = highest;
      }
      for (var m = 0; m < ds.length; m++) {
        if (ds[m].bal <= 0.01 || ds[m] === target) { continue; }
        ds[m].bal -= Math.min(ds[m].min, ds[m].bal);
      }
      target.bal -= Math.min(target.min + extraMonthly, target.bal);
    }
    return { months: months, interest: interest };
  }

  function update() {
    var debts = readDebts();
    var extra = parseAmount($("dp-extra"));
    var cur = $("dp-currency").value;
    if (!debts.length) {
      $("dp-snow-time").textContent = "-";
      $("dp-snow-interest").textContent = "-";
      $("dp-ava-time").textContent = "-";
      $("dp-ava-interest").textContent = "-";
      $("dp-saved").textContent = "Add at least one debt above.";
      return;
    }
    var totalBal = debts.reduce(function (s, d) { return s + d.balance; }, 0);
    var snow = simulate(debts, extra, "snowball");
    var ava = simulate(debts, extra, "avalanche");
    $("dp-snow-time").textContent = fmtMonths(snow.months);
    $("dp-snow-interest").textContent = fmt(snow.interest, cur) + " interest";
    $("dp-ava-time").textContent = fmtMonths(ava.months);
    $("dp-ava-interest").textContent = fmt(ava.interest, cur) + " interest";
    var saved = ava.interest - snow.interest;
    if (ava.months === 1200 || snow.months === 1200) {
      $("dp-saved").textContent = "Total debt: " + fmt(totalBal, cur) + ". The simulation did not finish within 100 years â€” increase the extra payment or check the minimums.";
    } else if (saved > 0) {
      $("dp-saved").textContent = "Avalanche saves about " + fmt(saved, cur) + " in interest compared with snowball, but snowball clears the first debt faster. Both are valid â€” the best strategy is the one you can actually stick to.";
    } else {
      $("dp-saved").textContent = "Both strategies finish in the same time and pay the same interest here (same APR on all debts). Strategy choice matters most when APRs differ.";
    }
  }

  $("dp-add").addEventListener("click", function () { addRow(null); update(); });
  wireThousands($("dp-extra"));
  $("dp-extra").addEventListener("input", update);
  $("dp-currency").addEventListener("change", update);

  addRow({ name: "Credit card", balance: "10.000.000", apr: "24", min: "400.000" });
  addRow({ name: "Motorcycle loan", balance: "20.000.000", apr: "12", min: "800.000" });
  update();
})();
