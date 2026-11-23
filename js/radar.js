/* ==========================================================================
   DECCAN CANVAS — Live Radar & Hourly Dynamic Updates Manager
   Real-Time Social Ticker, Ingested Feed Stream & Venue Cross-Linking
   ========================================================================== */

const RadarManager = (() => {
  let drawerEl = null;
  let updatesData = null;
  let refreshTimer = null;

  async function init() {
    drawerEl = document.getElementById('radar-drawer');
    const toggleBtn = document.getElementById('radar-toggle-btn');
    const closeBtn = document.getElementById('radar-close-btn');
    const refreshBtn = document.getElementById('radar-refresh-btn');

    if (toggleBtn) {
      toggleBtn.addEventListener('click', toggle);
    }

    if (closeBtn) {
      closeBtn.addEventListener('click', hide);
    }

    if (refreshBtn) {
      refreshBtn.addEventListener('click', () => {
        refreshBtn.classList.add('spinning');
        fetchUpdates(true).finally(() => {
          setTimeout(() => refreshBtn.classList.remove('spinning'), 600);
        });
      });
    }

    await fetchUpdates();

    // Re-check hourly (every 60 minutes)
    if (refreshTimer) clearInterval(refreshTimer);
    refreshTimer = setInterval(() => {
      fetchUpdates(false);
    }, 60 * 60 * 1000);
  }

  async function fetchUpdates(forceToast = false) {
    try {
      const res = await fetch(`data/updates.json?t=${Date.now()}`);
      if (!res.ok) throw new Error('Failed to load updates.json');
      updatesData = await res.json();
      renderFeed();
      updateTopTicker();
      if (forceToast) showToast('Radar refreshed with latest hourly telemetry!');
    } catch (e) {
      console.warn('Notice: Could not load live data/updates.json, using fallback data.', e);
    }
  }

  function updateTopTicker() {
    const badge = document.getElementById('radar-ticker-text');
    if (!badge || !updatesData) return;

    const total = updatesData.total_active_drops || (updatesData.updates ? updatesData.updates.length : 0);
    badge.textContent = `LIVE RADAR (${total} drops today)`;
  }

  function renderFeed() {
    const feedContainer = document.getElementById('radar-feed-list');
    if (!feedContainer || !updatesData || !updatesData.updates) return;

    feedContainer.innerHTML = updatesData.updates.map(item => {
      const cleanPhone = (item.rsvp_contact || '').replace(/[^0-9+]/g, '');
      const waLink = item.rsvp_contact ? `https://wa.me/${cleanPhone.replace(/[^0-9]/g, '')}` : item.link;

      return `
        <div class="radar-item" data-venue-id="${item.venue_id}">
          <div class="radar-item-top">
            <span class="drop-badge">${item.badge || 'LIVE DROP'}</span>
            <span class="radar-time-tag">${item.timestamp}</span>
          </div>

          <div class="radar-source-tag">
            <svg width="12" height="12" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><circle cx="12" cy="12" r="10"></circle><polygon points="12 6 12 12 16 14"></polygon></svg>
            ${item.source} · ${item.author}
          </div>

          <div class="radar-item-headline">${item.headline}</div>
          <div class="radar-item-body">${item.body}</div>

          <div class="radar-item-footer">
            <span class="radar-venue-link" onclick="event.stopPropagation(); window.MapEngine.selectPlace('${item.venue_id}', true);">
              📍 ${item.venue_name} [${item.neighborhood}]
            </span>
            <a href="${waLink}" target="_blank" class="radar-rsvp-link" onclick="event.stopPropagation();">
              RSVP / Details &rarr;
            </a>
          </div>
        </div>
      `;
    }).join('');

    // Clicking an item flies to venue
    feedContainer.querySelectorAll('.radar-item').forEach(el => {
      el.addEventListener('click', () => {
        const venueId = el.getAttribute('data-venue-id');
        if (venueId && window.MapEngine) {
          window.MapEngine.selectPlace(venueId, true);
        }
      });
    });
  }

  function toggle() {
    if (!drawerEl) return;
    if (drawerEl.classList.contains('open')) {
      hide();
    } else {
      show();
    }
  }

  function show() {
    if (drawerEl) {
      if (window.DossierManager) window.DossierManager.hide();
      drawerEl.classList.add('open');
      const toggleBtn = document.getElementById('radar-toggle-btn');
      if (toggleBtn) toggleBtn.classList.add('active');
    }
  }

  function hide() {
    if (drawerEl) {
      drawerEl.classList.remove('open');
      const toggleBtn = document.getElementById('radar-toggle-btn');
      if (toggleBtn) toggleBtn.classList.remove('active');
    }
  }

  function showToast(msg) {
    let toast = document.getElementById('radar-toast');
    if (!toast) {
      toast = document.createElement('div');
      toast.id = 'radar-toast';
      toast.style.cssText = `
        position: fixed;
        bottom: 24px;
        left: 50%;
        transform: translateX(-50%);
        background: var(--bg-surface);
        border: 1px solid var(--accent-cafe);
        color: var(--text-primary);
        font-size: 13px;
        font-weight: 600;
        padding: 10px 18px;
        border-radius: 999px;
        box-shadow: var(--shadow-lg);
        z-index: 9999;
        transition: opacity 0.3s ease;
      `;
      document.body.appendChild(toast);
    }
    toast.textContent = msg;
    toast.style.opacity = '1';
    setTimeout(() => {
      toast.style.opacity = '0';
    }, 2800);
  }

  function broadcastDrop(drop) {
    if (!updatesData) updatesData = { updates: [] };
    updatesData.updates.unshift(drop);
    renderFeed();
    updateTopTicker();
    showToast(`New live drop broadcasted: "${drop.headline}"`);
  }

  return {
    init,
    toggle,
    show,
    hide,
    broadcastDrop,
    fetchUpdates
  };
})();

window.RadarManager = RadarManager;
