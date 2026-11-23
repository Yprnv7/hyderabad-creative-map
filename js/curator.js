/* ==========================================================================
   DECCAN CANVAS — Curator Studio Manager
   Add Places, Broadcast Live Drops, Export Database
   ========================================================================== */

const CuratorStudio = (() => {
  let modalBackdrop = null;

  function init() {
    modalBackdrop = document.getElementById('curator-modal');
    const toggleBtn = document.getElementById('curator-toggle-btn');
    const closeBtn = document.getElementById('curator-close-btn');

    if (toggleBtn) {
      toggleBtn.addEventListener('click', show);
    }
    if (closeBtn) {
      closeBtn.addEventListener('click', hide);
    }

    // Tab switching inside Curator Modal
    document.querySelectorAll('.curator-tab-btn').forEach(btn => {
      btn.addEventListener('click', () => {
        document.querySelectorAll('.curator-tab-btn').forEach(b => b.classList.remove('active'));
        document.querySelectorAll('.curator-tab-content').forEach(c => c.style.display = 'none');
        btn.classList.add('active');
        const tabId = btn.getAttribute('data-tab');
        const content = document.getElementById(tabId);
        if (content) content.style.display = 'flex';
      });
    });

    // Populate venue dropdown for live drop
    populateVenueDropdown();

    // Form: Add Place
    const addPlaceForm = document.getElementById('curator-add-place-form');
    if (addPlaceForm) {
      addPlaceForm.addEventListener('submit', handleAddPlace);
    }

    // Form: Broadcast Drop
    const broadcastForm = document.getElementById('curator-broadcast-form');
    if (broadcastForm) {
      broadcastForm.addEventListener('submit', handleBroadcastDrop);
    }

    // Export DB button
    const exportBtn = document.getElementById('curator-export-db-btn');
    if (exportBtn) {
      exportBtn.addEventListener('click', exportDatabase);
    }
  }

  function populateVenueDropdown() {
    const select = document.getElementById('drop-venue-select');
    if (!select || !window.MapEngine) return;

    const places = window.MapEngine.getAllPlaces();
    select.innerHTML = places.map(p => `<option value="${p.id}">${p.name} [${p.neighborhood}]</option>`).join('');
  }

  function handleAddPlace(e) {
    e.preventDefault();
    const name = document.getElementById('new-place-name').value.trim();
    const tagline = document.getElementById('new-place-tagline').value.trim();
    const category = document.getElementById('new-place-category').value;
    const categoryLabel = document.getElementById('new-place-category').selectedOptions[0].text;
    const neighborhood = document.getElementById('new-place-neighborhood').value;
    const zone = document.getElementById('new-place-zone').value;
    const address = document.getElementById('new-place-address').value.trim();
    const lat = parseFloat(document.getElementById('new-place-lat').value);
    const lng = parseFloat(document.getElementById('new-place-lng').value);
    const primaryPerson = document.getElementById('new-place-person').value.trim();
    const primaryRole = document.getElementById('new-place-role').value.trim();
    const phone = document.getElementById('new-place-phone').value.trim();
    const email = document.getElementById('new-place-email').value.trim();
    const insta = document.getElementById('new-place-insta').value.trim();
    const website = document.getElementById('new-place-website').value.trim();
    const vibeInput = document.getElementById('new-place-vibes').value.trim();
    const about = document.getElementById('new-place-about').value.trim();
    const tip = document.getElementById('new-place-tip').value.trim();

    if (!name || isNaN(lat) || isNaN(lng)) {
      alert('Please fill in place name and valid coordinates.');
      return;
    }

    const id = name.toLowerCase().replace(/[^a-z0-9]+/g, '-') + '-' + Math.floor(Math.random() * 1000);

    const newPlace = {
      id,
      name,
      tagline: tagline || 'Creative establishment in Hyderabad.',
      category,
      category_label: categoryLabel,
      neighborhood,
      zone,
      address,
      coordinates: { lat, lng },
      vibe_tags: vibeInput ? vibeInput.split(',').map(s => s.trim()) : ['Creative Hub', 'Hyderabad'],
      price_tier: '₹₹',
      hours: '09:00 AM – 10:30 PM',
      peak_creative_hours: '04:00 PM – 07:30 PM',
      hiring_status: 'Open for Collabs',
      contacts: {
        primary_person: primaryPerson || name,
        primary_role: primaryRole || 'Founder',
        phone: phone || '+91 91212 90045',
        whatsapp: phone ? phone.replace(/[^0-9]/g, '') : '919121290045',
        email: email || 'hello@deccancanvas.in',
        instagram: insta || '@hyderabadcreative',
        instagram_url: insta ? `https://instagram.com/${insta.replace('@', '')}` : '#',
        website: website || 'https://deccancanvas.in'
      },
      dossier: {
        about: about || 'Curated entry added via Deccan Canvas Curator Studio.',
        insider_tip: tip || 'Explore during evening creative hours.',
        amenities: ['Wi-Fi', 'Creative Focus']
      },
      latest_drop: {
        timestamp: 'Just now',
        type: 'Curator Entry',
        title: 'Mapped on Deccan Canvas',
        snippet: 'Newly verified creative establishment in Hyderabad.'
      }
    };

    if (window.MapEngine) {
      window.MapEngine.addPlace(newPlace);
    }

    hide();
    populateVenueDropdown();
    alert(`"${name}" has been mapped and added to Deccan Canvas!`);
  }

  function handleBroadcastDrop(e) {
    e.preventDefault();
    const venueId = document.getElementById('drop-venue-select').value;
    const places = window.MapEngine ? window.MapEngine.getAllPlaces() : [];
    const venue = places.find(p => p.id === venueId);

    const headline = document.getElementById('drop-headline').value.trim();
    const body = document.getElementById('drop-body').value.trim();
    const badge = document.getElementById('drop-badge').value;
    const source = document.getElementById('drop-source').value;

    if (!headline || !body) {
      alert('Please enter headline and body for the drop.');
      return;
    }

    const drop = {
      id: `up-live-${Date.now()}`,
      timestamp: 'Just now',
      iso_time: new Date().toISOString(),
      venue_id: venueId,
      venue_name: venue ? venue.name : 'Deccan Creative Venue',
      neighborhood: venue ? venue.neighborhood : 'Hyderabad',
      category: venue ? venue.category : 'cafe',
      source,
      author: venue ? venue.contacts.primary_person : 'Curator Studio',
      badge,
      headline,
      body,
      link: venue ? venue.contacts.website : '#',
      rsvp_contact: venue ? venue.contacts.phone : '',
      verified: true
    };

    if (window.RadarManager) {
      window.RadarManager.broadcastDrop(drop);
      window.RadarManager.show();
    }

    hide();
  }

  function exportDatabase() {
    const places = window.MapEngine ? window.MapEngine.getAllPlaces() : [];
    const blob = new Blob([JSON.stringify(places, null, 2)], { type: 'application/json' });
    const url = URL.createObjectURL(blob);
    const a = document.createElement('a');
    a.href = url;
    a.download = `deccan_canvas_hyderabad_places_${Date.now()}.json`;
    document.body.appendChild(a);
    a.click();
    document.body.removeChild(a);
    URL.revokeObjectURL(url);
  }

  function show() {
    if (modalBackdrop) modalBackdrop.classList.add('open');
    populateVenueDropdown();
  }

  function hide() {
    if (modalBackdrop) modalBackdrop.classList.remove('open');
  }

  return {
    init,
    show,
    hide
  };
})();

window.CuratorStudio = CuratorStudio;
