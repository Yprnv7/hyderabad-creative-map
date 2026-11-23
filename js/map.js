/* ==========================================================================
   DECCAN CANVAS — Map Engine
   Styling: Exactly matching https://lagataperduda.com/en/mapa/
   Dual-Engine Architecture: Google Maps API + Dark Matter Fallback
   ========================================================================== */

const MapEngine = (() => {
  let map = null;
  let googleMap = null;
  let markersLayer = null;
  let allPlaces = [];
  let activePlaceId = null;
  let activeCategories = new Set(['cafe', 'heritage_icon', 'design_studio', 'art_culture', 'brand_fashion', 'coworking_maker']);
  let activeZone = 'all';
  let searchQuery = '';
  let currentEngine = 'leaflet'; // 'leaflet' or 'google'
  let googleMarkers = [];

  // Hyderabad Presets
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

  // La Gata Perduda Category Color Map
  const CATEGORY_COLORS = {
    cafe: 'var(--c-green)',
    heritage_icon: 'var(--c-yellow)',
    design_studio: 'var(--c-orange)',
    art_culture: 'var(--c-blue)',
    brand_fashion: 'var(--c-pink)',
    coworking_maker: 'var(--c-purple)'
  };

  // La Gata Perduda Google Maps Dark Style Array
  const GOOGLE_MAPS_DARK_STYLE = [
    { elementType: 'geometry', stylers: [{ color: '#000000' }] },
    { elementType: 'labels.icon', stylers: [{ visibility: 'off' }] },
    { elementType: 'labels.text.fill', stylers: [{ color: '#777777' }] },
    { elementType: 'labels.text.stroke', stylers: [{ color: '#000000' }] },
    { featureType: 'administrative', elementType: 'geometry', stylers: [{ color: '#222222' }] },
    { featureType: 'administrative.country', elementType: 'geometry.stroke', stylers: [{ color: '#333333' }] },
    { featureType: 'poi', stylers: [{ visibility: 'off' }] },
    { featureType: 'road', elementType: 'geometry.fill', stylers: [{ color: '#111111' }] },
    { featureType: 'road', elementType: 'geometry.stroke', stylers: [{ color: '#1a1a1a' }] },
    { featureType: 'road.highway', elementType: 'geometry.fill', stylers: [{ color: '#1c1c1c' }] },
    { featureType: 'transit', stylers: [{ visibility: 'off' }] },
    { featureType: 'water', elementType: 'geometry', stylers: [{ color: '#0a0a0a' }] }
  ];

  function init(placesData) {
    allPlaces = placesData;

    // Check if Google Maps API key is configured
    const gmapsKey = getGoogleMapsApiKey();
    if (gmapsKey) {
      loadGoogleMapsScript(gmapsKey);
    } else {
      initLeafletMap();
    }

    bindFilterEvents();
    renderMarkers();
  }

  function getGoogleMapsApiKey() {
    const urlParams = new URLSearchParams(window.location.search);
    return urlParams.get('gmaps_key') || localStorage.getItem('gmaps_api_key') || '';
  }

  function setGoogleMapsApiKey(key) {
    if (key) {
      localStorage.setItem('gmaps_api_key', key);
      loadGoogleMapsScript(key);
    } else {
      localStorage.removeItem('gmaps_api_key');
      switchToLeaflet();
    }
  }

  function loadGoogleMapsScript(key) {
    if (window.google && window.google.maps) {
      initGoogleMapInstance();
      return;
    }
    const script = document.createElement('script');
    script.src = `https://maps.googleapis.com/maps/api/js?key=${encodeURIComponent(key)}&callback=MapEngine.onGoogleMapsLoaded`;
    script.async = true;
    script.defer = true;
    script.onerror = () => {
      console.warn('Google Maps API script error. Falling back to Dark Matter tiles.');
      initLeafletMap();
    };
    document.head.appendChild(script);
  }

  function onGoogleMapsLoaded() {
    initGoogleMapInstance();
  }

  function initGoogleMapInstance() {
    try {
      const mapEl = document.getElementById('map');
      if (!mapEl) return;
      currentEngine = 'google';

      const center = ZONE_PRESETS.all.coords;
      googleMap = new google.maps.Map(mapEl, {
        center: { lat: center[0], lng: center[1] },
        zoom: ZONE_PRESETS.all.zoom,
        styles: GOOGLE_MAPS_DARK_STYLE,
        disableDefaultUI: true,
        zoomControl: true,
        backgroundColor: '#000000'
      });

      renderMarkers();
      updateEngineBadge();
    } catch (e) {
      console.warn('Could not initialize Google Map, falling back to Leaflet:', e);
      initLeafletMap();
    }
  }

  function initLeafletMap() {
    currentEngine = 'leaflet';
    const mapEl = document.getElementById('map');
    if (!mapEl) return;

    if (map) {
      map.remove();
      map = null;
    }

    map = L.map('map', {
      center: ZONE_PRESETS.all.coords,
      zoom: ZONE_PRESETS.all.zoom,
      minZoom: 10,
      maxZoom: 18,
      zoomControl: true
    });

    // Pure Dark Matter Tiles matching La Gata Perduda aesthetic
    L.tileLayer('https://{s}.basemaps.cartocdn.com/dark_all/{z}/{x}/{y}{r}.png', {
      attribution: '&copy; CARTO &copy; OpenStreetMap | Deccan Canvas',
      subdomains: 'abcd',
      maxZoom: 19
    }).addTo(map);

    markersLayer = L.layerGroup().addTo(map);
    renderMarkers();
    updateEngineBadge();
  }

  function renderMarkers() {
    const filtered = allPlaces.filter(place => {
      // Category filter
      if (!activeCategories.has(place.category)) return false;

      // Zone filter
      if (activeZone !== 'all' && place.zone !== activeZone) return false;

      // Search query
      if (searchQuery) {
        const q = searchQuery.toLowerCase();
        const matchName = place.name.toLowerCase().includes(q);
        const matchNeigh = place.neighborhood.toLowerCase().includes(q);
        const matchVibe = place.vibe_tags.some(v => v.toLowerCase().includes(q));
        const matchContact = (place.contacts.primary_person || '').toLowerCase().includes(q);
        if (!matchName && !matchNeigh && !matchVibe && !matchContact) {
          return false;
        }
      }

      return true;
    });

    if (currentEngine === 'google' && googleMap) {
      renderGoogleMarkers(filtered);
    } else if (map && markersLayer) {
      renderLeafletMarkers(filtered);
    }

    updateCount(filtered.length);
  }

  function renderLeafletMarkers(filtered) {
    markersLayer.clearLayers();

    filtered.forEach(place => {
      const colorVar = CATEGORY_COLORS[place.category] || 'var(--c-green)';
      const isActive = place.id === activePlaceId;

      const markerHtml = `
        <div class="lgp-node ${isActive ? 'active' : ''}" style="--c-node: ${colorVar};" data-id="${place.id}">
          <div class="lgp-node-core"></div>
        </div>
      `;

      const customIcon = L.divIcon({
        html: markerHtml,
        className: 'lgp-pin',
        iconSize: [28, 28],
        iconAnchor: [14, 14]
      });

      const marker = L.marker([place.coordinates.lat, place.coordinates.lng], { icon: customIcon });

      const tooltipHtml = `
        <div class="lgp-tooltip">
          <div class="lgp-tooltip-title">${place.name}</div>
          <div class="lgp-tooltip-sub">${place.neighborhood} &bull; ${place.category_label}</div>
        </div>
      `;
      marker.bindTooltip(tooltipHtml, {
        direction: 'top',
        offset: [0, -10],
        opacity: 1
      });

      marker.on('click', () => {
        selectPlace(place.id, true);
      });

      markersLayer.addLayer(marker);
    });
  }

  function renderGoogleMarkers(filtered) {
    googleMarkers.forEach(m => m.setMap(null));
    googleMarkers = [];

    filtered.forEach(place => {
      const colorVar = CATEGORY_COLORS[place.category] || 'rgb(var(--c-green))';
      const marker = new google.maps.Marker({
        position: { lat: place.coordinates.lat, lng: place.coordinates.lng },
        map: googleMap,
        title: place.name,
        icon: {
          path: google.maps.SymbolPath.CIRCLE,
          scale: 9,
          fillColor: '#000000',
          fillOpacity: 1,
          strokeColor: place.category === 'cafe' ? '#a0c29e' :
                       place.category === 'heritage_icon' ? '#f8d180' :
                       place.category === 'design_studio' ? '#d6772f' :
                       place.category === 'art_culture' ? '#5771ac' :
                       place.category === 'brand_fashion' ? '#ce9494' : '#af82d7',
          strokeWeight: 2.5
        }
      });

      marker.addListener('click', () => {
        selectPlace(place.id, true);
      });

      googleMarkers.push(marker);
    });
  }

  function selectPlace(placeId, shouldFly = false) {
    activePlaceId = placeId;
    const place = allPlaces.find(p => p.id === placeId);
    if (!place) return;

    renderMarkers();

    if (shouldFly) {
      if (currentEngine === 'google' && googleMap) {
        googleMap.panTo({ lat: place.coordinates.lat, lng: place.coordinates.lng });
        googleMap.setZoom(15);
      } else if (map) {
        map.flyTo([place.coordinates.lat, place.coordinates.lng], 15.5, {
          duration: 1.2,
          easeLinearity: 0.25
        });
      }
    }

    if (window.DossierModal) {
      window.DossierModal.show(place);
    }
  }

  function toggleCategory(category) {
    if (activeCategories.has(category)) {
      if (activeCategories.size > 1) {
        activeCategories.delete(category);
      } else {
        // If it's the last one, reset all
        activeCategories = new Set(['cafe', 'heritage_icon', 'design_studio', 'art_culture', 'brand_fashion', 'coworking_maker']);
      }
    } else {
      activeCategories.add(category);
    }
    renderMarkers();
  }

  function setZone(zoneKey) {
    activeZone = zoneKey;
    const preset = ZONE_PRESETS[zoneKey] || ZONE_PRESETS.all;

    if (currentEngine === 'google' && googleMap) {
      googleMap.panTo({ lat: preset.coords[0], lng: preset.coords[1] });
      googleMap.setZoom(preset.zoom);
    } else if (map) {
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

  function updateCount(count) {
    const el = document.getElementById('filters-count-num');
    if (el) el.textContent = `${count} of ${allPlaces.length}`;
  }

  function updateEngineBadge() {
    const badge = document.getElementById('engine-status-badge');
    if (badge) {
      badge.textContent = currentEngine === 'google' ? 'ENGINE: GOOGLE MAPS API' : 'ENGINE: DARK CANVAS';
    }
  }

  function bindFilterEvents() {
    // Checkbox category filters (Exact La Gata Perduda behavior)
    document.querySelectorAll('.filter-item-wrapper input[type="checkbox"]').forEach(input => {
      input.addEventListener('change', (e) => {
        const cat = e.target.getAttribute('data-cat');
        toggleCategory(cat);
      });
    });

    // Zone pills
    document.querySelectorAll('.zone-btn').forEach(btn => {
      btn.addEventListener('click', () => {
        document.querySelectorAll('.zone-btn').forEach(b => b.classList.remove('active'));
        btn.classList.add('active');
        const zone = btn.getAttribute('data-zone');
        setZone(zone);
      });
    });
  }

  return {
    init,
    selectPlace,
    toggleCategory,
    setZone,
    setSearch,
    setGoogleMapsApiKey,
    onGoogleMapsLoaded,
    getAllPlaces: () => allPlaces
  };
})();

window.MapEngine = MapEngine;
