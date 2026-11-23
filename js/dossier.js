/* ==========================================================================
   DECCAN CANVAS — Deep Dossier & Contact Drawer Manager
   Complete Contact Details, 1-Click WhatsApp/Call, vCard Export & Directions
   ========================================================================== */

const DossierManager = (() => {
  let drawerEl = null;
  let currentPlace = null;

  function init() {
    drawerEl = document.getElementById('dossier-drawer');
    const closeBtn = document.getElementById('dossier-close-btn');

    if (closeBtn) {
      closeBtn.addEventListener('click', hide);
    }

    // Escape key closes drawer
    document.addEventListener('keydown', (e) => {
      if (e.key === 'Escape') hide();
    });
  }

  function show(place) {
    if (!drawerEl) init();
    currentPlace = place;

    // Populate drawer elements
    document.getElementById('dossier-category').textContent = place.category_label;
    document.getElementById('dossier-category').className = `category-tag ${place.category}`;
    document.getElementById('dossier-price').textContent = place.price_tier || '₹₹';
    document.getElementById('dossier-status').textContent = place.hiring_status || 'Walk-ins Welcome';
    document.getElementById('dossier-title').textContent = place.name;
    document.getElementById('dossier-tagline').textContent = place.tagline;

    // Person of Contact Meta
    const personName = place.contacts.primary_person || place.name;
    const personRole = place.contacts.primary_role || 'Founder & Director';
    const cleanPhone = (place.contacts.phone || '').replace(/[^0-9+]/g, '');
    const cleanWhatsapp = (place.contacts.whatsapp || cleanPhone).replace(/[^0-9]/g, '');
    const email = place.contacts.email || '';
    const instagram = place.contacts.instagram || '';
    const instagramUrl = place.contacts.instagram_url || `https://instagram.com/${instagram.replace('@', '')}`;
    const website = place.contacts.website || '#';

    // Initials for avatar
    const initials = personName
      .split(' ')
      .slice(0, 2)
      .map(n => n[0])
      .join('')
      .toUpperCase();

    document.getElementById('contact-avatar-text').textContent = initials;
    document.getElementById('contact-person-name').textContent = personName;
    document.getElementById('contact-person-role').textContent = personRole;

    // Contact Action Triggers
    const whatsappBtn = document.getElementById('contact-action-whatsapp');
    const callBtn = document.getElementById('contact-action-call');
    const emailBtn = document.getElementById('contact-action-email');
    const instaBtn = document.getElementById('contact-action-insta');

    if (whatsappBtn) {
      const waMsg = encodeURIComponent(`Hi ${personName}, discovering ${place.name} on Deccan Canvas Hyderabad. Connecting regarding:`);
      whatsappBtn.href = `https://wa.me/${cleanWhatsapp}?text=${waMsg}`;
      whatsappBtn.target = '_blank';
    }

    if (callBtn) {
      callBtn.href = `tel:${cleanPhone}`;
    }

    if (emailBtn) {
      const emailSubject = encodeURIComponent(`Inquiry via Deccan Canvas: ${place.name}`);
      emailBtn.href = `mailto:${email}?subject=${emailSubject}`;
    }

    if (instaBtn) {
      instaBtn.href = instagramUrl;
      instaBtn.target = '_blank';
    }

    // Secondary Person
    const secondaryEl = document.getElementById('contact-secondary-person');
    if (secondaryEl) {
      if (place.contacts.secondary_person) {
        secondaryEl.textContent = place.contacts.secondary_person;
        secondaryEl.parentElement.style.display = 'flex';
      } else {
        secondaryEl.parentElement.style.display = 'none';
      }
    }

    // Copy Contact Details Button
    const copyBtn = document.getElementById('copy-contact-btn');
    if (copyBtn) {
      copyBtn.onclick = () => copyContactToClipboard(place);
    }

    // Export vCard Button
    const vcardBtn = document.getElementById('download-vcard-btn');
    if (vcardBtn) {
      vcardBtn.onclick = () => downloadVCard(place);
    }

    // About Prose
    document.getElementById('dossier-about-text').textContent = place.dossier.about;

    // Insider Tip
    document.getElementById('dossier-tip-text').textContent = place.dossier.insider_tip;

    // Vibe Tags
    const vibeContainer = document.getElementById('dossier-vibe-tags');
    if (vibeContainer) {
      vibeContainer.innerHTML = place.vibe_tags
        .map(tag => `<span class="vibe-tag">#${tag}</span>`)
        .join('');
    }

    // Details Table
    document.getElementById('dossier-address-text').textContent = place.address;
    document.getElementById('dossier-hours-text').textContent = place.hours;
    document.getElementById('dossier-peak-text').textContent = place.peak_creative_hours || 'Afternoon & Sunset';

    // Directions Links (Google & Apple Maps)
    const lat = place.coordinates.lat;
    const lng = place.coordinates.lng;
    const gmapsLink = document.getElementById('directions-google-maps');
    const amapsLink = document.getElementById('directions-apple-maps');

    if (gmapsLink) {
      gmapsLink.href = `https://www.google.com/maps/search/?api=1&query=${lat},${lng}`;
      gmapsLink.target = '_blank';
    }
    if (amapsLink) {
      amapsLink.href = `https://maps.apple.com/?q=${encodeURIComponent(place.name)}&ll=${lat},${lng}`;
      amapsLink.target = '_blank';
    }

    // Amenities
    const amenitiesContainer = document.getElementById('dossier-amenities');
    if (amenitiesContainer && place.dossier.amenities) {
      amenitiesContainer.innerHTML = place.dossier.amenities
        .map(am => `<span class="status-badge">✓ ${am}</span>`)
        .join('');
    }

    // Latest Live Drop
    const dropCard = document.getElementById('dossier-live-drop-card');
    if (dropCard) {
      if (place.latest_drop) {
        dropCard.style.display = 'flex';
        document.getElementById('drop-card-badge').textContent = place.latest_drop.type || 'LIVE DROP';
        document.getElementById('drop-card-time').textContent = place.latest_drop.timestamp || 'Recent';
        document.getElementById('drop-card-title').textContent = place.latest_drop.title;
        document.getElementById('drop-card-snippet').textContent = place.latest_drop.snippet;
      } else {
        dropCard.style.display = 'none';
      }
    }

    // Close Radar if open
    if (window.RadarManager) window.RadarManager.hide();

    // Slide drawer open
    drawerEl.classList.add('open');
  }

  function hide() {
    if (drawerEl) drawerEl.classList.remove('open');
    currentPlace = null;
  }

  function copyContactToClipboard(place) {
    const text = `
${place.name} [${place.category_label}]
Neighborhood: ${place.neighborhood}
Address: ${place.address}
Contact Person: ${place.contacts.primary_person} (${place.contacts.primary_role})
Phone: ${place.contacts.phone}
WhatsApp: ${place.contacts.whatsapp}
Email: ${place.contacts.email}
Instagram: ${place.contacts.instagram}
Website: ${place.contacts.website}
Hours: ${place.hours}
---
Curated on Deccan Canvas · Hyderabad Creative Map
    `.trim();

    navigator.clipboard.writeText(text).then(() => {
      const copyBtn = document.getElementById('copy-contact-btn');
      if (copyBtn) {
        const orig = copyBtn.innerHTML;
        copyBtn.innerHTML = `✓ Copied to Clipboard!`;
        copyBtn.style.color = 'var(--accent-cafe)';
        setTimeout(() => {
          copyBtn.innerHTML = orig;
          copyBtn.style.color = '';
        }, 2200);
      }
    });
  }

  function downloadVCard(place) {
    const person = place.contacts.primary_person || place.name;
    const phone = (place.contacts.phone || '').replace(/[^0-9+]/g, '');
    const email = place.contacts.email || '';
    const website = place.contacts.website || '';
    const address = place.address || '';

    const vcard = `BEGIN:VCARD
VERSION:3.0
FN:${person} - ${place.name}
ORG:${place.name}
TITLE:${place.contacts.primary_role || 'Founder'}
TEL;TYPE=CELL,VOICE:${phone}
EMAIL;TYPE=INTERNET,WORK:${email}
URL:${website}
ADR;TYPE=WORK:;;${address};Hyderabad;;500001;India
NOTE:${place.tagline}
END:VCARD`;

    const blob = new Blob([vcard], { type: 'text/vcard;charset=utf-8;' });
    const url = URL.createObjectURL(blob);
    const a = document.createElement('a');
    a.href = url;
    a.download = `${place.id}.vcf`;
    document.body.appendChild(a);
    a.click();
    document.body.removeChild(a);
    URL.revokeObjectURL(url);
  }

  return {
    init,
    show,
    hide,
    getCurrentPlace: () => currentPlace
  };
})();

window.DossierManager = DossierManager;
