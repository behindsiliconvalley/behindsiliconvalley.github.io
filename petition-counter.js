/**
 * petition-counter.js
 * Fetches live petition signature counts from a public Google Sheet
 * and updates all petition-related elements on the page.
 * Falls back gracefully to hardcoded HTML values if fetch fails.
 */
(function () {
  'use strict';

  var SHEET_ID = '1zgCs5E3Qj5zNDw-G6z0A78Kk5-keVuZGEspbXFtxrHE';
  var JSON_URL = 'https://docs.google.com/spreadsheets/d/' + SHEET_ID + '/gviz/tq?tqx=out:json';
  var GOAL = 15000;

  function fmt(n) {
    return n.toString().replace(/\B(?=(\d{3})+(?!\d))/g, ',');
  }

  function parseGvizJson(text) {
    var start = text.indexOf('(');
    var end = text.lastIndexOf(')');
    if (start === -1 || end === -1) throw new Error('Invalid response');
    return JSON.parse(text.substring(start + 1, end));
  }

  function getLastValue(cells) {
    for (var i = cells.length - 1; i >= 2; i--) {
      if (cells[i] && typeof cells[i].v === 'number') return cells[i].v;
    }
    return 0;
  }

  function fetchPetitionData() {
    fetch(JSON_URL)
      .then(function (r) {
        if (!r.ok) throw new Error('HTTP ' + r.status);
        return r.text();
      })
      .then(function (text) {
        var data = parseGvizJson(text);
        var rows = data.table.rows;
        var total = 0;
        var schools = [];

        for (var r = 0; r < rows.length; r++) {
          var cells = rows[r].c;
          if (!cells || !cells[1]) continue;
          var name = cells[1].v;
          if (!name || typeof name !== 'string') continue;
          if (name === 'School Name') continue;

          if (name === 'Totals') {
            total = Math.round(getLastValue(cells));
            continue;
          }

          var count = Math.round(getLastValue(cells));
          var url = (cells[0] && cells[0].v) ? cells[0].v : '';
          if (count > 0) schools.push({ name: name, count: count, url: url });
        }

        if (!total && schools.length) {
          for (var s = 0; s < schools.length; s++) total += schools[s].count;
        }

        if (total > 0) updateDOM(total, schools);
      })
      .catch(function (err) {
        console.warn('Petition counter: could not fetch live data.', err);
      });
  }

  function updateDOM(total, schools) {
    var tf = fmt(total);
    var pct = Math.min((total / GOAL) * 100, 100);

    var countEl = document.getElementById('petition-count');
    if (countEl) countEl.textContent = tf + '+';

    var fillEl = document.getElementById('petition-fill');
    if (fillEl) fillEl.style.width = pct.toFixed(1) + '%';

    var barLabel = document.getElementById('petition-bar-label');
    if (barLabel) barLabel.textContent = tf + ' / ' + fmt(GOAL);

    var stickyBtn = document.getElementById('sticky-petition-btn');
    if (stickyBtn && stickyBtn.dataset.prefix) {
      stickyBtn.textContent = stickyBtn.dataset.prefix + tf + stickyBtn.dataset.suffix;
    }

    var joinText = document.getElementById('petition-join-text');
    if (joinText && joinText.dataset.prefix) {
      joinText.textContent = joinText.dataset.prefix + tf + joinText.dataset.suffix;
    }

    var heroCount = document.getElementById('hero-petition-count');
    if (heroCount) {
      var text = heroCount.textContent;
      heroCount.textContent = text.replace(/[\d,]+\+/, tf + '+');
    }

    var breakdown = document.getElementById('petition-breakdown');
    if (breakdown && schools.length > 0) {
      schools.sort(function (a, b) { return b.count - a.count; });
      var label = breakdown.dataset.breakdownLabel || 'Signatures by petition:';
      var html = '<div style="font-weight:600;margin-bottom:8px;color:#1565c0;font-size:0.95em;">' + label + '</div>';
      var max = schools[0].count;
      for (var i = 0; i < schools.length; i++) {
        var s = schools[i];
        var w = Math.min((s.count / max) * 100, 100);
        html += '<div style="margin-bottom:6px;display:flex;align-items:center;gap:8px;">'
          + '<span style="flex:0 0 200px;font-size:0.9em;">' + (s.url ? '<a href="' + s.url + '" target="_blank" style="color:#1565c0;text-decoration:none;">' + s.name + '</a>' : s.name) + '</span>'
          + '<div style="flex:1;height:10px;background:#e3f2fd;border-radius:5px;overflow:hidden;">'
          + '<div style="height:100%;width:' + w.toFixed(0) + '%;background:#1976d2;border-radius:5px;transition:width 1s ease-out;"></div>'
          + '</div>'
          + '<span style="min-width:50px;text-align:right;font-family:\'JetBrains Mono\',monospace;font-size:0.85em;">' + fmt(s.count) + '</span>'
          + '</div>';
      }
      breakdown.innerHTML = html;
      breakdown.style.display = 'block';
    }

    var source = document.getElementById('petition-source');
    if (source) source.style.display = 'block';
  }

  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', fetchPetitionData);
  } else {
    fetchPetitionData();
  }
})();
