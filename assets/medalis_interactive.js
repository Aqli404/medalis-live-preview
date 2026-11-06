/**
 * Medalis Live Preview — Interactive Engine (Olimpix AI)
 * - Clean, native UI without artificial developer toolbars
 * - Olimpix AI voice narration & haptics
 * - Auto-theme switcher synced with OS preference
 * - Soft haptic click audio via Web Audio API
 * - Early Learner TK interactive animations & voice narration ("Bacakan Soal")
 * - Lembar Tryout interactive option selection
 * - Live ticking countdown timer for CBT HUD
 * - Draggable Hero CBT HUD Card with minimize/expand
 * - 20 Screens Client Showcase Dock (Floating Demo Panel with Pure Inline SVGs)
 */

const SCREENS_CATALOG = [
  {
    category: "Publik & Akun",
    iconSvg: `<svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><circle cx="12" cy="12" r="10"></circle><line x1="2" y1="12" x2="22" y2="12"></line><path d="M12 2a15.3 15.3 0 0 1 4 10 15.3 15.3 0 0 1-4 10 15.3 15.3 0 0 1-4-10 15.3 15.3 0 0 1 4-10z"></path></svg>`,
    items: [
      { name: "Landing Page", base: "landing" },
      { name: "Paket & Harga (Pricing)", base: "pricing" },
      { name: "Laporan WhatsApp Bunda", base: "laporan-whatsapp" },
      { name: "Halaman Masuk (Login)", base: "login" },
      { name: "Orientasi Siswa (Onboarding)", base: "onboarding" }
    ]
  },
  {
    category: "Portal Belajar Siswa",
    iconSvg: `<svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M22 10v6M2 10l10-5 10 5-10 5z"></path><path d="M6 12v5c3 3 9 3 12 0v-5"></path></svg>`,
    items: [
      { name: "Dashboard Siswa", base: "dashboard" },
      { name: "Katalog Modul Resmi", base: "daftar-modul" },
      { name: "Pembaca E-Book Interaktif", base: "ebook-reader" },
      { name: "Tanya Guru Olimpix AI", base: "guru-ai" },
      { name: "Jadwal & Prep Timeline", base: "prep-timeline" }
    ]
  },
  {
    category: "Simulasi Ujian CBT",
    iconSvg: `<svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><circle cx="12" cy="12" r="10"></circle><polyline points="12 6 12 12 16 14"></polyline></svg>`,
    items: [
      { name: "Lobby Tryout Puspresnas", base: "lobby-tryout" },
      { name: "Lembar Ujian CBT Online", base: "lembar-tryout" },
      { name: "Hasil Skor & Analisis", base: "hasil-tryout" },
      { name: "Pembahasan Soal & Kunci", base: "pembahasan" }
    ]
  },
  {
    category: "Early Learner TK",
    iconSvg: `<svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><circle cx="12" cy="12" r="10"></circle><path d="M8 14s1.5 2 4 2 4-2 4-2"></path><line x1="9" y1="9" x2="9.01" y2="9"></line><line x1="15" y1="9" x2="15.01" y2="9"></line></svg>`,
    items: [
      { name: "Modul Usia Dini (TK)", base: "early-learner-tk" },
      { name: "Menara Balok Mini-Game", base: "tk-menara-balok" }
    ]
  },
  {
    category: "System & State Pages",
    iconSvg: `<svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M12 22s8-4 8-10V5l-8-3-8 3v7c0 6 8 10 8 10z"></path></svg>`,
    items: [
      { name: "Peringatan Anti-Cheat", base: "state-anti-cheat" },
      { name: "Indikator Mode Offline", base: "state-offline" },
      { name: "Riwayat Kosong (Empty)", base: "state-empty" },
      { name: "Halaman 404 Not Found", base: "state-404" }
    ]
  }
];

// Audio Context Singleton
let audioCtx = null;
function getAudioContext() {
  if (!audioCtx) {
    audioCtx = new (window.AudioContext || window.webkitAudioContext)();
  }
  if (audioCtx.state === 'suspended') {
    audioCtx.resume();
  }
  return audioCtx;
}

