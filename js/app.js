/* ==========================================================================
   DECCAN CANVAS — App Main Entry Point
   Initializes Auth, Map Engine, Dossier Drawer, Radar, and Curator Studio
   ========================================================================== */

document.addEventListener('DOMContentLoaded', () => {
  let isMapInitialized = false;

  async function bootstrapApp(session) {
    if (isMapInitialized) return;
    isMapInitialized = true;

    try {
      // 1. Fetch Places
      const res = await fetch(`data/places.json?t=${Date.now()}`);
      if (!res.ok) throw new Error('Could not fetch data/places.json');
      const places = await res.json();

      // 2. Initialize Map Engine
      window.MapEngine.init(places);

      // 3. Initialize Dossier
      window.DossierManager.init();

      // 4. Initialize Radar
      window.RadarManager.init();

      // 5. Initialize Curator Studio
      window.CuratorStudio.init();

      console.log(`Deccan Canvas successfully initialized with ${places.length} mapped locations! Logged in as: ${session.role}`);
    } catch (e) {
      console.error('Fatal initialization error:', e);
    }
  }

  // Bind Auth Gate
  window.AuthManager.initUI((session) => {
    bootstrapApp(session);
  });

  // Global Keyboard Shortcuts
  document.addEventListener('keydown', (e) => {
    // Focus search on '/'
    if (e.key === '/' && document.activeElement.tagName !== 'INPUT' && document.activeElement.tagName !== 'TEXTAREA') {
      e.preventDefault();
      const search = document.getElementById('search-input');
      if (search) search.focus();
    }
    // Toggle radar on 'r'
    if ((e.key === 'r' || e.key === 'R') && document.activeElement.tagName !== 'INPUT' && document.activeElement.tagName !== 'TEXTAREA') {
      if (window.RadarManager) window.RadarManager.toggle();
    }
  });
});
