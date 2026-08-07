/* Usługi Hydrauliczne Ireneusz Stryszyk — skrypt strony */
(function () {
  'use strict';
  document.documentElement.classList.add('js');

  /* menu na telefonie */
  var burger = document.querySelector('.burger');
  var nav = document.querySelector('.nav');
  if (burger && nav) {
    burger.addEventListener('click', function () {
      var open = nav.classList.toggle('is-open');
      burger.setAttribute('aria-expanded', open ? 'true' : 'false');
    });
    nav.addEventListener('click', function (e) {
      if (e.target.tagName === 'A') {
        nav.classList.remove('is-open');
        burger.setAttribute('aria-expanded', 'false');
      }
    });
  }

  /* nagłówek: chowa się przy przewijaniu w dół, wraca przy przewijaniu w górę */
  var top = document.querySelector('.top');
  if (top) {
    var ostatniY = window.scrollY;
    var onScroll = function () {
      var y = window.scrollY;
      top.classList.toggle('is-stuck', y > 8);
      var menuOtwarte = nav && nav.classList.contains('is-open');
      if (!menuOtwarte) {
        /* chowamy dopiero poniżej pierwszego ekranu, żeby nie migało przy górze strony */
        if (y > 260 && y > ostatniY + 6) top.classList.add('is-hidden');
        else if (y < ostatniY - 6 || y < 120) top.classList.remove('is-hidden');
      }
      ostatniY = y;
    };
    onScroll();
    window.addEventListener('scroll', onScroll, { passive: true });
  }

  /* hero: przenikające kadry + podpis */
  var stage = document.querySelector('.hero-media');
  if (stage) {
    var frames = Array.prototype.slice.call(stage.querySelectorAll('figure'));
    var capBox = document.querySelector('.hero-cap');
    var i = 0;
    var show = function (n) {
      frames.forEach(function (f, k) { f.classList.toggle('is-on', k === n); });
      if (capBox) capBox.textContent = frames[n].getAttribute('data-cap') || '';
    };
    if (frames.length) {
      show(0);
      if (frames.length > 1 && !window.matchMedia('(prefers-reduced-motion: reduce)').matches) {
        setInterval(function () { i = (i + 1) % frames.length; show(i); }, 6500);
      }
    }
  }

  /* delikatne pojawianie się sekcji, z bezpiecznikiem */
  var rv = Array.prototype.slice.call(document.querySelectorAll('.rv'));
  if (rv.length) {
    var reveal = function (el) { el.classList.add('is-in'); };
    var revealWidoczne = function () {
      rv.forEach(function (el) {
        if (el.classList.contains('is-in')) return;
        var r = el.getBoundingClientRect();
        if (r.top < window.innerHeight * 1.15) reveal(el);
      });
    };

    if ('IntersectionObserver' in window) {
      var io = new IntersectionObserver(function (entries) {
        entries.forEach(function (en) {
          if (en.isIntersecting) { reveal(en.target); io.unobserve(en.target); }
        });
      }, { rootMargin: '0px 0px -8% 0px', threshold: 0.06 });
      rv.forEach(function (el) { io.observe(el); });
    } else {
      rv.forEach(reveal);
    }

    /* bezpieczniki: w karcie otwartej w tle obserwator bywa uśpiony,
       więc dokładamy sprawdzanie przy przewijaniu i twardy limit czasu */
    window.addEventListener('scroll', revealWidoczne, { passive: true });
    window.addEventListener('resize', revealWidoczne, { passive: true });
    document.addEventListener('visibilitychange', revealWidoczne);
    revealWidoczne();
    setTimeout(revealWidoczne, 900);
    setTimeout(function () { rv.forEach(reveal); }, 3500);
  }

  /* powiększanie zdjęć */
  var lb = document.querySelector('.lb');
  if (lb) {
    var lbImg = lb.querySelector('img');
    var lbCap = lb.querySelector('.lb-cap');
    var items = [];
    var cur = 0;

    var collect = function () {
      items = Array.prototype.slice.call(document.querySelectorAll('[data-zoom]'));
    };
    var open = function (n) {
      cur = (n + items.length) % items.length;
      var el = items[cur];
      lbImg.src = el.getAttribute('data-zoom');
      lbImg.alt = el.getAttribute('data-alt') || '';
      if (lbCap) lbCap.textContent = el.getAttribute('data-cap') || '';
      lb.hidden = false;
      document.body.style.overflow = 'hidden';
      lb.querySelector('.lb-x').focus();
    };
    var close = function () {
      lb.hidden = true;
      lbImg.removeAttribute('src');
      document.body.style.overflow = '';
    };

    collect();
    document.addEventListener('click', function (e) {
      var t = e.target.closest ? e.target.closest('[data-zoom]') : null;
      if (t) {
        e.preventDefault();
        collect();
        open(items.indexOf(t));
      }
    });
    lb.querySelector('.lb-x').addEventListener('click', close);
    lb.querySelector('.lb-p').addEventListener('click', function () { open(cur - 1); });
    lb.querySelector('.lb-n').addEventListener('click', function () { open(cur + 1); });
    lb.addEventListener('click', function (e) { if (e.target === lb) close(); });
    document.addEventListener('keydown', function (e) {
      if (lb.hidden) return;
      if (e.key === 'Escape') close();
      if (e.key === 'ArrowLeft') open(cur - 1);
      if (e.key === 'ArrowRight') open(cur + 1);
    });
  }

  /* formularz: wymagamy telefonu albo e-maila */
  var form = document.querySelector('form[data-form]');
  if (form) {
    form.addEventListener('submit', function (e) {
      var tel = form.querySelector('[name="telefon"]');
      var mail = form.querySelector('[name="email"]');
      var msg = form.querySelector('.form-error');
      if (tel && mail && !tel.value.trim() && !mail.value.trim()) {
        e.preventDefault();
        if (msg) {
          msg.textContent = 'Podaj telefon albo adres e-mail, żebyśmy mogli odpowiedzieć.';
          msg.style.color = '#8e2434';
        }
        tel.focus();
      }
    });
  }


  /* rok w stopce */
  var y = document.querySelector('[data-year]');
  if (y) y.textContent = new Date().getFullYear();
})();