// Soft UI click sound (~750Hz sine curve)
function playSoftClick() {
  try {
    const ctx = getAudioContext();
    const osc = ctx.createOscillator();
    const gain = ctx.createGain();
    osc.type = 'sine';
    osc.frequency.setValueAtTime(750, ctx.currentTime);
    osc.frequency.exponentialRampToValueAtTime(350, ctx.currentTime + 0.045);
    gain.gain.setValueAtTime(0.06, ctx.currentTime);
    gain.gain.exponentialRampToValueAtTime(0.001, ctx.currentTime + 0.045);
    osc.connect(gain);
    gain.connect(ctx.destination);
    osc.start();
    osc.stop(ctx.currentTime + 0.045);
  } catch(e) {}
}

// Victory Ding Chime for answers / early learner
function playChime() {
  try {
    const ctx = getAudioContext();
    const freqs = [523.25, 659.25, 783.99, 1046.50];
    freqs.forEach((f, idx) => {
      const osc = ctx.createOscillator();
      const gain = ctx.createGain();
      osc.type = 'triangle';
      const t = ctx.currentTime + idx * 0.07;
      osc.frequency.setValueAtTime(f, t);
      gain.gain.setValueAtTime(0.12, t);
      gain.gain.exponentialRampToValueAtTime(0.001, t + 0.35);
      osc.connect(gain);
      gain.connect(ctx.destination);
      osc.start(t);
      osc.stop(t + 0.35);
    });
  } catch(e) {}
}

// Handle Auto Theme (Sistem)
function handleAutoTheme() {
  playSoftClick();
  const isDarkOS = window.matchMedia && window.matchMedia('(prefers-color-scheme: dark)').matches;
  const currentPath = window.location.pathname;
  let target;
  if (isDarkOS) {
    target = currentPath.includes('-terang.html') ? currentPath.replace('-terang.html', '-gelap.html') : 'landing-gelap.html';
  } else {
    target = currentPath.includes('-gelap.html') ? currentPath.replace('-gelap.html', '-terang.html') : 'landing-terang.html';
  }
  window.location.href = target;
}
window.handleAutoTheme = handleAutoTheme;

// Global click audio listener
function setupGlobalClickSounds() {
  document.addEventListener('click', (e) => {
    const clickable = e.target.closest('a, button, [role="button"], .cursor-pointer');
    if (clickable) {
      playSoftClick();
    }
  }, true);
}

// Live ticking countdown timer
function setupLiveTimer() {
  const timerEls = document.querySelectorAll('#live-cbt-timer, .font-timer');
  if (!timerEls || timerEls.length === 0) return;

  let totalSeconds = 1 * 3600 + 24 * 60 + 19; // 01:24:19 default

  setInterval(() => {
    if (totalSeconds > 0) {
      totalSeconds--;
      const h = Math.floor(totalSeconds / 3600);
      const m = Math.floor((totalSeconds % 3600) / 60);
      const s = totalSeconds % 60;
      const formatted = `${String(h).padStart(2, '0')}:${String(m).padStart(2, '0')}:${String(s).padStart(2, '0')}`;
      
      timerEls.forEach(el => {
        if (el.textContent.includes(':')) {
          el.textContent = formatted;
        }
      });
    }
  }, 1000);
}

