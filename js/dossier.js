/* ==========================================================================
   DECCAN CANVAS — Detail Modal & Contact Dossier
   Styling: Exactly matching https://lagataperduda.com/en/mapa/ modal-bg
   Radial Color Mesh Glow, 1-Click WhatsApp/Call, vCard & Google Maps Embed
   ========================================================================== */

const DossierModal = (() => {
  let modalEl = null;
  let currentPlace = null;

  const COLOR_MAP = {
    cafe: 'green',
    heritage_icon: 'yellow',
    design_studio: 'orange',
    art_culture: 'blue',
    brand_fashion: 'pink',
    coworking_maker: 'blue'
  };

  function init() {
    modalEl = document.getElementById('lgp-modal');
    const closeBtn = document.getElementById('lgp-modal-close');

    if (closeBtn) {
      closeBtn.addEventListener('click', hide);
    }

    if (modalEl) {
      modalEl.addEventListener('click', (e) => {
        if (e.target === modalEl) hide();
      });
    }

    document.addEventListener('keydown', (e) => {
      if (e.key === 'Escape') hide();
    });
  }

  function show(place) {
    if (!modalEl) init();
    currentPlace = place;

    const colorName = COLOR_MAP[place.category] || 'green';
    const modalBg = document.getElementById('modal-bg-glow');
    if (modalBg) {
      modalBg.setAttribute('data-color', colorName);
    }

    // Header info
    const catEl = document.getElementById('modal-category');
    if (catEl) {
      catEl.textContent = place.category_label;
      catEl.style.color = `rgb(var(--c-${colorName}))`;
      catEl.style.borderColor = `rgb(var(--c-${colorName}))`;
    }

    document.getElementById('modal-title').textContent = place.name;
    document.getElementById('modal-tagline').textContent = place.tagline;

    // Contact Dossier
    const personName = place.contacts.primary_person || place.name;
    const personRole = place.contacts.primary_role || 'Founder & Director';
    const cleanPhone = (place.contacts.phone || '').replace(/[^0-9+]/g, '');
    const cleanWhatsapp = (place.contacts.whatsapp || cleanPhone).replace(/[^0-9]/g, '');
    const email = place.contacts.email || '';
    const instaHandle = (place.contacts.instagram || '').replace('@', '');
    const instaUrl = place.contacts.instagram_url || `https://instagram.com/${instaHandle}`;

    document.getElementById('modal-person-name').textContent = personName;
    document.getElementById('modal-person-role').textContent = personRole;

    // Buttons
    const waBtn = document.getElementById('modal-btn-whatsapp');
    const callBtn = document.getElementById('modal-btn-call');
    const emailBtn = document.getElementById('modal-btn-email');
    const instaBtn = document.getElementById('modal-btn-instagram');

    if (waBtn) {
      const msg = encodeURIComponent(`Hi ${personName}, discovering ${place.name} on Deccan Canvas Hyderabad. Connecting regarding:`);
      waBtn.href = `https://wa.me/${cleanWhatsapp}?text=${msg}`;
    }

    if (callBtn) {
      callBtn.href = `tel:${cleanPhone}`;
    }

    if (emailBtn) {
      emailBtn.href = `mailto:${email}?subject=${encodeURIComponent(`Deccan Canvas Inquiry: ${place.name}`)}`;
    }

    if (instaBtn) {
      instaBtn.href = instaUrl;
    }

    // Secondary Person
    const secEl = document.getElementById('modal-secondary-person');
    if (secEl) {
      if (place.contacts.secondary_person) {
        secEl.textContent = place.contacts.secondary_person;
        secEl.style.display = 'block';
      } else {
        secEl.style.display = 'none';
      }
    }

    // Copy Contact Details
    const copyBtn = document.getElementById('modal-copy-contact-btn');
    if (copyBtn) {
      copyBtn.onclick = () => copyContact(place);
    }

    // Save vCard
    const vcardBtn = document.getElementById('modal-download-vcard-btn');
    if (vcardBtn) {
      vcardBtn.onclick = () => downloadVCard(place);
    }

    // About Prose & Insider Tip
    document.getElementById('modal-about-text').textContent = place.dossier.about;
    document.getElementById('modal-tip-text').textContent = place.dossier.insider_tip;

    // Meta Grid
    document.getElementById('modal-address').textContent = place.address;
    document.getElementById('modal-hours').textContent = place.hours;
    document.getElementById('modal-peak').textContent = place.peak_creative_hours || 'Afternoon';
    document.getElementById('modal-pricing').textContent = place.price_tier || '₹₹';

    // Google Maps Navigation Deep Links
    const lat = place.coordinates.lat;
    const lng = place.coordinates.lng;
    const gmapsLink = document.getElementById('modal-gmaps-link');
    const amapsLink = document.getElementById('modal-amaps-link');

    if (gmapsLink) {
      gmapsLink.href = `https://www.google.com/maps/search/?api=1&query=${lat},${lng}`;
    }
    if (amapsLink) {
      amapsLink.href = `https://maps.apple.com/?q=${encodeURIComponent(place.name)}&ll=${lat},${lng}`;
    }

    // Google Maps Location Embed Preview
    const embedIframe = document.getElementById('modal-gmaps-iframe');
    if (embedIframe) {
      embedIframe.src = `https://maps.google.com/maps?q=${lat},${lng}&t=m&z=15&output=embed&iwloc=near`;
    }

    // Live Drop in Modal
    const dropCard = document.getElementById('modal-drop-card');
    if (dropCard) {
      if (place.latest_drop) {
        dropCard.style.display = 'block';
        document.getElementById('modal-drop-title').textContent = place.latest_drop.title;
        document.getElementById('modal-drop-snippet').textContent = place.latest_drop.snippet;
      } else {
        dropCard.style.display = 'none';
      }
    }

    modalEl.classList.add('open');
  }

  function hide() {
    if (modalEl) modalEl.classList.remove('open');
    currentPlace = null;
  }

  function copyContact(place) {
    const text = `
${place.name} [${place.category_label}]
Address: ${place.address}
Contact: ${place.contacts.primary_person} (${place.contacts.primary_role})
Phone: ${place.contacts.phone}
WhatsApp: ${place.contacts.whatsapp}
Email: ${place.contacts.email}
Instagram: ${place.contacts.instagram}
Website: ${place.contacts.website}
Hours: ${place.hours}
---
Deccan Canvas · Hyderabad Creative Cartography
    `.trim();

    navigator.clipboard.writeText(text).then(() => {
      const btn = document.getElementById('modal-copy-contact-btn');
      if (btn) {
        const orig = btn.textContent;
        btn.textContent = '✓ COPIED';
        setTimeout(() => { btn.textContent = orig; }, 2000);
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
    hide
  };
})();

window.DossierModal = DossierModal;
