(function () {
  "use strict";

  var API_BASE = "https://mc-api-987883614051.europe-west1.run.app";
  var $ = function (id) { return document.getElementById(id); };
  var state = { rows: [], market: null, error: "" };
  var timer = null;

  var ids = {
    market: "mc-market",
    rows: "mc-rows",
    status: "mc-status",
    mcap: "scr-mcap",
    roe: "scr-roe",
    pbv: "scr-pbv",
    growth: "scr-growth",
    yield: "scr-yield",
    de: "scr-de",
    sector: "scr-sector",
    sort: "scr-sort",
    reset: "scr-reset"
  };

  function el(id) { return $(ids[id]); }

  function fmt(n, digits) {
    if (n === null || n === undefined || isNaN(n)) return "-";
    return Number(n).toLocaleString("id-ID", { minimumFractionDigits: digits, maximumFractionDigits: digits });
  }

  function fmtPct(n) { return fmt(n, 1) + "%"; }

  function fmtRp(n) { return "Rp " + Number(n).toLocaleString("id-ID", { maximumFractionDigits: 0 }); }

  function fmtTrillion(n) {
    if (n === null || n === undefined || isNaN(n)) return "-";
    return fmt(n / 1e12, 1);
  }

  function regimeBadge(regime) {
    if (regime === "bull") return '<span class="mc-badge mc-badge-bull">Bull market</span>';
    if (regime === "bear") return '<span class="mc-badge mc-badge-bear">Bear market</span>';
    return '<span class="mc-badge">' + (regime || "-") + "</span>";
  }

  function scorePill(score) {
    var cls = score >= 60 ? "score-hi" : score >= 45 ? "score-mid" : "score-lo";
    return '<span class="score-pill ' + cls + '">' + fmt(score, 1) + "</span>";
  }

  function renderMarket(m) {
    if (!m) return;
    var strip = el("market");
    strip.innerHTML =
      '<div class="mc-stat"><span class="mc-stat-label">Market regime</span>' +
      '<span class="mc-stat-value">' + regimeBadge(m.regime) + "</span></div>" +
      '<div class="mc-stat"><span class="mc-stat-label">IHSG close</span>' +
      '<span class="mc-stat-value">' + fmt(m.ihsg_close, 2) + "</span></div>" +
      '<div class="mc-stat"><span class="mc-stat-label">IHSG vs SMA60</span>' +
      '<span class="mc-stat-value">' + fmt(m.ihsg_sma60, 2) + "</span></div>" +
      '<div class="mc-stat"><span class="mc-stat-label">5-day breadth</span>' +
      '<span class="mc-stat-value">' + fmt(m.breadth_pct, 1) + "%</span>" +
      '<span class="mc-stat-label">' + m.advancers_5d + " adv / " + m.decliners_5d + " dec" + "</span></div>" +
      '<div class="mc-stat"><span class="mc-stat-label">Data as of</span>' +
      '<span class="mc-stat-value">' + (m.asof || "-") + "</span></div>";
  }

  function renderRows() {
    var sortKey = el("sort").value;
    var rows = state.rows.slice();
    var sortMap = {
      score: function (a, b) { return b.score - a.score; },
      roe: function (a, b) { return b.roe_pct - a.roe_pct; },
      yield: function (a, b) { return b.div_yield_pct - a.div_yield_pct; },
      growth: function (a, b) { return b.growth_pct - a.growth_pct; },
      pbv: function (a, b) { return a.pbv - b.pbv; },
      mcap: function (a, b) { return b.market_cap - a.market_cap; }
    };
    rows.sort(sortMap[sortKey] || sortMap.score);

    var tbody = el("rows");
    if (!rows.length) {
      tbody.innerHTML = '<tr><td colspan="11">No stocks match these filters.</td></tr>';
      return;
    }
    var html = "";
    for (var i = 0; i < rows.length; i++) {
      var r = rows[i];
      html +=
        "<tr>" +
        "<td><strong>" + r.ticker + "</strong></td>" +
        '<td class="num">' + fmtRp(r.price) + "</td>" +
        '<td class="num">' + fmtTrillion(r.market_cap) + "</td>" +
        '<td class="num">' + fmt(r.pe, 1) + "</td>" +
        '<td class="num">' + fmtPct(r.roe_pct) + "</td>" +
        '<td class="num">' + fmt(r.pbv, 2) + "</td>" +
        '<td class="num">' + fmt(r.de, 2) + "</td>" +
        '<td class="num">' + fmtPct(r.growth_pct) + "</td>" +
        '<td class="num">' + fmtPct(r.div_yield_pct) + "</td>" +
        "<td>" + (r.sector || "-") + "</td>" +
        '<td class="num">' + scorePill(r.score) + "</td>" +
        "</tr>";
    }
    tbody.innerHTML = html;
  }

  function renderStatus() {
    var s = el("status");
    if (state.error) {
      s.textContent = state.error;
      return;
    }
    s.textContent = state.rows.length
      ? state.rows.length + " stocks match your filters"
      : "Screener data not loaded yet.";
  }

  function fetchSectors() {
    fetch(API_BASE + "/api/screener?limit=200")
      .then(function (r) { return r.ok ? r.json() : null; })
      .then(function (data) {
        if (!data || !data.rows) return;
        var seen = {};
        var sectors = [];
        data.rows.forEach(function (r) {
          var s = r.sector;
          if (s && !seen[s]) { seen[s] = true; sectors.push(s); }
        });
        sectors.sort();
        var sel = el("sector");
        var cur = sel.value;
        sel.innerHTML = '<option value="">All sectors</option>' +
          sectors.map(function (s) { return '<option value="' + s + '">' + s + "</option>"; }).join("");
        if (sectors.indexOf(cur) !== -1) sel.value = cur;
      })
      .catch(function () {});
  }

  function fetchScreener() {
    var params = {
      min_mcap_bn: String(Math.round(parseFloat(el("mcap").value || "0") * 1000)),
      min_roe: el("roe").value || "0",
      max_pbv: el("pbv").value || "",
      min_growth: el("growth").value || "0",
      min_yield: el("yield").value || "0",
      max_de: el("de").value || "",
      sector: el("sector").value,
      limit: "200"
    };
    var qs = Object.keys(params)
      .filter(function (k) { return params[k] !== ""; })
      .map(function (k) { return k + "=" + encodeURIComponent(params[k]); })
      .join("&");
    fetch(API_BASE + "/api/screener?" + qs)
      .then(function (r) {
        if (!r.ok) throw new Error("HTTP " + r.status);
        return r.json();
      })
      .then(function (data) {
        state.rows = data.rows || [];
        state.error = "";
        renderStatus();
        renderRows();
      })
      .catch(function () {
        state.error = "Screener data is temporarily unavailable. Please try again in a moment.";
        renderStatus();
      });
  }

  function fetchMarket() {
    fetch(API_BASE + "/api/market")
      .then(function (r) {
        if (!r.ok) throw new Error("HTTP " + r.status);
        return r.json();
      })
      .then(function (m) {
        state.market = m;
        renderMarket(m);
      })
      .catch(function () {});
  }

  function scheduleFetch() {
    clearTimeout(timer);
    timer = setTimeout(fetchScreener, 350);
  }

  function wire() {
    if (!el("rows")) return;
    ["mcap", "roe", "pbv", "growth", "yield", "de", "sector", "sort"].forEach(function (k) {
      el(k).addEventListener("input", scheduleFetch);
      el(k).addEventListener("change", scheduleFetch);
    });
    el("reset").addEventListener("click", function () {
      el("mcap").value = "10";
      el("roe").value = "15";
      el("pbv").value = "2";
      el("growth").value = "5";
      el("yield").value = "3";
      el("de").value = "1";
      el("sector").value = "";
      el("sort").value = "score";
      fetchScreener();
    });
    fetchMarket();
    fetchSectors();
    fetchScreener();
  }

  document.addEventListener("DOMContentLoaded", wire);
  if (document.readyState !== "loading") wire();
})();