// Draggable & Minimizable Hero CBT HUD Card
function setupDraggableHeroHUD() {
  const hud = document.getElementById('hero-cbt-hud') || document.querySelector('.hero-cbt-draggable');
  if (!hud) return;

  let isDragging = false;
  let startX, startY;
  let initialLeft, initialTop;

  hud.addEventListener('mousedown', (e) => {
    if (e.target.closest('a, button')) return;
    isDragging = true;
    startX = e.clientX;
    startY = e.clientY;
    
    const rect = hud.getBoundingClientRect();
    hud.style.bottom = 'auto';
    hud.style.right = 'auto';
    hud.style.left = `${rect.left}px`;
    hud.style.top = `${rect.top}px`;
    hud.style.position = 'fixed';
    initialLeft = rect.left;
    initialTop = rect.top;
    e.preventDefault();
  });

  window.addEventListener('mousemove', (e) => {
    if (!isDragging) return;
    const dx = e.clientX - startX;
    const dy = e.clientY - startY;
    hud.style.left = `${initialLeft + dx}px`;
    hud.style.top = `${initialTop + dy}px`;
  });

  window.addEventListener('mouseup', () => {
    isDragging = false;
  });

  // Touch support
  hud.addEventListener('touchstart', (e) => {
    if (e.target.closest('a, button')) return;
    const touch = e.touches[0];
    isDragging = true;
    startX = touch.clientX;
    startY = touch.clientY;
    const rect = hud.getBoundingClientRect();
    hud.style.bottom = 'auto';
    hud.style.right = 'auto';
    hud.style.left = `${rect.left}px`;
    hud.style.top = `${rect.top}px`;
    hud.style.position = 'fixed';
    initialLeft = rect.left;
    initialTop = rect.top;
  }, { passive: true });

  window.addEventListener('touchmove', (e) => {
    if (!isDragging) return;
    const touch = e.touches[0];
    const dx = touch.clientX - startX;
    const dy = touch.clientY - startY;
    hud.style.left = `${initialLeft + dx}px`;
    hud.style.top = `${initialTop + dy}px`;
  }, { passive: true });

  window.addEventListener('touchend', () => {
    isDragging = false;
  });

  // Minimize / Expand button
  const minBtn = document.getElementById('hud-minimize-btn');
  if (minBtn) {
    let isMinimized = false;
    const originalChildren = Array.from(hud.children);
    
    minBtn.addEventListener('click', (e) => {
      e.stopPropagation();
      playSoftClick();
      isMinimized = !isMinimized;
      if (isMinimized) {
        hud.classList.add('hero-cbt-minimized');
        hud.innerHTML = `
          <div class="flex items-center gap-2 cursor-pointer" id="hud-expand-trigger">
            <span class="relative flex h-2 w-2"><span class="animate-ping absolute inline-flex h-full w-full rounded-full bg-emerald opacity-75"></span><span class="relative inline-flex rounded-full h-2 w-2 bg-emerald"></span></span>
            <span class="text-xs font-bold text-white tracking-wide">Simulasi CBT</span>
            <span class="text-[11px] text-[#D4A747] font-semibold font-timer ml-1">01:24:19</span>
            <span class="text-[#94A3B8] text-xs hover:text-white ml-1.5">[⤢ Buka]</span>
          </div>
        `;
        document.getElementById('hud-expand-trigger').addEventListener('click', () => {
          minBtn.click();
        });
      } else {
        hud.classList.remove('hero-cbt-minimized');
        hud.innerHTML = '';
        originalChildren.forEach(child => hud.appendChild(child));
        setupDraggableHeroHUD();
      }
    });
  }
}

