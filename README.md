# DECCAN CANVAS 🌐

> **The Definitive Interactive Cartography of Hyderabad’s Creative Underground.**  
> Artisan Roasteries &bull; Design & Architecture Studios &bull; Haute Ateliers &bull; Contemporary Art Galleries &bull; Cultural Heritage Institutions &bull; Lakefront Retreats.

![Deccan Canvas](data:image/svg+xml,<svg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 24 24' fill='%230DA687'><polygon points='12 2 2 7 12 12 22 7 12 2'/><polyline points='2 17 12 22 22 17'/><polyline points='2 12 12 17 22 12'/></svg>)

---

## 🧭 The Vision

Hyderabad is experiencing an explosive creative renaissance. Beyond the IT campuses and historic monuments lies a thriving ecosystem of independent single-estate roasteries, avant-garde couture ateliers, ceramic labs, biophilic design practices, and 400-year-old culinary and scent institutions.

**Deccan Canvas** is an interactive, private-access cartographic intelligence platform mapping this ecosystem with exhaustive contact dossiers, direct founder communication channels, and an hourly live social radar feed.

---

## ✨ Core Platform Capabilities

### 1. 🗺️ Dark Velvet Cartography Engine
- Custom dark vector cartography built with CartoDB Dark Matter base tiles.
- Glowing category radar pins with animated SVG glyphs and beacon waves:
  - ☕ **Artisan Cafes & Roasteries** (Nordic Alpine Emerald `#0DA687`)
  - 🏛️ **Heritage Icons & Historic Scents** (Nizam Honey Ochre `#F59E1A`)
  - 📐 **Design Studios & Architecture** (Electric Violet `#8B5CF6`)
  - 🖼️ **Contemporary Art Galleries** (Deccan Cyan `#06B6D4`)
  - 👗 **Haute Ateliers & Fashion Brands** (Rose Atelier `#F43F5E`)
  - ⚡ **Creative Labs & Ceramic Maker Spaces** (Studio Emerald `#10B981`)
- **Neighborhood Jump Bar**: Instant camera flights across:
  - Jubilee Hills & Banjara Hills
  - Madhapur, Hitec City & Kondapur
  - Gachibowli & Financial District
  - Begumpet & Somajiguda
  - Sainikpuri & Secunderabad
  - Old City, Charminar & Musi River Heritage
  - Gandipet & Kokapet Lakefront

### 2. 📇 Deep Contact Dossier Drawer
For every single mapped venue, Deccan Canvas provides an exhaustive, verified dossier:
- **Primary Person of Contact & Role** (e.g., *Nishant Sinha — Founder & Master Roaster*, *Sanjay Garg — Textile Designer*, *Sahil Taneja — Master Pastry Chef*).
- **Direct 1-Click Triggers**:
  - 💬 **WhatsApp Direct**: Opens pre-composed WhatsApp chat with the founder/manager.
  - 📞 **Direct Call**: One-tap phone connection.
  - ✉️ **Direct Email**: Pre-populated subject line inquiry.
  - 📸 **Instagram Profile**: Verified handle and link.
- **Utility Actions**:
  - 💾 **Save vCard (.vcf)**: Browser generates and downloads an authentic contact card with full metadata.
  - 📋 **Copy All Details**: Formatted contact block copied to clipboard.
- **The Space & Ethos**: Architectural and creative narrative.
- **Insider Tip**: Secret order, preferred table, or optimal visit timing.
- **Navigation**: 1-click directions in **Apple Maps** and **Google Maps**.
- **Amenities**: Wi-Fi speed, power outlets, dog-friendly status, valet parking.

### 3. 📡 Live Radar & Hourly Dynamic Ingestion
- **Automated Hourly Ingestion**: `scripts/update_feed.py` pulls from live Google News RSS, event listings, and social drops.
- **Live Status Ticker**: Real-time ticker in top navigation indicating drops today and recency.
- **Slide-Over Feed**: Shows live drops, weekend popups, secret menu tastings, exhibition vernissages, and design talks.
- **Direct Venue Linking**: Clicking any radar drop immediately flies to the venue on the map and opens its dossier.

### 4. 🔒 Private Member Authentication Gate & Curator Studio
- **Atmospheric Lockscreen**: Bespoke dark velvet modal with topographic contours.
- **Role-Based Access**:
  - **Member Access**:
    - Username: `member` &bull; Password: `deccan2026`
    - Or Instant Passkey: `HYD-CREATIVE-2026`
  - **Curator Mode**:
    - Username: `curator` &bull; Password: `charminar99`
    - Unlocks the **Curator Studio** to map new venues on the fly, broadcast live drops to the radar feed, and export JSON backups.

---

## 🚀 Running Locally

```bash
# Clone the repository
git clone https://github.com/Yprnv7/hyderabad-creative-map.git
cd hyderabad-creative-map

# Serve with any static web server (e.g. Python)
python3 -m http.server 8080

# Open in browser:
# http://localhost:8080
```

### Trigger Hourly Dynamic Radar Ingestion Manually
```bash
python3 scripts/update_feed.py
```

---

## 📄 License

MIT License. Designed with craft for Hyderabad's creative community.
