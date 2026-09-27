/* Balm theme documentation: mobile menu, client side search, and settings opened on a deep link. */
(function () {
  'use strict';

  /* ---------------------------------------------------------------- mobile menu */
  var toggle = document.querySelector('.nav-toggle');
  var sidebar = document.getElementById('sidebar');
  function setNav(open) {
    document.documentElement.classList.toggle('nav-open', open);
    if (toggle) toggle.setAttribute('aria-expanded', open ? 'true' : 'false');
  }
  if (toggle && sidebar) {
    toggle.addEventListener('click', function () {
      setNav(!document.documentElement.classList.contains('nav-open'));
    });
    sidebar.addEventListener('click', function (e) {
      if (e.target.closest('a')) setNav(false);
    });
    document.addEventListener('keydown', function (e) {
      if (e.key === 'Escape' && document.documentElement.classList.contains('nav-open')) {
        setNav(false);
        toggle.focus();
      }
    });
  }

  /* ---------------------------------------------------------------- deep links open their settings */
  function openTarget() {
    var id = decodeURIComponent(location.hash.slice(1));
    if (!id) return;
    var target = document.getElementById(id);
    if (!target) return;
    var entry = target.closest('.entry');
    if (entry && entry !== target.parentElement) entry = null;
    if (entry) {
      entry.querySelectorAll('details.settings-details').forEach(function (d) { d.open = true; });
    }
    var parentDetails = target.closest('details');
    if (parentDetails) parentDetails.open = true;
  }
  window.addEventListener('hashchange', openTarget);
  openTarget();

  /* ---------------------------------------------------------------- search */
  var input = document.getElementById('search-input');
  var box = document.getElementById('search-results');
  if (!input || !box) return;

  function fold(s) {
    return (s || '').toLowerCase().normalize('NFD').replace(/[̀-ͯ]/g, '');
  }
  var index = null;
  function getIndex() {
    if (index) return index;
    index = (window.BALM_SEARCH || []).map(function (r) {
      return { r: r, t: fold(r.t), p: fold(r.p), x: fold(r.x), l: fold(r.l) };
    });
    return index;
  }

  function escapeHtml(s) {
    return String(s).replace(/[&<>"']/g, function (c) {
      return { '&': '&amp;', '<': '&lt;', '>': '&gt;', '"': '&quot;', "'": '&#39;' }[c];
    });
  }
  function highlight(text, words) {
    var html = escapeHtml(text);
    words.forEach(function (w) {
      if (w.length < 2) return;
      var safe = w.replace(/[.*+?^${}()|[\]\\]/g, '\\$&');
      html = html.replace(new RegExp('(' + safe + ')', 'gi'), '<mark>$1</mark>');
    });
    return html;
  }
  function snippet(text, words) {
    var f = fold(text);
    var pos = -1;
    for (var i = 0; i < words.length && pos < 0; i++) pos = f.indexOf(words[i]);
    if (pos < 0) return text.slice(0, 150) + (text.length > 150 ? '...' : '');
    var start = Math.max(0, pos - 60);
    var out = text.slice(start, start + 170);
    return (start > 0 ? '...' : '') + out + (start + 170 < text.length ? '...' : '');
  }

  /* A word counts fully when it starts a word of the field, a little when it only sits inside one. */
  function wordScore(field, w, full, part) {
    var i = field.indexOf(w);
    if (i < 0) return -1;
    var best = part;
    while (i >= 0) {
      var starts = i === 0 || /[^a-z0-9]/.test(field.charAt(i - 1));
      var ends = i + w.length >= field.length || /[^a-z0-9]/.test(field.charAt(i + w.length));
      if (starts && ends) return full;
      if (starts) best = Math.max(best, full / 2);
      i = field.indexOf(w, i + 1);
    }
    return best;
  }

  function search(q) {
    var words = fold(q).split(/\s+/).filter(Boolean);
    if (!words.length) return [];
    var full = words.join(' ');
    var results = [];
    getIndex().forEach(function (e) {
      var score = 0;
      for (var i = 0; i < words.length; i++) {
        var w = words[i];
        var t = wordScore(e.t, w, 6, 1), p = wordScore(e.p, w, 2, 0.5), x = wordScore(e.x, w, 1, 0.2), l = wordScore(e.l, w, 1.5, 0.2);
        if (t < 0 && p < 0 && x < 0 && l < 0) return;
        score += Math.max(t, 0) + Math.max(p, 0) + Math.max(x, 0) + Math.max(l, 0);
      }
      if (e.t === full) score += 30;
      else if (wordScore(e.t, full, 1, 0) === 1) score += 14;
      if (words.length > 1 && wordScore(e.x, full, 1, 0) === 1) score += 6;
      if (wordScore(e.l, full, 1, 0) === 1) score += words.length > 1 ? 12 : 3;
      results.push({ e: e, s: score });
    });
    results.sort(function (a, b) { return b.s - a.s; });
    return results.slice(0, 12).map(function (x) { return x.e.r; });
  }

  function render() {
    var q = input.value.trim();
    if (!q) { close(); return; }
    var words = fold(q).split(/\s+/).filter(Boolean);
    var res = search(q);
    var html = '<p class="search-results__count" role="status">' +
      (res.length ? res.length + (res.length === 12 ? '+' : '') + ' result' + (res.length > 1 ? 's' : '') : 'No results for ' + escapeHtml(q)) +
      '</p>';
    if (res.length) {
      html += '<ul>' + res.map(function (r) {
        return '<li><a href="' + escapeHtml(r.u) + '">' +
          '<span class="r-title">' + highlight(r.t, words) + '</span>' +
          '<span class="r-page">' + escapeHtml(r.p) + '</span>' +
          (r.x ? '<span class="r-snip">' + highlight(snippet(r.x, words), words) + '</span>' : '') +
          '</a></li>';
      }).join('') + '</ul>';
    }
    box.innerHTML = html;
    box.hidden = false;
  }
  function close() {
    box.hidden = true;
    box.innerHTML = '';
  }

  var timer = null;
  input.addEventListener('input', function () {
    clearTimeout(timer);
    timer = setTimeout(render, 80);
  });
  input.addEventListener('focus', function () { if (input.value.trim()) render(); });

  function links() { return Array.prototype.slice.call(box.querySelectorAll('a')); }
  input.addEventListener('keydown', function (e) {
    if (e.key === 'ArrowDown') {
      var l = links();
      if (l.length) { e.preventDefault(); l[0].focus(); }
    } else if (e.key === 'Enter') {
      var first = links()[0];
      if (first) { e.preventDefault(); first.click(); }
    } else if (e.key === 'Escape') {
      input.value = '';
      close();
    }
  });
  box.addEventListener('keydown', function (e) {
    var l = links();
    var i = l.indexOf(document.activeElement);
    if (e.key === 'ArrowDown' && i < l.length - 1) { e.preventDefault(); l[i + 1].focus(); }
    else if (e.key === 'ArrowUp') { e.preventDefault(); if (i > 0) l[i - 1].focus(); else input.focus(); }
    else if (e.key === 'Escape') { e.preventDefault(); close(); input.focus(); }
  });
  box.addEventListener('click', function (e) {
    if (e.target.closest('a')) { close(); setNav(false); }
  });
  document.addEventListener('click', function (e) {
    if (!e.target.closest('.search')) close();
  });
  document.addEventListener('keydown', function (e) {
    var tag = (document.activeElement && document.activeElement.tagName) || '';
    if (e.key === '/' && !/INPUT|TEXTAREA|SELECT/.test(tag) && !e.metaKey && !e.ctrlKey && !e.altKey) {
      e.preventDefault();
      input.focus();
    }
  });
})();