// 20 Screens Showcase Dock (Pure SVG Icons, Zero Font Ligature Glitch)
function setupScreensShowcaseDock() {
  if (document.getElementById('demo-dock-trigger')) return;

  const currentPath = window.location.pathname.toLowerCase();

  // Floating Trigger Button
  const trigger = document.createElement('button');
  trigger.id = 'demo-dock-trigger';
  trigger.type = 'button';
  trigger.innerHTML = `
    <span class="demo-trigger-dot"></span>
    <svg width="15" height="15" viewBox="0 0 24 24" fill="none" stroke="#D4A747" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round">
      <rect x="3" y="3" width="7" height="7"></rect>
      <rect x="14" y="3" width="7" height="7"></rect>
      <rect x="14" y="14" width="7" height="7"></rect>
      <rect x="3" y="14" width="7" height="7"></rect>
    </svg>
    <span>20 Layar Demo</span>
  `;

  // Showcase Panel Drawer
  const panel = document.createElement('div');
  panel.id = 'demo-dock-panel';

  let bodyHtml = '';
  SCREENS_CATALOG.forEach(cat => {
    bodyHtml += `
      <div class="demo-group-box">
        <div class="demo-group-title">
          <div class="demo-group-left">
            ${cat.iconSvg}
            <span>${cat.category}</span>
          </div>
          <span class="demo-group-count">${cat.items.length} layar</span>
        </div>
    `;
    cat.items.forEach(item => {
      const isCurrentTerang = currentPath.endsWith(`${item.base}-terang.html`);
      const isCurrentGelap = currentPath.endsWith(`${item.base}-gelap.html`);
      bodyHtml += `
        <div class="demo-row">
          <div class="demo-row-info" title="${item.name}">
            <span>${item.name}</span>
          </div>
          <div class="demo-seg-wrap">
            <a href="${item.base}-terang.html" class="demo-seg-btn ${isCurrentTerang ? 'is-active-terang' : ''}">
              <svg width="11" height="11" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><circle cx="12" cy="12" r="5"></circle><line x1="12" y1="1" x2="12" y2="3"></line><line x1="12" y1="21" x2="12" y2="23"></line><line x1="4.22" y1="4.22" x2="5.64" y2="5.64"></line><line x1="18.36" y1="18.36" x2="19.78" y2="19.78"></line><line x1="1" y1="12" x2="3" y2="12"></line><line x1="21" y1="12" x2="23" y2="12"></line><line x1="4.22" y1="19.78" x2="5.64" y2="18.36"></line><line x1="18.36" y1="5.64" x2="19.78" y2="4.22"></line></svg>
              <span>Terang</span>
            </a>
            <a href="${item.base}-gelap.html" class="demo-seg-btn ${isCurrentGelap ? 'is-active-gelap' : ''}">
              <svg width="11" height="11" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M21 12.79A9 9 0 1 1 11.21 3 7 7 0 0 0 21 12.79z"></path></svg>
              <span>Gelap</span>
            </a>
          </div>
        </div>
      `;
    });
    bodyHtml += `</div>`;
  });

  panel.innerHTML = `
    <div class="demo-panel-header">
      <div class="demo-header-title">
        <span class="demo-badge-brand">Olimpix AI</span>
        <h4>Katalog 20 Layar Demo</h4>
      </div>
      <button type="button" id="demo-panel-close" class="demo-close-btn" title="Tutup Menu">
        <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round"><line x1="18" y1="6" x2="6" y2="18"></line><line x1="6" y1="6" x2="18" y2="18"></line></svg>
      </button>
    </div>
    <div class="demo-panel-body">
      ${bodyHtml}
    </div>
  `;

  document.body.appendChild(trigger);
  document.body.appendChild(panel);

  // Toggle logic
  trigger.addEventListener('click', (e) => {
    e.stopPropagation();
    playSoftClick();
    panel.classList.toggle('active');
  });

  const closeBtn = document.getElementById('demo-panel-close');
  if (closeBtn) {
    closeBtn.addEventListener('click', (e) => {
      e.stopPropagation();
      playSoftClick();
      panel.classList.remove('active');
    });
  }

  // Click outside to close
  document.addEventListener('click', (e) => {
    if (!panel.contains(e.target) && !trigger.contains(e.target) && panel.classList.contains('active')) {
      panel.classList.remove('active');
    }
  });
}

// Early Learner interactive setup
function setupEarlyLearnerTK() {
  const bacakanBtn = Array.from(document.querySelectorAll('button, a')).find(b => {
    const txt = b.textContent.toLowerCase();
    return txt.includes('bacakan') || txt.includes('suara');
  });

  if (bacakanBtn) {
    bacakanBtn.classList.add('early-learner-speaker');
    bacakanBtn.addEventListener('click', (e) => {
      e.preventDefault();
      e.stopPropagation();
      playChime();
      bacakanBtn.classList.add('speaking-pulse');
      if ('speechSynthesis' in window) {
        window.speechSynthesis.cancel();
        const utter = new SpeechSynthesisUtterance('Ayo cari menara yang paling tinggi ya!');
        utter.lang = 'id-ID';
        utter.onend = () => bacakanBtn.classList.remove('speaking-pulse');
        window.speechSynthesis.speak(utter);
      }
    });
  }

  const cards = document.querySelectorAll('.grid > div.cursor-pointer, .grid > div[class*="rounded"]');
  cards.forEach(card => {
    card.addEventListener('click', () => {
      playChime();
      cards.forEach(c => {
        c.classList.remove('ring-2', 'ring-[#059669]', 'bg-[#ECFDF5]');
        const star = c.querySelector('.star-badge');
        if (star) star.remove();
      });
      card.classList.add('ring-2', 'ring-[#059669]', 'bg-[#ECFDF5]');
    });
  });
}

