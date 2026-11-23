/* ==========================================================================
   DECCAN CANVAS — Map Engine & Custom Cartography
   Leaflet Dark Matter Canvas, Glowing SVG Radar Nodes & Spring Navigation
   ========================================================================== */

const MapEngine = (() => {
  let map = null;
  let markersLayer = null;
  let allPlaces = [];
  let activePlaceId = null;
  let activeFilter = 'all';
  let activeZone = 'all';
  let searchQuery = '';

  // Hyderabad Geographic Presets
  const ZONE_PRESETS = {
    'all': { coords: [17.4150, 78.4250], zoom: 12 },
    'jubilee-banjara': { coords: [17.4300, 78.4200], zoom: 14 },
    'madhapur-hitec': { coords: [17.4450, 78.3840], zoom: 14 },
    'gachibowli-financial': { coords: [17.4300, 78.3520], zoom: 13.5 },
    'begumpet-central': { coords: [17.4450, 78.4650], zoom: 14.5 },
    'secunderabad-sainikpuri': { coords: [17.4870, 78.5430], zoom: 14 },
    'old-city-charminar': { coords: [17.3630, 78.4740], zoom: 15 },
    'gandipet-lakefront': { coords: [17.3850, 78.3050], zoom: 13.5 }
  };

  // Category SVGs
  const CATEGORY_SVGS = {
    cafe: `<svg class="pin-icon-svg" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M18 8h1a4 4 0 0 1 0 8h-1"></path><path d="M2 8h16v9a4 4 0 0 1-4 4H6a4 4 0 0 1-4-4V8z"></path><line x1="6" y1="1" x2="6" y2="4"></line><line x1="10" y1="1" x2="10" y2="4"></line><line x1="14" y1="1" x2="14" y2="4"></line></svg>`,
    heritage_icon: `<svg class="pin-icon-svg" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M3 21h18"></path><path d="M5 21V7l7-4 7 4v14"></path><path d="M9 10a3 3 0 0 1 6 0v11H9V10z"></path></svg>`,
    design_studio: `<svg class="pin-icon-svg" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><circle cx="12" cy="12" r="10"></circle><polygon points="16.24 7.76 14.12 14.12 7.76 16.24 9.88 9.88 16.24 7.76"></polygon></svg>`,
    art_culture: `<svg class="pin-icon-svg" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><rect x="3" y="3" width="18" height="18" rx="2"></rect><circle cx="8.5" cy="8.5" r="1.5"></circle><polyline points="21 15 16 10 5 21"></polyline></svg>`,
    brand_fashion: `<svg class="pin-icon-svg" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><circle cx="6" cy="6" r="3"></circle><circle cx="6" cy="18" r="3"></circle><line x1="20" y1="4" x2="8.12" y2="15.88"></line><line x1="14.47" y1="14.48" x2="20" y2="20"></line><line x1="8.12" y1="8.12" x2="12" y2="12"></line></svg>`,
    coworking_maker: `<svg class="pin-icon-svg" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><polygon points="13 2 3 14 12 14 11 22 21 10 12 10 13 2"></polygon></svg>`
  };

  function init(placesData) {
    allPlaces = placesData;

    // Initialize Map with custom coordinates & options
    map = L.map('map', {
      center: ZONE_PRESETS.all.coords,
      zoom: ZONE_PRESETS.all.zoom,
      minZoom: 10,
      maxZoom: 18,
      zoomControl: true
    });

    // Dark Matter Tiles
    L.tileLayer('https://{s}.basemaps.cartocdn.com/dark_all/{z}/{x}/{y}{r}.png', {
      attribution: '&copy; <a href="https://carto.com/">CARTO</a> &copy; <a href="https://openstreetmap.org">OSM</a> | Deccan Canvas Hyderabad',
      subdomains: 'abcd',
      maxZoom: 19
    }).addTo(map);

    markersLayer = L.layerGroup().addTo(map);

    renderMarkers();
    bindEvents();
  }

  function renderMarkers() {
    markersLayer.clearLayers();

    const filtered = allPlaces.filter(place => {
      // Category filter
      if (activeFilter !== 'all' && place.category !== activeFilter) return false;

      // Zone filter
      if (activeZone !== 'all' && place.zone !== activeZone) return false;

      // Search query
      if (searchQuery) {
        const q = searchQuery.toLowerCase();
        const matchName = place.name.toLowerCase().includes(q);
        const matchNeigh = place.neighborhood.toLowerCase().includes(q);
        const matchVibe = place.vibe_tags.some(v => v.toLowerCase().includes(q));
        const matchContact = (place.contacts.primary_person || '').toLowerCase().includes(q);
        const matchTagline = (place.tagline || '').toLowerCase().includes(q);
        if (!matchName && !matchNeigh && !matchVibe && !matchContact && !matchTagline) {
          return false;
        }
      }

      return true;
    });

    filtered.forEach(place => {
      const svgIcon = CATEGORY_SVGS[place.category] || CATEGORY_SVGS.cafe;
      const isActive = place.id === activePlaceId;

      const markerHtml = `
        <div class="pin-bubble ${place.category} ${isActive ? 'active' : ''}" data-id="${place.id}">
          <div class="pin-beacon"></div>
          ${svgIcon}
        </div>
      `;

      const customIcon = L.divIcon({
        html: markerHtml,
        className: 'custom-map-pin',
        iconSize: [40, 40],
        iconAnchor: [20, 20]
      });

      const marker = L.marker([place.coordinates.lat, place.coordinates.lng], { icon: customIcon });

      // Tooltip
      const tooltipContent = `
        <div class="custom-pin-tooltip">
          <div class="tooltip-title">${place.name}</div>
          <div class="tooltip-sub">${place.neighborhood} · ${place.category_label}</div>
        </div>
      `;
      marker.bindTooltip(tooltipContent, {
        direction: 'top',
        offset: [0, -14],
        opacity: 1
      });

      // Click opens Dossier
      marker.on('click', () => {
        selectPlace(place.id, true);
      });

      markersLayer.addLayer(marker);
    });

    updateCounters(filtered.length);
  }

  function selectPlace(placeId, shouldFly = false) {
    activePlaceId = placeId;
    const place = allPlaces.find(p => p.id === placeId);
    if (!place) return;

    // Re-render markers to update active styling
    renderMarkers();

    // Fly camera smoothly to location
    if (shouldFly && map) {
      map.flyTo([place.coordinates.lat, place.coordinates.lng], 15.5, {
        duration: 1.2,
        easeLinearity: 0.25
      });
    }

    // Open Dossier Drawer
    if (window.DossierManager) {
      window.DossierManager.show(place);
    }
  }

  function setCategoryFilter(category) {
    activeFilter = category;
    renderMarkers();
  }

  function setZoneFilter(zoneKey) {
    activeZone = zoneKey;
    const preset = ZONE_PRESETS[zoneKey] || ZONE_PRESETS.all;
    if (map) {
      map.flyTo(preset.coords, preset.zoom, {
        duration: 1.4,
        easeLinearity: 0.25
      });
    }
    renderMarkers();
  }

  function setSearch(query) {
    searchQuery = (query || '').trim();
    renderMarkers();
  }

  function updateCounters(visibleCount) {
    const counterEl = document.getElementById('visible-count');
    if (counterEl) {
      counterEl.textContent = `${visibleCount} of ${allPlaces.length} mapped`;
    }
  }

  function bindEvents() {
    // Area Pills
    document.querySelectorAll('.area-pill').forEach(pill => {
      pill.addEventListener('click', (e) => {
        document.querySelectorAll('.area-pill').forEach(p => p.classList.remove('active'));
        pill.classList.add('active');
        const zone = pill.getAttribute('data-zone');
        setZoneFilter(zone);
      });
    });

    // Category Pills
    document.querySelectorAll('.cat-pill').forEach(pill => {
      pill.addEventListener('click', (e) => {
        document.querySelectorAll('.cat-pill').forEach(p => p.classList.remove('active'));
        pill.classList.add('active');
        const cat = pill.getAttribute('data-cat');
        setCategoryFilter(cat);
      });
    });

    // Search Input
    const searchInput = document.getElementById('search-input');
    const searchClear = document.getElementById('search-clear');

    if (searchInput) {
      searchInput.addEventListener('input', (e) => {
        const val = e.target.value;
        setSearch(val);
        if (searchClear) {
          if (val.length > 0) searchClear.classList.add('active');
          else searchClear.classList.remove('active');
        }
      });
    }

    if (searchClear) {
      searchClear.addEventListener('click', () => {
        if (searchInput) {
          searchInput.value = '';
          setSearch('');
          searchClear.classList.remove('active');
          searchInput.focus();
        }
      });
    }
  }

  function addPlace(newPlace) {
    allPlaces.push(newPlace);
    renderMarkers();
    selectPlace(newPlace.id, true);
  }

  return {
    init,
    selectPlace,
    setCategoryFilter,
    setZoneFilter,
    setSearch,
    addPlace,
    getAllPlaces: () => allPlaces
  };
})();

window.MapEngine = MapEngine;
