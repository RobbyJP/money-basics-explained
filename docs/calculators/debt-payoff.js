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

  function debtRow(index, data) {
    var d = data || { name: "", balance: "", apr: "", min: "" };
    var div = document.createElement("div");
    div.className = "dp-row";
    div.id = "dp-row-" + index;
    div.innerHTML =
      '<div class="dp-fields">' +
      '<div class="calc-row"><label>Debt name</label><input class="dp-name" type="text" value="' + d.name + '" placeholder="Credit card"></div>' +
      '<div class="calc-row"><label>Balance</label><input class="dp-balance" type="number" min="0" step="any" value="' + d.balance + '" inputmode="decimal"></div>' +
      '<div class="calc-row"><label>APR (%)</label><input class="dp-apr" type="number" min="0" step="any" value="' + d.apr + '" inputmode="decimal"></div>' +
      '<div class="calc-row"><label>Minimum payment</label><input class="dp-min" type="number" min="0" step="any" value="' + d.min + '" inputmode="decimal"></div>' +
      '</div>' +
      '<button type="button" class="calc-btn calc-btn-small dp-remove" aria-label="Remove this debt">&times;</button>';
    div.querySelector(".dp-remove").addEventListener("click", function () {
      div.remove();
      update();
    });
    div.querySelectorAll("input").forEach(function (inp) {
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
        balance: parseFloat(row.querySelector(".dp-balance").value) || 0,
        apr: parseFloat(row.querySelector(".dp-apr").value) || 0,
        min: parseFloat(row.querySelector(".dp-min").value) || 0
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
    var extra = parseFloat($("dp-extra").value) || 0;
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
      $("dp-saved").textContent = "Total debt: " + fmt(totalBal, cur) + ". The simulation did not finish within 100 years — increase the extra payment or check the minimums.";
    } else if (saved > 0) {
      $("dp-saved").textContent = "Avalanche saves about " + fmt(saved, cur) + " in interest compared with snowball, but snowball clears the first debt faster. Both are valid — the best strategy is the one you can actually stick to.";
    } else {
      $("dp-saved").textContent = "Both strategies finish in the same time and pay the same interest here (same APR on all debts). Strategy choice matters most when APRs differ.";
    }
  }

  $("dp-add").addEventListener("click", function () { addRow(null); update(); });
  $("dp-extra").addEventListener("input", update);
  $("dp-currency").addEventListener("change", update);

  addRow({ name: "Credit card", balance: "10000000", apr: "24", min: "400000" });
  addRow({ name: "Motorcycle loan", balance: "20000000", apr: "12", min: "800000" });
  update();
})();