// Smooth scroll with fixed navbar offset & active state sync
function setupLandingNavAndScroll() {
  const isDark = document.documentElement.classList.contains('dark') || document.body.classList.contains('bg-[#071324]');
  const activeClasses = isDark
    ? ['bg-[#D4A747]/[0.12]', 'text-[#D4A747]', 'font-bold']
    : ['bg-[#0B1E3A]/[0.08]', 'text-[#0B1E3A]', 'font-bold'];
  const inactiveClasses = isDark
    ? ['text-[#CBD5E1]', 'hover:text-white', 'font-medium']
    : ['text-[#334155]', 'hover:text-[#0B1E3A]', 'font-medium'];

  const navLinks = document.querySelectorAll('header nav a[href^="#"]');

  function setActiveNavLink(targetHash) {
    if (!targetHash) return;
    navLinks.forEach(link => {
      const href = link.getAttribute('href');
      if (href === targetHash) {
        link.classList.remove(...inactiveClasses);
        link.classList.add(...activeClasses);
        link.setAttribute('aria-current', 'page');
      } else {
        link.classList.remove(...activeClasses);
        link.classList.add(...inactiveClasses);
        link.removeAttribute('aria-current');
      }
    });
  }

  // Intercept click on anchor links
  document.querySelectorAll('a[href^="#"]').forEach(anchor => {
    anchor.addEventListener('click', function (e) {
      const hash = this.getAttribute('href');
      if (!hash || hash === '#') return;
      const targetId = hash.slice(1);
      const targetEl = document.getElementById(targetId);
      if (targetEl) {
        e.preventDefault();
        targetEl.scrollIntoView({ behavior: 'smooth', block: 'start' });
        if (history.pushState) {
          history.pushState(null, null, hash);
        } else {
          window.location.hash = hash;
        }
        setActiveNavLink(hash);
      }
    });
  });

  // Handle direct hash on page load
  if (window.location.hash) {
    setActiveNavLink(window.location.hash);
  }

  // ScrollSpy to update active nav link while scrolling
  if (navLinks.length > 0) {
    const sections = Array.from(navLinks)
      .map(link => {
        const id = link.getAttribute('href').slice(1);
        return document.getElementById(id);
      })
      .filter(Boolean);

    window.addEventListener('scroll', () => {
      const scrollPos = window.pageYOffset + 120;
      let currentSectionId = null;

      sections.forEach(sec => {
        if (sec.offsetTop <= scrollPos) {
          currentSectionId = sec.id;
        }
      });

      if (currentSectionId) {
        setActiveNavLink('#' + currentSectionId);
      }
    }, { passive: true });
  }
}

// Initialize on DOMContentLoaded
document.addEventListener('DOMContentLoaded', () => {
  setupGlobalClickSounds();
  setupLiveTimer();
  setupDraggableHeroHUD();
  setupScreensShowcaseDock();
  setupLandingNavAndScroll();

  const path = window.location.pathname.toLowerCase();
  if (path.includes('tk') || path.includes('early-learner')) {
    setupEarlyLearnerTK();
  }
});


// Global Theme Switcher Helper for 3-Mode [ Terang | Gelap | Sistem ]
function setMedalisTheme(mode) {
  try {
    localStorage.setItem('medalis_preferred_theme', mode);
  } catch (e) {}
}

function applySystemTheme(prefix) {
  try {
    localStorage.setItem('medalis_preferred_theme', 'system');
  } catch (e) {}
  const prefersDark = window.matchMedia && window.matchMedia('(prefers-color-scheme: dark)').matches;
  const target = prefersDark ? prefix + '-gelap.html' : prefix + '-terang.html';
  if (!window.location.pathname.endsWith(target)) {
    window.location.href = target;
  }
}

// Highlight System button if preferred theme is system
document.addEventListener('DOMContentLoaded', function() {
  try {
    const pref = localStorage.getItem('medalis_preferred_theme');
    const sysBtn = document.getElementById('theme-system-btn');
    if (pref === 'system' && sysBtn) {
      const isDark = document.documentElement.classList.contains('dark') || window.location.pathname.includes('-gelap');
      if (isDark) {
        sysBtn.className = 'flex items-center gap-1 px-2.5 py-1 rounded-full bg-[#D4A747] text-[#0B1E3A] font-bold shadow-sm transition-all';
        const gelapBtn = sysBtn.previousElementSibling;
        if (gelapBtn) gelapBtn.className = 'flex items-center gap-1 px-2.5 py-1 rounded-full text-[#94A3B8] hover:text-white transition-all';
      } else {
        sysBtn.className = 'flex items-center gap-1 px-2.5 py-1 rounded-full bg-[#0B1E3A] text-white font-bold shadow-sm transition-all';
        const terangBtn = sysBtn.previousElementSibling ? sysBtn.previousElementSibling.previousElementSibling : null;
        if (terangBtn) terangBtn.className = 'flex items-center gap-1 px-2.5 py-1 rounded-full text-[#64748B] hover:text-[#0B1E3A] transition-all';
      }
    }
  } catch (e) {}
});
