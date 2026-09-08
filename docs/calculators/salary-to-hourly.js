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

  function update() {
    var annual = parseAmount($("st-annual"));
    var hours = Math.max(1, parseFloat(String($("st-hours").value).replace(",", ".")) || 0);
    var weeks = Math.max(1, parseInt($("st-weeks").value, 10) || 0);
    var cur = $("st-currency").value;
    var totalHours = hours * weeks;
    var hourly = totalHours > 0 ? annual / totalHours : 0;
    var weekly = hours > 0 ? (hourly * hours) : 0;
    var monthly = weeks > 0 ? (hourly * hours * 52) / 12 : 0;

    $("st-hourly").textContent = fmt(hourly, cur);
    $("st-weekly").textContent = fmt(weekly, cur);
    $("st-monthly").textContent = fmt(monthly, cur);
  }

  var ids = ["st-annual", "st-hours", "st-weeks", "st-currency"];
  for (var i = 0; i < ids.length; i++) {
    if (ids[i] === "st-annual") { wireThousands($(ids[i])); }
    $(ids[i]).addEventListener("input", update);
    $(ids[i]).addEventListener("change", update);
  }
  update();
})();