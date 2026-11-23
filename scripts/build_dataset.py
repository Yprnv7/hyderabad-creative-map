import json

places = [
    # --- JUBILEE HILLS & BANJARA HILLS ---
    {
        "id": "roastery-coffee-house-jubilee",
        "name": "Roastery Coffee House",
        "tagline": "Pioneering Indian single-origin estate coffee in a cascading brick heritage bungalow.",
        "category": "cafe",
        "category_label": "Artisan Roastery & Cafe",
        "neighborhood": "Jubilee Hills",
        "zone": "jubilee-banjara",
        "address": "Road No. 45, Nandagiri Hills, Jubilee Hills, Hyderabad 500033",
        "coordinates": {"lat": 17.4334, "lng": 78.4069},
        "vibe_tags": ["Single-Origin Estates", "Cascading Brick Courtyard", "Manual Brew Bar", "High Creative Energy"],
        "price_tier": "₹₹",
        "hours": "08:00 AM – 11:00 PM",
        "peak_creative_hours": "09:30 AM – 12:30 PM & 04:00 PM – 07:00 PM",
        "hiring_status": "Hiring Creatives",
        "contacts": {
            "primary_person": "Nishant Sinha",
            "primary_role": "Founder & Master Roaster",
            "phone": "+91 91212 90045",
            "whatsapp": "+919121290045",
            "email": "connect@roasterycoffee.in",
            "instagram": "@roasterycoffeehouseindia",
            "instagram_url": "https://instagram.com/roasterycoffeehouseindia",
            "website": "https://roasterycoffee.co.in",
            "secondary_person": "Events & Community: Priya Sharma"
        },
        "dossier": {
            "about": "Set inside a sprawling bungalow wrapped in red-brick textures and foliage, Roastery Coffee House single-handedly popularized specialty third-wave coffee in Hyderabad. It acts as the de-facto morning salon for indie directors, architects, and writers debating scripts over pour-overs.",
            "insider_tip": "Ask for the Chemex bar seat on the inner verandah. Request the Monsoon Malabar AA roast with their signature sourdough avocado toast.",
            "amenities": ["High-Speed Wi-Fi", "Outdoor Courtyard", "Manual Pour-Over Bar", "Valet Parking", "Pet Friendly", "Ample Power Plugs"]
        },
        "latest_drop": {
            "timestamp": "42m ago",
            "type": "New Roast Drop",
            "title": "Araku Valley Microlot Series",
            "snippet": "Fresh anaerobic fermentation batch from Chintapalli Estate now on the siphon bar."
        }
    },
    {
        "id": "autumn-leaf-cafe-jubilee",
        "name": "Autumn Leaf Cafe",
        "tagline": "A serene 1970s garden villa marrying artisanal design, home goods, and garden dining.",
        "category": "cafe",
        "category_label": "Botanical Cafe & Design Store",
        "neighborhood": "Jubilee Hills",
        "zone": "jubilee-banjara",
        "address": "Plot 823, Road No. 41, CBI Colony, Jubilee Hills, Hyderabad 500033",
        "coordinates": {"lat": 17.4367, "lng": 78.4019},
        "vibe_tags": ["Garden Sanctuary", "Antique Teak Interiors", "Pet Friendly", "Deep Focus"],
        "price_tier": "₹₹₹",
        "hours": "09:00 AM – 10:30 PM",
        "peak_creative_hours": "10:00 AM – 01:00 PM",
        "hiring_status": "Open for Collabs",
        "contacts": {
            "primary_person": "Meghana Rao",
            "primary_role": "Founder & Creative Director",
            "phone": "+91 98490 28411",
            "whatsapp": "+919849028411",
            "email": "curator@autumnleafcafe.com",
            "instagram": "@autumnleafcafe",
            "instagram_url": "https://instagram.com/autumnleafcafe",
            "website": "https://autumnleafcafe.com",
            "secondary_person": "Gallery & Popups: Siddharth Varma"
        },
        "dossier": {
            "about": "Tucked away in the leafy lanes of Jubilee Hills Road 41, Autumn Leaf is housed in an old residential property restored with reclaimed Chettinad pillars, terrazzo flooring, and towering tamarind trees. An integrated boutique curates bespoke brassware and handcrafted textiles.",
            "insider_tip": "The secluded garden tables under the canopy have dedicated power outlets and stable Wi-Fi. Order the Rosemary Iced Tea and Walnut Brownie.",
            "amenities": ["Al-Fresco Dining", "Artisan Retail Store", "Power Sockets", "Wi-Fi", "Dog Friendly", "Quiet Nooks"]
        },
        "latest_drop": {
            "timestamp": "1h ago",
            "type": "Weekend Popup",
            "title": "Koppa Studio Ceramics Showcase",
            "snippet": "Hand-thrown stoneware & ceramic planters exhibition this Saturday."
        }
    },
    {
        "id": "lamakaan-cultural-hub-banjara",
        "name": "Lamakaan",
        "tagline": "The radical non-commercial open cultural space for theatre, literature, and art.",
        "category": "art_culture",
        "category_label": "Cultural Center & Public Salon",
        "neighborhood": "Banjara Hills",
        "zone": "jubilee-banjara",
        "address": "Off Road No. 1, Opposite GVK One Mall, Banjara Hills, Hyderabad 500034",
        "coordinates": {"lat": 17.4223, "lng": 78.4482},
        "vibe_tags": ["Radical Theatre", "Irani Chai & Samosa", "Public Debates", "Free Creative Space"],
        "price_tier": "₹",
        "hours": "10:00 AM – 10:00 PM (Closed Mondays)",
        "peak_creative_hours": "05:00 PM – 09:30 PM",
        "hiring_status": "Hosting Popups",
        "contacts": {
            "primary_person": "Ashhar Farhan",
            "primary_role": "Co-Founder & Trustee",
            "phone": "+91 96427 31329",
            "whatsapp": "+919642731329",
            "email": "admin@lamakaan.com",
            "instagram": "@lamakaan_hyd",
            "instagram_url": "https://instagram.com/lamakaan_hyd",
            "website": "https://lamakaan.com",
            "secondary_person": "Programming Lead: Humera Ahmed"
        },
        "dossier": {
            "about": "Named 'The Placeless Space' in Urdu, Lamakaan is an inclusive, non-profit cultural institution fostering unhindered artistic expression. From grassroots plays in Dakhni to documentary screenings and book launches, it remains the intellectual heartbeat of Hyderabad's creative scene.",
            "insider_tip": "Grab a hot glass of ₹15 Irani chai and mutton samosas from the canteen; take a seat on the stone steps beneath the giant rock outcrop during the sunset play reading.",
            "amenities": ["Amphitheatre", "Exhibition Gallery", "Free Public Access", "Subsidized Canteen", "Book Exchange", "Open Stage"]
        },
        "latest_drop": {
            "timestamp": "2h ago",
            "type": "Live Play",
            "title": "Dakhni Folk Ensemble Performance",
            "snippet": "Live street theatre and musical performance starting at 07:00 PM tonight."
        }
    },
    {
        "id": "kalakriti-art-gallery-banjara",
        "name": "Kalakriti Art Gallery",
        "tagline": "Contemporary fine arts, historic Deccan cartography, and multidisciplinary exhibitions.",
        "category": "art_culture",
        "category_label": "Contemporary Art Gallery",
        "neighborhood": "Banjara Hills",
        "zone": "jubilee-banjara",
        "address": "468, Road No. 10, Banjara Hills, Hyderabad 500034",
        "coordinates": {"lat": 17.4285, "lng": 78.4384},
        "vibe_tags": ["Fine Art Curations", "Antique Maps of Deccan", "Artist Residencies", "Quiet Contemplation"],
        "price_tier": "₹₹₹₹",
        "hours": "11:00 AM – 07:00 PM (Open 7 Days)",
        "peak_creative_hours": "02:00 PM – 05:00 PM",
        "hiring_status": "Studio Residencies",
        "contacts": {
            "primary_person": "Prshant Lahoti",
            "primary_role": "Managing Trustee & Collector",
            "phone": "+91 40 6656 4444",
            "whatsapp": "+919849012345",
            "email": "info@kalakriti.in",
            "instagram": "@kalakritiartgallery",
            "instagram_url": "https://instagram.com/kalakritiartgallery",
            "website": "https://kalakritiartgallery.com",
            "secondary_person": "Chief Curator: Renu Modi"
        },
        "dossier": {
            "about": "Founded in 2002, Kalakriti is Central India's premier contemporary art gallery. Beyond showcasing established Indian modernists and emerging sculptors, Kalakriti houses the prestigious Prashant K. Lahoti Collection of antique maps, rare lithographs, and Deccan cartography dating back to the 16th century.",
            "insider_tip": "Ask to view the archived cartography wing on the upper deck — it features 18th-century hand-colored survey maps of Golconda and Hyderabad.",
            "amenities": ["Museum-Grade Lighting", "Printmaking Studio", "Art Library", "Artist Talks", "Climate-Controlled Vault"]
        },
        "latest_drop": {
            "timestamp": "3h ago",
            "type": "Exhibition",
            "title": "Deccan Topographies & Modernity",
            "snippet": "New solo exhibition by contemporary sculptor A. Ramachandran opens this Friday."
        }
    },
    {
        "id": "raw-mango-banjara",
        "name": "Raw Mango Banjara Hills",
        "tagline": "Sanjay Garg's architectural handloom sanctuary exploring Indian craftsmanship.",
        "category": "brand_fashion",
        "category_label": "Artisanal Fashion & Architecture",
        "neighborhood": "Banjara Hills",
        "zone": "jubilee-banjara",
        "address": "Road No. 10, Singhania Villa, Banjara Hills, Hyderabad 500034",
        "coordinates": {"lat": 17.4297, "lng": 78.4358},
        "vibe_tags": ["Chanderi & Varanasi Silks", "Brutalist Courtyard", "Textile Heritage", "High Craft"],
        "price_tier": "₹₹₹₹",
        "hours": "11:00 AM – 08:00 PM",
        "peak_creative_hours": "12:00 PM – 04:00 PM",
        "hiring_status": "Walk-ins Welcome",
        "contacts": {
            "primary_person": "Sanjay Garg",
            "primary_role": "Founder & Textile Designer",
            "phone": "+91 40 2335 1200",
            "whatsapp": "+919810012345",
            "email": "hyderabad@rawmango.com",
            "instagram": "@raw_mango",
            "instagram_url": "https://instagram.com/raw_mango",
            "website": "https://rawmango.com",
            "secondary_person": "Boutique Manager: Ananya Das"
        },
        "dossier": {
            "about": "Raw Mango's Hyderabad flagship is as much an architectural statement as a fashion atelier. Designed with raw lime plaster walls, exposed concrete, and minimalist brass fixtures, the space celebrates indigenous weaving techniques with modern sensibilities.",
            "insider_tip": "Notice how the spatial acoustics create an intentional monastic hush. Study the bespoke hand-woven brocades in the central vault.",
            "amenities": ["Architectural Interior", "Textile Archive", "Private Styling Salon", "Lounge Area", "Valet Service"]
        },
        "latest_drop": {
            "timestamp": "4h ago",
            "type": "Collection Release",
            "title": "Muraqqa: Deccan Silk Silhouettes",
            "snippet": "Limited-edition brocade jackets inspired by Golconda court miniature paintings."
        }
    },
    {
        "id": "roast-ccx-jubilee",
        "name": "Roast CCX (Coffee Collective)",
        "tagline": "Cyberpunk brutalist coffee lounge with cold brew taps and high-focus workstations.",
        "category": "cafe",
        "category_label": "Specialty Coffee Lab",
        "neighborhood": "Jubilee Hills",
        "zone": "jubilee-banjara",
        "address": "Road No. 45, Beside Croma, Jubilee Hills, Hyderabad 500033",
        "coordinates": {"lat": 17.4322, "lng": 78.4098},
        "vibe_tags": ["Nitro Cold Brew Taps", "Monochrome Industrial", "Late Night Coffee", "Tech Creatives"],
        "price_tier": "₹₹",
        "hours": "07:30 AM – 01:00 AM",
        "peak_creative_hours": "08:00 PM – 11:30 PM",
        "hiring_status": "Hiring Creatives",
        "contacts": {
            "primary_person": "Karthik Reddy",
            "primary_role": "Head of Operations & Coffee Strategy",
            "phone": "+91 80088 12344",
            "whatsapp": "+918008812344",
            "email": "roastccx@gmail.com",
            "instagram": "@roastccx",
            "instagram_url": "https://instagram.com/roastccx",
            "website": "https://roastccx.com",
            "secondary_person": "Lead Barista: Arvind Kumar"
        },
        "dossier": {
            "about": "Roast CCX reimagines the coffeehouse as a high-octane creative nerve center. Dark steel counters, glass partitions, and precision Modbar taps yield a sharp, contemporary atmosphere favored by founders and digital product designers.",
            "insider_tip": "Try their Nitro Cascara or the Smoked Orange Espresso. The mezzanine level features ergonomic standing desks with gigabit Wi-Fi.",
            "amenities": ["Gigabit Wi-Fi", "Standing Workstations", "Modbar Espresso Bar", "Late Night Seating", "Outdoor Deck"]
        },
        "latest_drop": {
            "timestamp": "5h ago",
            "type": "Design Talk",
            "title": "Midnight UX Teardown Meetup",
            "snippet": "Hyderabad Designers Guild hosting a live case-study critique tonight at 09:00 PM."
        }
    },
    {
        "id": "true-black-specialty-coffee",
        "name": "True Black Specialty Coffee",
        "tagline": "Disciplined minimalism, Japanese pour-over aesthetics, and estate transparency.",
        "category": "cafe",
        "category_label": "Minimalist Coffee Sanctuary",
        "neighborhood": "Jubilee Hills",
        "zone": "jubilee-banjara",
        "address": "Plot 212, Road No. 36, Jubilee Hills, Hyderabad 500033",
        "coordinates": {"lat": 17.4371, "lng": 78.4034},
        "vibe_tags": ["Japanese Minimalist", "Kalita Wave Pour-over", "Acoustic Silence", "Pure Focus"],
        "price_tier": "₹₹",
        "hours": "08:00 AM – 10:00 PM",
        "peak_creative_hours": "08:30 AM – 11:30 AM",
        "hiring_status": "Walk-ins Welcome",
        "contacts": {
            "primary_person": "Abhishek Rao",
            "primary_role": "Founder & Sensory Specialist",
            "phone": "+91 95020 44552",
            "whatsapp": "+919502044552",
            "email": "info@trueblackcoffee.com",
            "instagram": "@trueblackcoffee",
            "instagram_url": "https://instagram.com/trueblackcoffee",
            "website": "https://trueblackcoffee.com",
            "secondary_person": "Brew Quality: Divya P."
        },
        "dossier": {
            "about": "True Black strips away coffee culture fluff: no syrupy concoctions, just meticulous temperature calibration, micro-lot traceability, and a calm, monastic interior with black oak counters and muted lighting.",
            "insider_tip": "Order the Geisha or Ratnagiri Estate Anaerobic on the Kalita Wave dripper. Note their 'No Loud Calls' policy inside the brew room.",
            "amenities": ["No-Loud-Calls Quiet Zone", "Manual Filter Bar", "Power Outlets", "Espresso Tasting Flights"]
        },
        "latest_drop": {
            "timestamp": "6h ago",
            "type": "Sensory Cupping",
            "title": "Public Coffee Cupping Session",
            "snippet": "Blind cupping of 6 Indian microlots this Sunday at 10:00 AM."
        }
    },
    {
        "id": "aaromale-creative-community",
        "name": "Aaromale - Cafe & Creative Community",
        "tagline": "An organic creative sanctuary for indie musicians, painters, and open-air workshops.",
        "category": "art_culture",
        "category_label": "Arts Collective & Garden Cafe",
        "neighborhood": "Jubilee Hills",
        "zone": "jubilee-banjara",
        "address": "Plot 537, Road No. 1, Film Nagar, Jubilee Hills, Hyderabad 500096",
        "coordinates": {"lat": 17.4201, "lng": 78.4112},
        "vibe_tags": ["Art Collective", "Acoustic Open Mics", "Pottery Workshops", "Film Screenings"],
        "price_tier": "₹₹",
        "hours": "08:00 AM – 11:00 PM",
        "peak_creative_hours": "05:00 PM – 09:00 PM",
        "hiring_status": "Open for Collabs",
        "contacts": {
            "primary_person": "Varun T.",
            "primary_role": "Creative Director & Co-Founder",
            "phone": "+91 99882 12345",
            "whatsapp": "+919988212345",
            "email": "community@aaromale.life",
            "instagram": "@aaromale_hyd",
            "instagram_url": "https://instagram.com/aaromale_hyd",
            "website": "https://aaromale.life",
            "secondary_person": "Artist Relations: Kavya N."
        },
        "dossier": {
            "about": "Nestled in Film Nagar, Aaromale converted a vintage residential home into an open multidisciplinary salon. From weekend pottery classes on the lawn to indie singer-songwriter sessions under fairy lights, it is a haven for young Hyderabad artists.",
            "insider_tip": "The attic room hosts intimate script readings and podcast recording sessions. The Kerala iced coffee and shakshuka are local favorites.",
            "amenities": ["Open Lawn Stage", "Workshop Pavilion", "Podcast Studio Nook", "Art Supplies On-Site", "Dog Friendly"]
        },
        "latest_drop": {
            "timestamp": "7h ago",
            "type": "Workshop",
            "title": "Deccan Miniature Painting Workshop",
            "snippet": "Learn traditional natural stone pigment mixing with master artist Govind Raj."
        }
    },
    {
        "id": "the-banyan-tree-studio",
        "name": "The Banyan Tree Studio",
        "tagline": "Award-winning architectural and spatial design studio focusing on biophilic luxury.",
        "category": "design_studio",
        "category_label": "Architecture & Spatial Design",
        "neighborhood": "Jubilee Hills",
        "zone": "jubilee-banjara",
        "address": "Road No. 36, Near Peddamma Temple Metro, Jubilee Hills, Hyderabad 500033",
        "coordinates": {"lat": 17.4390, "lng": 78.4010},
        "vibe_tags": ["Biophilic Architecture", "Material Library", "Sustainable Interiors", "Spatial Design"],
        "price_tier": "₹₹₹₹",
        "hours": "09:30 AM – 06:30 PM (Mon–Fri)",
        "peak_creative_hours": "11:00 AM – 04:00 PM",
        "hiring_status": "Hiring Creatives",
        "contacts": {
            "primary_person": "Sunil Nambiar",
            "primary_role": "Principal Architect & Founder",
            "phone": "+91 40 4010 8899",
            "whatsapp": "+919848033221",
            "email": "studio@banyantree.design",
            "instagram": "@banyantreestudio",
            "instagram_url": "https://instagram.com/banyantreestudio",
            "website": "https://banyantree.design",
            "secondary_person": "Design Lead: Sahithi V."
        },
        "dossier": {
            "about": "The Banyan Tree Studio has designed some of Hyderabad's most iconic residences, boutique hotels, and experimental retail spaces. Their studio houses a tactile material lab of local granite, basalt stone, brass, and recycled hardwoods.",
            "insider_tip": "Call ahead for appointment access to their material exploration library. They frequently host interdisciplinary architecture juries.",
            "amenities": ["Material Exploration Lab", "Architectural Scale Model Workshop", "Design Library", "CAD / VR Walkthrough Lab"]
        },
        "latest_drop": {
            "timestamp": "8h ago",
            "type": "Studio Hiring",
            "title": "Hiring Senior Computational Architect",
            "snippet": "Looking for Rhino/Grasshopper computational designers for a new lakefront pavilion."
        }
    },
    {
        "id": "good-earth-banjara",
        "name": "Good Earth Hyderabad",
        "tagline": "Design house celebrating the heritage of the Silk Route and Deccan royal aesthetics.",
        "category": "brand_fashion",
        "category_label": "Luxury Design & Home Goods",
        "neighborhood": "Banjara Hills",
        "zone": "jubilee-banjara",
        "address": "Road No. 12, NBT Nagar, Banjara Hills, Hyderabad 500034",
        "coordinates": {"lat": 17.4245, "lng": 78.4412},
        "vibe_tags": ["Deccan Motifs", "Hand-Painted Ceramics", "Sensory Aromas", "Luxury Craft"],
        "price_tier": "₹₹₹₹",
        "hours": "11:00 AM – 08:00 PM",
        "peak_creative_hours": "03:00 PM – 06:30 PM",
        "hiring_status": "Walk-ins Welcome",
        "contacts": {
            "primary_person": "Anita Lal",
            "primary_role": "Creative Director & Founder",
            "phone": "+91 40 2337 5444",
            "whatsapp": "+919910012345",
            "email": "customercare@goodearth.in",
            "instagram": "@goodearthindia",
            "instagram_url": "https://instagram.com/goodearthindia",
            "website": "https://goodearth.in",
            "secondary_person": "Store Curator: Meera Iyer"
        },
        "dossier": {
            "about": "Set inside a converted multi-story bungalow on Road 12, Good Earth presents an immersive universe of Deccan chintz, hand-turned stoneware, fine bone china, and perfumed botanicals. It is an enduring benchmark for luxury Indian lifestyle design.",
            "insider_tip": "The home fragrance and heritage textiles section on the second floor contains limited-edition pieces inspired by Asaf Jahi palace motifs.",
            "amenities": ["Lifestyle Showroom", "Aroma Bar", "Custom Gift Registry", "Valet Parking"]
        },
        "latest_drop": {
            "timestamp": "9h ago",
            "type": "New Collection",
            "title": "Golconda Gardenia Fine Porcelain",
            "snippet": "New bone china collection featuring Mughal floral borders and 24k gold gilding."
        }
    },

    # --- MADHAPUR, HITEC CITY & GACHIBOWLI ---
    {
        "id": "crave-kraft-specialty-coffee",
        "name": "Crave Kraft Specialty Coffee",
        "tagline": "Where design agency founders and product engineers fuel up over precision espresso.",
        "category": "cafe",
        "category_label": "Indie Specialty Coffee",
        "neighborhood": "Madhapur & Hitec City",
        "zone": "madhapur-hitec",
        "address": "Ayyappa Society Main Road, Near Madhapur Metro, Hyderabad 500081",
        "coordinates": {"lat": 17.4491, "lng": 78.3845},
        "vibe_tags": ["Tech-Design Salons", "Aeropress Bar", "Lo-Fi Beats", "Startup Brainstorming"],
        "price_tier": "₹₹",
        "hours": "08:00 AM – 11:30 PM",
        "peak_creative_hours": "10:00 AM – 01:00 PM & 08:00 PM – 11:00 PM",
        "hiring_status": "Hiring Creatives",
        "contacts": {
            "primary_person": "Rahul Sen",
            "primary_role": "Co-Founder & Coffee Curator",
            "phone": "+91 98711 23450",
            "whatsapp": "+919871123450",
            "email": "cravekraft@gmail.com",
            "instagram": "@cravekraftcoffee",
            "instagram_url": "https://instagram.com/cravekraftcoffee",
            "website": "https://cravekraft.in",
            "secondary_person": "Events Coordinator: Tanvi Joshi"
        },
        "dossier": {
            "about": "Crave Kraft is the unofficial think-tank for Madhapur's design and engineering underground. Clean plywood tables, warm accent lighting, and a focused playlist of ambient jazz and lo-fi beats create the ideal environment for deep flow state work.",
            "insider_tip": "Their iced tonic espresso with kaffir lime zest is legendary. Grab the corner booth with multiple USB-C PD fast chargers.",
            "amenities": ["USB-C PD Fast Charging", "1 Gbps Fiber Wi-Fi", "Aeropress Bar", "Outdoor Smoking Zone", "Custom Roasts"]
        },
        "latest_drop": {
            "timestamp": "28m ago",
            "type": "Community Meetup",
            "title": "Saturday Morning Figma Jam",
            "snippet": "Madhapur UI/UX community holding informal design system critique this Saturday at 10 AM."
        }
    },
    {
        "id": "state-gallery-of-art-madhapur",
        "name": "State Gallery of Art (Chitramayee)",
        "tagline": "Expansive public modernist art pavilion surrounded by granite boulder landscape.",
        "category": "art_culture",
        "category_label": "Public Contemporary Art Gallery",
        "neighborhood": "Madhapur & Hitec City",
        "zone": "madhapur-hitec",
        "address": "Road No. 1, Kavuri Hills, Madhapur, Hyderabad 500033",
        "coordinates": {"lat": 17.4398, "lng": 78.3972},
        "vibe_tags": ["Monumental Sculptures", "Boulder Amphitheatre", "State Art Exhibitions", "Photographer Haven"],
        "price_tier": "₹",
        "hours": "10:30 AM – 06:30 PM (Closed Mondays)",
        "peak_creative_hours": "03:30 PM – 06:00 PM",
        "hiring_status": "Hosting Popups",
        "contacts": {
            "primary_person": "Dr. K. Lakshmi",
            "primary_role": "Director & Chief Curator",
            "phone": "+91 40 2311 3369",
            "whatsapp": "+919440011223",
            "email": "stategalleryofart@telangana.gov.in",
            "instagram": "@stategalleryofarthyd",
            "instagram_url": "https://instagram.com/stategalleryofarthyd",
            "website": "https://stategalleryofart.telangana.gov.in",
            "secondary_person": "Exhibitions In-Charge: M. Ramana"
        },
        "dossier": {
            "about": "Constructed across rugged Deccan granite rocks, Chitramayee State Gallery of Art is Hyderabad's largest contemporary exhibition campus. It hosts the Hyderabad Design Week, national sculpture symposiums, and fine arts graduating showcases.",
            "insider_tip": "Wander through the outdoor sculpture garden behind the main wing during golden hour. The interplay between raw granite boulders and bronze statues is breathtaking.",
            "amenities": ["Outdoor Sculpture Garden", "Auditorium", "Free Parking", "Natural Daylighting", "Wheelchair Accessible"]
        },
        "latest_drop": {
            "timestamp": "1h ago",
            "type": "Exhibition",
            "title": "Telangana Contemporary Printmakers 2026",
            "snippet": "Over 80 experimental lithographs, woodcuts, and etching prints now on display in Hall B."
        }
    },
    {
        "id": "f45-design-studio-lab",
        "name": "F45 Design Studio & Lab",
        "tagline": "Specialized spatial strategy, brand architecture, and interactive generative installations.",
        "category": "design_studio",
        "category_label": "Design & Innovation Lab",
        "neighborhood": "Madhapur & Hitec City",
        "zone": "madhapur-hitec",
        "address": "4th Floor, Durgam Cheruvu Boulevard, Madhapur, Hyderabad 500081",
        "coordinates": {"lat": 17.4421, "lng": 78.3887},
        "vibe_tags": ["Brand Architecture", "Generative Installations", "Spatial UX", "Open Design Sprints"],
        "price_tier": "₹₹₹₹",
        "hours": "10:00 AM – 07:00 PM",
        "peak_creative_hours": "02:00 PM – 06:00 PM",
        "hiring_status": "Hiring Creatives",
        "contacts": {
            "primary_person": "Aditya Varma",
            "primary_role": "Creative Director & Partner",
            "phone": "+91 40 4855 9900",
            "whatsapp": "+919849922110",
            "email": "hello@f45studio.design",
            "instagram": "@f45designlab",
            "instagram_url": "https://instagram.com/f45designlab",
            "website": "https://f45studio.design",
            "secondary_person": "Tech & Creative Lead: Sandeep K."
        },
        "dossier": {
            "about": "F45 sits at the intersection of architecture, visual identity, and creative technology. Overlooking the Durgam Cheruvu lake, their glass-and-steel studio produces identity systems and flagship retail experiences for forward-thinking Indian brands.",
            "insider_tip": "They host bi-weekly 'Open Friday Demos' showcasing experimental TouchDesigner and generative code visuals. Send an email to reserve an observer seat.",
            "amenities": ["Prototyping Lab", "Interactive Projection Wall", "Material Library", "Lake View Terrace"]
        },
        "latest_drop": {
            "timestamp": "2h ago",
            "type": "Project Launch",
            "title": "Spatial Identity for Deccan Craft Pavilion",
            "snippet": "Case study published documenting kinetic typography and responsive LED wayfinding."
        }
    },
    {
        "id": "comic-social-kondapur",
        "name": "Comic Social",
        "tagline": "Graphic novel haven, manga studio, and illustrated coffeehouse for comic book artists.",
        "category": "coworking_maker",
        "category_label": "Illustration Cafe & Graphic Studio",
        "neighborhood": "Madhapur & Hitec City",
        "zone": "madhapur-hitec",
        "address": "Opposite Botanical Garden, Kondapur / Hitec City, Hyderabad 500084",
        "coordinates": {"lat": 17.4610, "lng": 78.3621},
        "vibe_tags": ["Graphic Novels & Manga", "Drawing Tablets", "Indie Comic Artists", "Playful Energy"],
        "price_tier": "₹₹",
        "hours": "11:00 AM – 11:00 PM",
        "peak_creative_hours": "04:00 PM – 08:30 PM",
        "hiring_status": "Open for Collabs",
        "contacts": {
            "primary_person": "Deepak George",
            "primary_role": "Founder & Comic Curator",
            "phone": "+91 90001 88223",
            "whatsapp": "+919000188223",
            "email": "comicsocialhyd@gmail.com",
            "instagram": "@comicsocial.in",
            "instagram_url": "https://instagram.com/comicsocial.in",
            "website": "https://comicsocial.in",
            "secondary_person": "Community Manager: Sharon Paul"
        },
        "dossier": {
            "about": "Part cafe, part graphic arts library, Comic Social houses over 3,000 rare graphic novels, indie zines, and manga volumes. It has become the meeting ground for Hyderabad's concept artists, storyboard creators, and animators.",
            "insider_tip": "Bring your iPad or sketchbook — you get 15% off artisanal brews when drawing in-house on Tuesday sketch nights.",
            "amenities": ["3,000+ Graphic Novel Library", "Wacom & iPad Friendly Tables", "Coffee Bar", "Board Games Nook", "Zine Printing Corner"]
        },
        "latest_drop": {
            "timestamp": "3h ago",
            "type": "Zine Fair",
            "title": "Hyderabad Indie Zine Fest 2026",
            "snippet": "Submissions open for self-published indie comics, risograph prints, and sticker art."
        }
    },
    {
        "id": "theory-cafe-bar-financial-district",
        "name": "Theory Cafe & Bar",
        "tagline": "Architectural glasshouse with high ceilings, lush greenery, and modern gastronomy.",
        "category": "cafe",
        "category_label": "Glasshouse Cafe & Dining",
        "neighborhood": "Gachibowli & FinDistrict",
        "zone": "gachibowli-financial",
        "address": "ISB Road, Financial District, Nanakramguda, Hyderabad 500032",
        "coordinates": {"lat": 17.4255, "lng": 78.3421},
        "vibe_tags": ["Brutalist Glasshouse", "Creative Cocktails", "Design Discussions", "High Volume Ceilings"],
        "price_tier": "₹₹₹",
        "hours": "11:30 AM – 12:00 AM",
        "peak_creative_hours": "04:30 PM – 08:00 PM",
        "hiring_status": "Walk-ins Welcome",
        "contacts": {
            "primary_person": "Vikram Chunduru",
            "primary_role": "Managing Director",
            "phone": "+91 40 6824 5500",
            "whatsapp": "+919866012345",
            "email": "reservations@theorycafe.in",
            "instagram": "@theoryhyd",
            "instagram_url": "https://instagram.com/theoryhyd",
            "website": "https://theorycafe.in",
            "secondary_person": "Culinary Director: Chef Anirudh"
        },
        "dossier": {
            "about": "Soaring double-height glass panels, exposed steel trusses, and mature indoor palms give Theory an airy, greenhouse-meets-industrial presence in the heart of the Financial District. It serves as an after-hours retreat for tech leaders and creative executives.",
            "insider_tip": "The central mezzanine table has the best ambient natural light for portfolio presentations and client dinners.",
            "amenities": ["Glasshouse Architecture", "Cocktail Bar", "Valet Parking", "High Speed Wi-Fi", "Outdoor Deck"]
        },
        "latest_drop": {
            "timestamp": "4h ago",
            "type": "New Menu",
            "title": "Spring Botanical Cocktail Tasting",
            "snippet": "Cocktails infused with local Mahua, Gondhoraj lemon, and smoked vetiver."
        }
    },
    {
        "id": "the-glass-onion-gachibowli",
        "name": "The Glass Onion",
        "tagline": "Minimalist golf-course overlook cafe framed by minimalist concrete and panoramic vistas.",
        "category": "cafe",
        "category_label": "Panoramic Vista Cafe",
        "neighborhood": "Gachibowli & FinDistrict",
        "zone": "gachibowli-financial",
        "address": "Boulder Hills Golf & Country Club, Gachibowli, Hyderabad 500032",
        "coordinates": {"lat": 17.4378, "lng": 78.3610},
        "vibe_tags": ["Golf Course Greens", "Minimalist Concrete", "Golden Hour Views", "Creative Strategy"],
        "price_tier": "₹₹₹",
        "hours": "07:30 AM – 11:00 PM",
        "peak_creative_hours": "05:00 PM – 07:30 PM (Sunset)",
        "hiring_status": "Open for Collabs",
        "contacts": {
            "primary_person": "Samir Sharma",
            "primary_role": "Co-Founder",
            "phone": "+91 80080 33441",
            "whatsapp": "+918008033441",
            "email": "glassonionhyd@gmail.com",
            "instagram": "@theglassonionhyd",
            "instagram_url": "https://instagram.com/theglassonionhyd",
            "website": "https://theglassonion.in",
            "secondary_person": "PR Lead: Natasha K."
        },
        "dossier": {
            "about": "Perched on the rolling lawns of Boulder Hills, The Glass Onion boasts floor-to-ceiling glass wrapping around emerald fairways and granite outcrops. Sunset brings a luminous amber glow that makes it a favorite spot for closing deals and sketching new product concepts.",
            "insider_tip": "Arrive at 05:00 PM to catch the sunset horizon across the boulders. Order the Burrata salad and single-origin cold brew.",
            "amenities": ["Panoramic Horizon View", "Outdoor Terrace", "Peaceful Acoustic Vibe", "Dedicated Parking"]
        },
        "latest_drop": {
            "timestamp": "5h ago",
            "type": "Acoustic Evening",
            "title": "Sunset Jazz Quintet",
            "snippet": "Live jazz standards on the terrace during sunset this Sunday."
        }
    },

    # --- BEGUMPET, SECUNDERABAD & SAINIKPURI ---
    {
        "id": "the-coffee-cup-sainikpuri",
        "name": "The Coffee Cup",
        "tagline": "The legendary vintage bohemian sanctuary that sparked Sainikpuri's indie cafe wave.",
        "category": "cafe",
        "category_label": "Bohemian Cafe & Cultural Nook",
        "neighborhood": "Sainikpuri & Secunderabad",
        "zone": "secunderabad-sainikpuri",
        "address": "E118, Sainikpuri 5th Avenue, Behind Defiance Bar, Secunderabad 500094",
        "coordinates": {"lat": 17.4878, "lng": 78.5442},
        "vibe_tags": ["Vintage Brick", "Old Books Nook", "Live Acoustic Stage", "Sainikpuri Heritage"],
        "price_tier": "₹₹",
        "hours": "09:00 AM – 11:30 PM",
        "peak_creative_hours": "04:00 PM – 08:30 PM",
        "hiring_status": "Hosting Popups",
        "contacts": {
            "primary_person": "Varun Reddy",
            "primary_role": "Founder & Cafe Curator",
            "phone": "+91 95027 12344",
            "whatsapp": "+919502712344",
            "email": "thecoffeecup.hyd@gmail.com",
            "instagram": "@thecoffeecuphyd",
            "instagram_url": "https://instagram.com/thecoffeecuphyd",
            "website": "https://thecoffeecup.in",
            "secondary_person": "Live Events: Rohit Roy"
        },
        "dossier": {
            "about": "Before cafe culture swept Hyderabad, The Coffee Cup established Sainikpuri as an alternative creative enclave. Built with reclaimed railway sleeper wood, weathered brickwork, and shelves of worn paperbacks, it has hosted hundreds of young poets, guitarists, and visual storytellers.",
            "insider_tip": "The rooftop terrace table under the bougainvillea is unmatched on cool Secunderabad evenings. Order the Caramel Frappe and the Club Sandwich.",
            "amenities": ["Book Library", "Open-Air Rooftop", "Live Acoustic Setup", "Pet Friendly", "Board Games"]
        },
        "latest_drop": {
            "timestamp": "1h ago",
            "type": "Poetry Slam",
            "title": "Twin Cities Spoken Word Open Mic",
            "snippet": "Secunderabad's long-running open mic returns this Friday evening at 07:00 PM."
        }
    },
    {
        "id": "groove-9-sainikpuri",
        "name": "Groove 9",
        "tagline": "Al-fresco bohemian arts cafe wrapped in tropical foliage and fairy lights.",
        "category": "cafe",
        "category_label": "Artisan Garden Cafe",
        "neighborhood": "Sainikpuri & Secunderabad",
        "zone": "secunderabad-sainikpuri",
        "address": "Road No. 9, Defence Colony, Sainikpuri, Secunderabad 500094",
        "coordinates": {"lat": 17.4891, "lng": 78.5410},
        "vibe_tags": ["Tropical Garden", "Fairy Lights", "Indie Music Sessions", "Freelancer Friendly"],
        "price_tier": "₹₹",
        "hours": "11:00 AM – 11:00 PM",
        "peak_creative_hours": "05:00 PM – 09:30 PM",
        "hiring_status": "Walk-ins Welcome",
        "contacts": {
            "primary_person": "Kiran Joseph",
            "primary_role": "Managing Partner",
            "phone": "+91 97000 89112",
            "whatsapp": "+919700089112",
            "email": "groove9cafe@gmail.com",
            "instagram": "@groove9cafe",
            "instagram_url": "https://instagram.com/groove9cafe",
            "website": "https://groove9.com",
            "secondary_person": "Curator: Sneha Mathew"
        },
        "dossier": {
            "about": "Groove 9 captures the easy-going, cantonment charm of Secunderabad. Low wooden benches, gravel underfoot, and towering coconut palms make it feel a world away from the glass high-rises of Cyberabad.",
            "insider_tip": "Ideal for collaborative team brainstorms outdoors. Try their Peri Peri Fries and Vietnamese Drip Coffee.",
            "amenities": ["Lush Garden Seating", "Outdoor Wi-Fi", "Pet Friendly", "Acoustic Playlists"]
        },
        "latest_drop": {
            "timestamp": "3h ago",
            "type": "Art Workshop",
            "title": "Linocut Printmaking on Handmade Paper",
            "snippet": "Workshop with local printmaker Aditi Roy; all carving tools & inks provided."
        }
    },
    {
        "id": "concu-patisserie-begumpet",
        "name": "Conçu Patisserie (Begumpet)",
        "tagline": "Haute-patisserie design studio marrying French classical precision with architectural grace.",
        "category": "cafe",
        "category_label": "Design Patisserie & Salon",
        "neighborhood": "Begumpet",
        "zone": "begumpet-central",
        "address": "Country Club Road, Begumpet, Hyderabad 500016",
        "coordinates": {"lat": 17.4442, "lng": 78.4612},
        "vibe_tags": ["French Haute Patisserie", "Architectural Desserts", "Pastel Aesthetics", "High Society Salon"],
        "price_tier": "₹₹₹",
        "hours": "10:00 AM – 11:00 PM",
        "peak_creative_hours": "03:00 PM – 06:30 PM",
        "hiring_status": "Hiring Creatives",
        "contacts": {
            "primary_person": "Sahil Taneja",
            "primary_role": "Founder & Master Pastry Chef",
            "phone": "+91 99858 57724",
            "whatsapp": "+919985857724",
            "email": "contact@concu.in",
            "instagram": "@concuofficial",
            "instagram_url": "https://instagram.com/concuofficial",
            "website": "https://concu.in",
            "secondary_person": "Co-Founder & Design Lead: Swati Upadhyay"
        },
        "dossier": {
            "about": "Founded by Le Cordon Bleu alumnus Sahil Taneja and interior designer Swati Upadhyay, Conçu raised the standard of patisserie across India. Every tart, choux, and entremet is engineered like a miniature sculptural marvel in a soothing, sunlit pastel salon.",
            "insider_tip": "The Choux Bun with hazelnut praline and the Tiramisu Paris-Brest are architectural masterpieces. Pair with a double ristretto.",
            "amenities": ["Air-Conditioned Salon", "Artisan Bakery Display", "Valet Parking", "Bespoke Cake Studio"]
        },
        "latest_drop": {
            "timestamp": "4h ago",
            "type": "Seasonal Drop",
            "title": "Yuzu & White Peach Entremet",
            "snippet": "New seasonal geometric entremet with Japanese yuzu curd and almond sponge."
        }
    },
    {
        "id": "ofen-bakery-begumpet",
        "name": "Ofen Bakery & Cafe",
        "tagline": "Classic continental bakehouse beloved by generations of Hyderabad designers & writers.",
        "category": "cafe",
        "category_label": "Heritage European Bakehouse",
        "neighborhood": "Begumpet",
        "zone": "begumpet-central",
        "address": "Shop 1-10-63/1, Chikoti Gardens, Begumpet, Hyderabad 500016",
        "coordinates": {"lat": 17.4475, "lng": 78.4678},
        "vibe_tags": ["Sourdough & Bagels", "European Continental", "Quiet Heritage", "Writer Sanctuary"],
        "price_tier": "₹₹",
        "hours": "08:30 AM – 10:30 PM",
        "peak_creative_hours": "09:00 AM – 12:00 PM",
        "hiring_status": "Walk-ins Welcome",
        "contacts": {
            "primary_person": "Zareer Patel",
            "primary_role": "Proprietor & Master Baker",
            "phone": "+91 40 2776 6060",
            "whatsapp": "+919849055440",
            "email": "ofenbakery@gmail.com",
            "instagram": "@ofencafe",
            "instagram_url": "https://instagram.com/ofencafe",
            "website": "https://ofencafe.com",
            "secondary_person": "Manager: Farhan Irani"
        },
        "dossier": {
            "about": "Ofen is a Begumpet institution where classic sourdough loaves, croissants, and quiches have been baked fresh daily since the late 1990s. Its quiet, unassuming interior has witnessed decades of book pitches, architectural consultations, and morning coffee rituals.",
            "insider_tip": "Arrive early at 09:00 AM to snag the warm almond croissants straight from the oven. Pair with an Americano in the corner glass room.",
            "amenities": ["Fresh Bakery Counter", "Quiet Work Atmosphere", "Street Parking", "Wi-Fi"]
        },
        "latest_drop": {
            "timestamp": "6h ago",
            "type": "Fresh Batch",
            "title": "Ancient Grain Sourdough Loaves",
            "snippet": "36-hour slow fermented rye & spelt sourdough loaves now on the counter."
        }
    },

    # --- OLD CITY, CHARMINAR & MUSI HERITAGE ---
    {
        "id": "nimrah-cafe-bakery-charminar",
        "name": "Nimrah Cafe & Bakery",
        "tagline": "The epicenter of Hyderabadi Irani chai and Osmania biscuits, facing the iconic Charminar.",
        "category": "heritage_icon",
        "category_label": "Historic Irani Cafe & Cultural Icon",
        "neighborhood": "Old City & Charminar",
        "zone": "old-city-charminar",
        "address": "Opposite Mecca Masjid & Charminar, Old City, Hyderabad 500002",
        "coordinates": {"lat": 17.3616, "lng": 78.4747},
        "vibe_tags": ["Golden Hour Chai", "Charminar Silhouette", "Street Photography Hub", "Centuries of Culture"],
        "price_tier": "₹",
        "hours": "04:00 AM – 11:30 PM",
        "peak_creative_hours": "05:30 AM – 08:00 AM (Sunrise) & 05:30 PM – 07:00 PM (Sunset)",
        "hiring_status": "Walk-ins Welcome",
        "contacts": {
            "primary_person": "Aslam Aslani",
            "primary_role": "Second-Generation Owner & Cultural Ambassador",
            "phone": "+91 98480 33445",
            "whatsapp": "+919848033445",
            "email": "nimrahcafe@gmail.com",
            "instagram": "@nimrahcafe",
            "instagram_url": "https://instagram.com/nimrahcafe",
            "website": "https://nimrahcafe.com",
            "secondary_person": "Manager: Subhan Bhai"
        },
        "dossier": {
            "about": "Standing proudly on the plaza facing the 1591 Charminar, Nimrah is more than a tea stall: it is Hyderabad's ultimate public amphitheater. Street photographers, poets, typographers, and heritage conservationists congregate at dawn to sip creamy Zafrani chai as the morning mist clears over the minarets.",
            "insider_tip": "Visit at 05:45 AM before sunrise. Ask for 'Zafrani Special' chai with hot, salt-sweet Osmania and Tie biscuits fresh from the wood ovens.",
            "amenities": ["Direct View of Charminar", "Fresh Bakery Ovens", "Open Standing Plaza", "Historic Location"]
        },
        "latest_drop": {
            "timestamp": "18m ago",
            "type": "Heritage Moment",
            "title": "Dawn Heritage Photowalk",
            "snippet": "Deccan Architectural Photowalk gathering at Nimrah plaza this Sunday dawn at 06:00 AM."
        }
    },
    {
        "id": "chowmahalla-palace-pavilion",
        "name": "Chowmahalla Palace Cultural Pavilion",
        "tagline": "The grand Asaf Jahi seat of power, neoclassical courtyards, and royal craft archives.",
        "category": "heritage_icon",
        "category_label": "Palatial Heritage & Craft Archive",
        "neighborhood": "Old City & Charminar",
        "zone": "old-city-charminar",
        "address": "20-4-236, Khilwat, Motigalli, Hyderabad 500002",
        "coordinates": {"lat": 17.3578, "lng": 78.4712},
        "vibe_tags": ["Neoclassical Architecture", "Belgian Crystal Chandeliers", "Deccan Textile Archive", "Monolithic History"],
        "price_tier": "₹₹",
        "hours": "10:00 AM – 05:00 PM (Closed Fridays)",
        "peak_creative_hours": "11:00 AM – 03:00 PM",
        "hiring_status": "Studio Residencies",
        "contacts": {
            "primary_person": "G. Kishan Rao",
            "primary_role": "Director & Conservation In-Charge",
            "phone": "+91 40 2452 2032",
            "whatsapp": "+919849044332",
            "email": "info@chowmahalla.org",
            "instagram": "@chowmahallapalace_official",
            "instagram_url": "https://instagram.com/chowmahallapalace_official",
            "website": "https://chowmahalla.org",
            "secondary_person": "Curatorial Officer: Dr. Safia Begum"
        },
        "dossier": {
            "about": "Modeled after the Shah of Iran's palace in Tehran, Chowmahalla ('Four Palaces') is a masterclass in synthesis of Persian, Indo-Saracenic, and European Neoclassical architecture. Its Durbar Hall (Khilwat Mubarak) features 19 colossal Belgian crystal chandeliers and the sacred marble throne (Takht-e-Nishan).",
            "insider_tip": "The restored 1912 Rolls-Royce Silver Ghost in the vintage car court is an industrial design marvel. Walk through the textile galleries to see authentic Zardozi court robes.",
            "amenities": ["Sprawling Palace Gardens", "Neoclassical Architecture", "Guided Curatorial Tours", "Textile & Weaponry Gallery"]
        },
        "latest_drop": {
            "timestamp": "2h ago",
            "type": "Restoration Tour",
            "title": "Asaf Jahi Textile Conservation Lecture",
            "snippet": "Public lecture on preserving 19th-century gold zari textiles in the Durbar courtyard."
        }
    },
    {
        "id": "al-ghalia-attar-distillers",
        "name": "Nizam's Perfumers / Attar Al-Ghalia",
        "tagline": "6th generation master distillers of pure sandalwood, rose, and rare Deccan shamama.",
        "category": "heritage_icon",
        "category_label": "Historic Scent Atelier",
        "neighborhood": "Old City & Charminar",
        "zone": "old-city-charminar",
        "address": "Laad Bazaar, Near Charminar Kamani, Hyderabad 500002",
        "coordinates": {"lat": 17.3621, "lng": 78.4728},
        "vibe_tags": ["Artisanal Hydro-Distillation", "Pure Dehnal Oudh", "Vintage Crystal Bottles", "Olfactory Craft"],
        "price_tier": "₹₹₹",
        "hours": "11:00 AM – 10:00 PM",
        "peak_creative_hours": "04:00 PM – 08:00 PM",
        "hiring_status": "Walk-ins Welcome",
        "contacts": {
            "primary_person": "Mirza Nooruddin",
            "primary_role": "Master Perfumer & Patriarch",
            "phone": "+91 40 2457 7890",
            "whatsapp": "+919885066778",
            "email": "attar.alghalia@gmail.com",
            "instagram": "@attar_alghalia_hyd",
            "instagram_url": "https://instagram.com/attar_alghalia_hyd",
            "website": "https://attaralghalia.in",
            "secondary_person": "Senior Distiller: Mirza Danish"
        },
        "dossier": {
            "about": "Crafting natural non-alcoholic perfumes using the ancient Deg & Bhapka (copper cauldron and copper receiver) method, Al-Ghalia preserves the sensory heritage of the Nizami court. Each drop of Ruh Gulab (pure Damask rose) requires thousands of petals hydro-distilled in traditional copper alembics.",
            "insider_tip": "Ask Mirza Nooruddin to show you his 40-year-aged wild Assam agarwood oil and the 'Mitti Attar', which captures the exact scent of the first monsoon rain hitting parched red soil.",
            "amenities": ["Custom Scent Blending", "Vintage Cut-Glass Flacons", "Historic Workshop Consultation"]
        },
        "latest_drop": {
            "timestamp": "4h ago",
            "type": "New Distillation",
            "title": "Wild Assam 1984 Oudh Distillation",
            "snippet": "Aged 12-tola release of single-tree Assam agarwood hydro-distilled in pure Mysore sandalwood oil."
        }
    },
    {
        "id": "salar-jung-museum-arts",
        "name": "Salar Jung Museum (Decorative Arts Wing)",
        "tagline": "The monumental one-man museum of global decorative arts, jade crafts, and miniatures.",
        "category": "heritage_icon",
        "category_label": "National Museum & Arts Archive",
        "neighborhood": "Old City & Charminar",
        "zone": "old-city-charminar",
        "address": "Darusshifa, Musi River Southern Bank, Hyderabad 500002",
        "coordinates": {"lat": 17.3713, "lng": 78.4804},
        "vibe_tags": ["Veiled Rebecca Sculpture", "Jade Daggers", "Persian Carpets", "Decorative Arts Mastery"],
        "price_tier": "₹",
        "hours": "10:00 AM – 05:00 PM (Closed Fridays)",
        "peak_creative_hours": "10:30 AM – 02:00 PM",
        "hiring_status": "Studio Residencies",
        "contacts": {
            "primary_person": "Dr. A. Nagender Reddy",
            "primary_role": "Director & Chief Curator",
            "phone": "+91 40 2452 3211",
            "whatsapp": "+919440055443",
            "email": "salarmus@gmail.com",
            "instagram": "@salarjungmuseum",
            "instagram_url": "https://instagram.com/salarjungmuseum",
            "website": "https://salarjungmuseum.in",
            "secondary_person": "Manuscript Keeper: Dr. Zakiya Sultana"
        },
        "dossier": {
            "about": "Assembled largely by Nawab Mir Yousuf Ali Khan (Salar Jung III), this museum on the banks of the Musi contains over 46,000 art objects and 8,000 rare manuscripts. From Italian sculptor Benzoni's breathtaking marble 'Veiled Rebecca' to Mughal Emperor Shah Jahan's personal white jade wine cup.",
            "insider_tip": "Spend time in the Western European Porcelain gallery and the 17th-century Deccani calligraphy wing. The musical mechanical clock rings on the hour in the central hall.",
            "amenities": ["40+ Galleries", "Manuscript Conservation Lab", "Library", "Cafeteria", "Wheelchair Accessible"]
        },
        "latest_drop": {
            "timestamp": "5h ago",
            "type": "Symposium",
            "title": "Deccani Miniature Painting Restoration",
            "snippet": "International conservators discussing mineral pigment analysis of 16th-century manuscripts."
        }
    },

    # --- GANDIPET, KOKAPET & LAKEFRONT RETREATS ---
    {
        "id": "the-lakefront-pavilion-gandipet",
        "name": "The Lakefront Pavilion (Gandipet)",
        "tagline": "Open-air architecture pavilion and design retreat overlooking the Osman Sagar reservoir.",
        "category": "coworking_maker",
        "category_label": "Design Pavilion & Creative Retreat",
        "neighborhood": "Gandipet & Lakefront",
        "zone": "gandipet-lakefront",
        "address": "Gandipet Main Road, Near Osman Sagar Bund, Hyderabad 500075",
        "coordinates": {"lat": 17.3821, "lng": 78.3012},
        "vibe_tags": ["Lakefront Breeze", "Exposed Timber & Concrete", "Weekend Design Retreat", "Sunset Brainstorming"],
        "price_tier": "₹₹₹",
        "hours": "07:00 AM – 09:30 PM",
        "peak_creative_hours": "04:30 PM – 07:30 PM (Sunset)",
        "hiring_status": "Open for Collabs",
        "contacts": {
            "primary_person": "Vikram Dev",
            "primary_role": "Managing Architect & Partner",
            "phone": "+91 98480 99881",
            "whatsapp": "+919848099881",
            "email": "retreat@lakefrontpavilion.in",
            "instagram": "@lakefrontpavilion",
            "instagram_url": "https://instagram.com/lakefrontpavilion",
            "website": "https://lakefrontpavilion.in",
            "secondary_person": "Community Lead: Rohini Reddy"
        },
        "dossier": {
            "about": "Designed with deep overhangs, rammed-earth walls, and reclaimed teakwood decks, The Lakefront Pavilion overlooks the tranquil waters of Gandipet. It has become the premier weekend escape for Hyderabad's creative directors holding off-sites, portfolio reviews, and sprint planning.",
            "insider_tip": "Book the sunset deck between 05:00 PM and 07:00 PM. The breeze off the reservoir paired with French press coffee clears mental fatigue.",
            "amenities": ["Rammed Earth Architecture", "Sunset Deck", "High-Speed Mesh Wi-Fi", "Dedicated Off-Site Workrooms", "Catering Service"]
        },
        "latest_drop": {
            "timestamp": "1h ago",
            "type": "Design Retreat",
            "title": "Hyderabad Creative Directors Guild Offsite",
            "snippet": "Quarterly leadership salon on AI workflows and physical craft integration."
        }
    },
    {
        "id": "seta-lake-house-kokapet",
        "name": "Seta Lake House",
        "tagline": "Minimalist Scandinavian-meets-Deccan cafe and culinary concept store on the lake.",
        "category": "cafe",
        "category_label": "Minimalist Lake Cafe",
        "neighborhood": "Gandipet & Lakefront",
        "zone": "gandipet-lakefront",
        "address": "Kokapet Golden Mile Road, Near Neopolis, Hyderabad 500075",
        "coordinates": {"lat": 17.4012, "lng": 78.3245},
        "vibe_tags": ["Scandinavian Minimalist", "Lake Breeze", "Artisanal Gelato & Pastry", "High Aesthetic"],
        "price_tier": "₹₹₹",
        "hours": "09:00 AM – 11:00 PM",
        "peak_creative_hours": "04:00 PM – 08:00 PM",
        "hiring_status": "Walk-ins Welcome",
        "contacts": {
            "primary_person": "Alankrita Rao",
            "primary_role": "Founder & Creative Lead",
            "phone": "+91 91000 44550",
            "whatsapp": "+919100044550",
            "email": "hello@setalakehouse.com",
            "instagram": "@setalakehouse",
            "instagram_url": "https://instagram.com/setalakehouse",
            "website": "https://setalakehouse.com",
            "secondary_person": "Pastry Head: Chef Lucas M."
        },
        "dossier": {
            "about": "Seta combines serene white-washed minimalism, water reflections, and lush foliage. Situated along the rapidly developing Kokapet Neopolis corridor, it offers an architectural refuge for creatives seeking stillness away from city traffic.",
            "insider_tip": "The outdoor floating deck tables have undisturbed panoramic water views. Try their Pistachio Brioche and cold extracted cascara.",
            "amenities": ["Floating Water Deck", "Natural Light Studio", "Electric Car Fast Chargers", "Artisan Bakery"]
        },
        "latest_drop": {
            "timestamp": "2h ago",
            "type": "Art Showcase",
            "title": "Minimalist Ceramics & Flora Pop-Up",
            "snippet": "Ceramic vases paired with indigenous Deccan wild flora by Studio Mrinmoy."
        }
    }
]

with open('/Users/py/.gemini/antigravity/scratch/hyderabad-creative-map/data/places.json', 'w', encoding='utf-8') as f:
    json.dump(places, f, indent=2, ensure_ascii=False)

print(f"Generated data/places.json with {len(places)} curated creative places!")

extra_places = [
    {
        "id": "sabyasachi-flagship-banjara",
        "name": "Sabyasachi Hyderabad Flagship",
        "tagline": "Opulent restoration atelier, Persian carpets, and museum-grade heritage couture.",
        "category": "brand_fashion",
        "category_label": "Haute Couture & Heritage Architecture",
        "neighborhood": "Banjara Hills",
        "zone": "jubilee-banjara",
        "address": "Plot 14, Road No. 10, Banjara Hills, Hyderabad 500034",
        "coordinates": {"lat": 17.4305, "lng": 78.4342},
        "vibe_tags": ["Museum Aesthetics", "Antique Oil Paintings", "Brass Chandeliers", "Deccani Grandeur"],
        "price_tier": "₹₹₹₹",
        "hours": "11:00 AM – 07:30 PM (By Appointment & Walk-in)",
        "peak_creative_hours": "02:00 PM – 05:30 PM",
        "hiring_status": "Walk-ins Welcome",
        "contacts": {
            "primary_person": "Sabyasachi Mukherjee",
            "primary_role": "Founder & Creative Director",
            "phone": "+91 40 4014 9900",
            "whatsapp": "+919830012345",
            "email": "hyderabad@sabyasachi.com",
            "instagram": "@sabyasachiofficial",
            "instagram_url": "https://instagram.com/sabyasachiofficial",
            "website": "https://sabyasachi.com",
            "secondary_person": "Store Director: Radhika Sen"
        },
        "dossier": {
            "about": "Spanning over 14,000 square feet across a restored Banjara Hills mansion, Sabyasachi's Hyderabad atelier is curated with hand-knotted Persian rugs, vintage Tanjore paintings, Dutch Delft tiles, and custom brass vitrines. It represents the pinnacle of experiential retail architecture in South Asia.",
            "insider_tip": "Look up at the hand-painted gold-leaf ceiling cornices inspired by the Chowmahalla Palace banquet hall. The jewelry salon in the inner chamber is breathtaking.",
            "amenities": ["VIP Styling Suites", "Museum-Grade Lighting", "Architectural Restoration", "Valet Parking"]
        },
        "latest_drop": {
            "timestamp": "1h ago",
            "type": "Couture Preview",
            "title": "The Nizami Heritage Jewelry Suite",
            "snippet": "Uncut Colombian emeralds set in 22k gold inspired by Golconda royal archives."
        }
    },
    {
        "id": "elahe-urban-banjara",
        "name": "Elahe Urban",
        "tagline": "Experimental luxury concept store showcasing contemporary Indian fashion innovators.",
        "category": "brand_fashion",
        "category_label": "Avant-Garde Fashion & Design",
        "neighborhood": "Banjara Hills",
        "zone": "jubilee-banjara",
        "address": "Road No. 10, Beside City Center, Banjara Hills, Hyderabad 500034",
        "coordinates": {"lat": 17.4278, "lng": 78.4425},
        "vibe_tags": ["Avant-Garde Silhouettes", "Curated Ateliers", "Modern Textiles", "Sculptural Racks"],
        "price_tier": "₹₹₹₹",
        "hours": "11:00 AM – 08:00 PM",
        "peak_creative_hours": "03:00 PM – 06:30 PM",
        "hiring_status": "Open for Collabs",
        "contacts": {
            "primary_person": "Smita Shroff",
            "primary_role": "Founder & Chief Curator",
            "phone": "+91 40 2335 0134",
            "whatsapp": "+919849066551",
            "email": "elahehyderabad@gmail.com",
            "instagram": "@elaheofficial",
            "instagram_url": "https://instagram.com/elaheofficial",
            "website": "https://elahe.in",
            "secondary_person": "Creative Buyer: Riya Patel"
        },
        "dossier": {
            "about": "Elahe Urban bridges high-end Indian design with urban experimental aesthetics. Featuring contemporary silhouettes from designers like Bodice, Pero, Rimzim Dadu, and Payal Khandwala, the concrete-and-fluted-glass interior is a magnet for stylists and visual artists.",
            "insider_tip": "The accessories corridor features handcrafted artisanal jewelry and sculptural leather bags that are rarely seen elsewhere in the country.",
            "amenities": ["Stylist Consultations", "Concrete Architectural Space", "Valet Parking"]
        },
        "latest_drop": {
            "timestamp": "3h ago",
            "type": "Designer Trunk Show",
            "title": "Bodice Experimental Tailoring Trunk Show",
            "snippet": "Architectural pleated wool and organic cotton separates with designer Ruchika Sachdeva."
        }
    },
    {
        "id": "toffee-coffee-roasters-banjara",
        "name": "Toffee Coffee Roasters",
        "tagline": "Micro-roastery championing micro-lot estate transparency and experimental fermentation.",
        "category": "cafe",
        "category_label": "Specialty Micro-Roastery",
        "neighborhood": "Banjara Hills",
        "zone": "jubilee-banjara",
        "address": "Road No. 12, MLA Colony, Banjara Hills, Hyderabad 500034",
        "coordinates": {"lat": 17.4211, "lng": 78.4390},
        "vibe_tags": ["Micro-lot Estates", "Experimental Fermentation", "Espresso Bar", "Quiet Courtyard"],
        "price_tier": "₹₹",
        "hours": "08:30 AM – 11:00 PM",
        "peak_creative_hours": "09:30 AM – 12:30 PM",
        "hiring_status": "Hiring Creatives",
        "contacts": {
            "primary_person": "Aditya Goel",
            "primary_role": "Founder & Green Coffee Buyer",
            "phone": "+91 97111 44552",
            "whatsapp": "+919711144552",
            "email": "connect@toffeecoffeeroasters.com",
            "instagram": "@toffeecoffeeroasters",
            "instagram_url": "https://instagram.com/toffeecoffeeroasters",
            "website": "https://toffeecoffeeroasters.com",
            "secondary_person": "Head of Roasting: Kunal M."
        },
        "dossier": {
            "about": "Toffee Coffee Roasters approaches coffee as an artisanal harvest. Featuring their custom Dutch Giesen roaster visible through floor-to-ceiling glass, patrons can watch green coffee beans transform into fragrant roasted perfection.",
            "insider_tip": "Order their Whiskey Barrel-Aged Cold Brew or the Honey-Processed Shevaroys pour-over. Take home freshly roasted whole beans ground to your brew method.",
            "amenities": ["Giesen Roaster Display", "Custom Grind Bar", "Outdoor Tree Seating", "High-Speed Wi-Fi"]
        },
        "latest_drop": {
            "timestamp": "4h ago",
            "type": "New Roast",
            "title": "Kerehaklu Estate Carbonic Maceration",
            "snippet": "Limited 50-bag roast profile featuring bright blackcurrant and dark plum tasting notes."
        }
    },
    {
        "id": "gallery-78-madhapur",
        "name": "Gallery 78 Contemporary",
        "tagline": "Experimental art incubator championing new media, printmaking, and installation art.",
        "category": "art_culture",
        "category_label": "New Media Art Incubator",
        "neighborhood": "Madhapur & Hitec City",
        "zone": "madhapur-hitec",
        "address": "Opposite Durgam Cheruvu Lake Promenade, Madhapur, Hyderabad 500081",
        "coordinates": {"lat": 17.4385, "lng": 78.3912},
        "vibe_tags": ["Interactive Installations", "Sound Art", "Young Contemporaries", "Lake Breeze"],
        "price_tier": "₹₹",
        "hours": "11:00 AM – 07:30 PM (Closed Mondays)",
        "peak_creative_hours": "04:00 PM – 07:00 PM",
        "hiring_status": "Hosting Popups",
        "contacts": {
            "primary_person": "Shalini Reddy",
            "primary_role": "Founder & Artistic Director",
            "phone": "+91 98490 88771",
            "whatsapp": "+919849088771",
            "email": "curate@gallery78.in",
            "instagram": "@gallery78_hyd",
            "instagram_url": "https://instagram.com/gallery78_hyd",
            "website": "https://gallery78.in",
            "secondary_person": "Program Manager: Nitin Rao"
        },
        "dossier": {
            "about": "Located a stone's throw from the Durgam Cheruvu lake bridge, Gallery 78 was founded to support boundary-pushing contemporary artists working with video art, kinetic sculpture, and generative soundscapes.",
            "insider_tip": "Check out their underground black-box video installation vault. It offers immersive 360-degree sound projection for digital media artists.",
            "amenities": ["Black-Box Video Vault", "Sound Art Rigging", "Terrace Cafe", "Artist Studio Space"]
        },
        "latest_drop": {
            "timestamp": "5h ago",
            "type": "New Exhibition",
            "title": "Subterranean Deccan: Granite & Code",
            "snippet": "Kinetic robotic sculpture and sound installation exploring the ancient granites of Telangana."
        }
    },
    {
        "id": "subko-coffee-hitec-city",
        "name": "Subko Specialty Coffee & Craft Bakehouse",
        "tagline": "Direct-trade South Asian specialty coffee, bean-to-bar cacao, and layered sourdough pastries.",
        "category": "cafe",
        "category_label": "Craft Coffee & Cacao Atelier",
        "neighborhood": "Madhapur & Hitec City",
        "zone": "madhapur-hitec",
        "address": "Ground Floor, Skyview Tower 10, Hitec City, Hyderabad 500081",
        "coordinates": {"lat": 17.4410, "lng": 78.3790},
        "vibe_tags": ["Single Estate Cacao", "Direct Trade South Asia", "Sourdough Croissanterie", "Precision Espresso"],
        "price_tier": "₹₹₹",
        "hours": "08:00 AM – 11:00 PM",
        "peak_creative_hours": "09:00 AM – 12:30 PM & 03:30 PM – 06:30 PM",
        "hiring_status": "Hiring Creatives",
        "contacts": {
            "primary_person": "Rahul Reddy",
            "primary_role": "Founder & Creative Visionary",
            "phone": "+91 22 4978 2345",
            "whatsapp": "+919820011223",
            "email": "namaste@subko.coffee",
            "instagram": "@subkocoffee",
            "instagram_url": "https://instagram.com/subkocoffee",
            "website": "https://subko.coffee",
            "secondary_person": "Hyderabad Lead Barista: Karthik M."
        },
        "dossier": {
            "about": "Subko ('From the subcontinent') revolutionized specialty coffee and cacao across South Asia. Their Hyderabad space pairs raw brick and brass accents with single-estate pour-overs from Karnataka and Meghalaya alongside bean-to-bar craft chocolates made with native cacao.",
            "insider_tip": "The Twice-Baked Almond Cardamom Croissant paired with a Cortado made with Kerehaklu Estate beans is legendary.",
            "amenities": ["Bean-to-Bar Cacao Pod", "Sourdough Bakehouse Display", "Precision Espresso Bar", "High-Speed Wi-Fi"]
        },
        "latest_drop": {
            "timestamp": "35m ago",
            "type": "Cacao Release",
            "title": "Anaerobic Fermented Idukki Cacao Bar",
            "snippet": "Single-estate 72% dark chocolate bar with naturally occurring passionfruit notes."
        }
    },
    {
        "id": "dsource-creative-lab",
        "name": "D'source Design Lab & Archive",
        "tagline": "Multidisciplinary design research hub, Indian typography lab, and craft documentation studio.",
        "category": "design_studio",
        "category_label": "Design Research & Typography Lab",
        "neighborhood": "Jubilee Hills",
        "zone": "jubilee-banjara",
        "address": "Road No. 36, Near Jubilee Hills Check Post, Hyderabad 500033",
        "coordinates": {"lat": 17.4312, "lng": 78.4145},
        "vibe_tags": ["Indic Typography", "Craft Documentation", "Design Archive", "Material Culture"],
        "price_tier": "₹₹₹",
        "hours": "10:00 AM – 06:30 PM (Mon–Fri)",
        "peak_creative_hours": "11:30 AM – 04:30 PM",
        "hiring_status": "Studio Residencies",
        "contacts": {
            "primary_person": "Prof. Ravi Poovaiah",
            "primary_role": "Principal Mentor & Design Scholar",
            "phone": "+91 40 2355 4499",
            "whatsapp": "+919820099887",
            "email": "research@dsource.in",
            "instagram": "@dsourcedesign",
            "instagram_url": "https://instagram.com/dsourcedesign",
            "website": "https://dsource.in",
            "secondary_person": "Typography Lead: Sneha G."
        },
        "dossier": {
            "about": "D'source is a national treasure for design research and education in India. Their Hyderabad studio focuses on vernacular signage documentation, Telugu and Dakhni type design, and archiving indigenous rural craft techniques.",
            "insider_tip": "Students and practicing designers can access their rare typography specimen archives by scheduling a reference visit with the archivist.",
            "amenities": ["Letterpress Workshop", "Type Specimen Vault", "Document Scanner Suite", "Reference Reading Room"]
        },
        "latest_drop": {
            "timestamp": "7h ago",
            "type": "Type Release",
            "title": "Nizam Sans: Open Source Bilingual Typeface",
            "snippet": "New open-source variable font pairing classical Naskh Urdu calligraphy with geometric Latin letterforms."
        }
    },
    {
        "id": "badshahi-ashurkhana-heritage",
        "name": "Badshahi Ashurkhana Tilework Atelier",
        "tagline": "400-year-old Persian enameled mosaic tilework masterpiece commissioned by Mohammed Quli Qutb Shah.",
        "category": "heritage_icon",
        "category_label": "Qutb Shahi Enameled Architectural Monument",
        "neighborhood": "Old City & Charminar",
        "zone": "old-city-charminar",
        "address": "Near Madina Circle, Pathar Gatti, Old City, Hyderabad 500002",
        "coordinates": {"lat": 17.3685, "lng": 78.4772},
        "vibe_tags": ["Persian Mosaic Tiles", "400 Years of Glaze", "Qutb Shahi Masterwork", "Calligraphic Wonder"],
        "price_tier": "₹",
        "hours": "09:00 AM – 06:00 PM (Free Public Access)",
        "peak_creative_hours": "09:30 AM – 12:00 PM (Morning Sun)",
        "hiring_status": "Walk-ins Welcome",
        "contacts": {
            "primary_person": "Mir Abbas Ali Moosvi",
            "primary_role": "Hereditary Mutawalli & Custodian",
            "phone": "+91 98480 77112",
            "whatsapp": "+919848077112",
            "email": "heritage@ashurkhana.org",
            "instagram": "@badshahiashurkhana",
            "instagram_url": "https://instagram.com/badshahiashurkhana",
            "website": "https://heritage.telangana.gov.in",
            "secondary_person": "Conservationist: Dr. N. Taher"
        },
        "dossier": {
            "about": "Constructed in 1594 CE, the Badshahi Ashurkhana houses the finest surviving enameled tile mosaics outside of Isfahan. Intricate floral arabesques, Quranic calligraphy, and deep cobalt, turquoise, and mustard glazes have retained their brilliant luster for over four centuries.",
            "insider_tip": "Visit on a bright morning when angled sunlight illuminates the south wall mosaics. Study how the Qutb Shahi artisans used interlocking botanical motifs without single repeating molds.",
            "amenities": ["Centuries-Old Tilework", "Courtyard", "Historical Guidance", "Free Entry"]
        },
        "latest_drop": {
            "timestamp": "8h ago",
            "type": "Conservation Walk",
            "title": "Deciphering Persian Calligraphy in Glaze",
            "snippet": "Guided curatorial walk on deciphering 16th-century enameled Thuluth script."
        }
    },
    {
        "id": "shadab-heritage-hall-old-city",
        "name": "Hotel Shadab Heritage Hall",
        "tagline": "The soul of Dakhni culinary craft, Nizami biryani, and dawn Nahari simmering.",
        "category": "heritage_icon",
        "category_label": "Culinary Heritage Institution",
        "neighborhood": "Old City & Charminar",
        "zone": "old-city-charminar",
        "address": "Plot 21, High Court Road, Madina Circle, Ghansi Bazaar, Hyderabad 500002",
        "coordinates": {"lat": 17.3698, "lng": 78.4755},
        "vibe_tags": ["Dum Biryani Craft", "Zaffrani Nahari at 05:30 AM", "Historic Writers Salon", "Old City Life"],
        "price_tier": "₹₹",
        "hours": "05:00 AM – 01:00 AM",
        "peak_creative_hours": "05:30 AM – 07:30 AM (Dawn Nahari) & 01:00 PM – 03:00 PM (Dum Biryani)",
        "hiring_status": "Walk-ins Welcome",
        "contacts": {
            "primary_person": "Umar Farooq",
            "primary_role": "Managing Director & Culinary Custodian",
            "phone": "+91 40 2456 5949",
            "whatsapp": "+919849033399",
            "email": "hotelshadab@gmail.com",
            "instagram": "@hotelshadab_hyd",
            "instagram_url": "https://instagram.com/hotelshadab_hyd",
            "website": "https://hotelshadab.com",
            "secondary_person": "Ustad-e-Bawarchi: Ustad Mohsin"
        },
        "dossier": {
            "about": "Standing near the High Court since the mid-20th century, Shadab is an institution where cooking is an unbroken ancestral art. Generations of Hyderabad poets, painters, and judges have gathered on its upper air-conditioned verandahs discussing civil matters and culture over fragrant dum biryani.",
            "insider_tip": "For early risers and night-shift creatives, visit at 05:30 AM for Nahari and Char-Koni Kulcha. The slow-simmered bone broth with fresh ginger matchsticks has no parallel.",
            "amenities": ["Historic Dining Hall", "Air-Conditioned Upper Salon", "Early Morning Service", "Traditional Wood Fire Deg Cooking"]
        },
        "latest_drop": {
            "timestamp": "9h ago",
            "type": "Culinary Tradition",
            "title": "Winter Nahari Season Launch",
            "snippet": "Simmered 12 hours on copper cauldrons with 21 secret botanical spices."
        }
    },
    {
        "id": "e11even-bakehouse-sainikpuri",
        "name": "E11even Cafe & Bakehouse",
        "tagline": "Boutique French pastry atelier, artisan sourdough, and slow mornings in leafy Sainikpuri.",
        "category": "cafe",
        "category_label": "Artisan Pastry & Coffee",
        "neighborhood": "Sainikpuri & Secunderabad",
        "zone": "secunderabad-sainikpuri",
        "address": "Plot 11, Sector A, Vayupuri, Sainikpuri, Secunderabad 500094",
        "coordinates": {"lat": 17.4851, "lng": 78.5398},
        "vibe_tags": ["Slow Mornings", "French Brioche & Tarts", "Sunlit Glass Windows", "Deep Creative Reading"],
        "price_tier": "₹₹",
        "hours": "09:00 AM – 10:30 PM",
        "peak_creative_hours": "10:00 AM – 01:00 PM",
        "hiring_status": "Walk-ins Welcome",
        "contacts": {
            "primary_person": "Natasha David",
            "primary_role": "Head Baker & Founder",
            "phone": "+91 91211 44550",
            "whatsapp": "+919121144550",
            "email": "e11evenbakehouse@gmail.com",
            "instagram": "@e11evenbakehouse",
            "instagram_url": "https://instagram.com/e11evenbakehouse",
            "website": "https://e11evenbakehouse.com",
            "secondary_person": "Coffee Lead: Joshua K."
        },
        "dossier": {
            "about": "E11even is an oasis of calm along the tree-lined avenues of Vayupuri. With warm birchwood interiors, a dedicated pastry showcase, and slow jazz on the speakers, it provides the perfect backdrop for long writing sessions and sketchbook journaling.",
            "insider_tip": "Their Lemon Meringue Tart and Cinnamon Babka knot are made in micro-batches daily. Pair with an iced aeropress.",
            "amenities": ["Quiet Work Atmosphere", "Air Conditioned", "Specialty Coffee", "Power Plugs"]
        },
        "latest_drop": {
            "timestamp": "5h ago",
            "type": "Fresh Bake",
            "title": "Wild Honey & Sea Salt Babka",
            "snippet": "New slow-proofed brioche babka laced with Nilgiri wild forest honey."
        }
    },
    {
        "id": "clayworks-studio-gandipet",
        "name": "Clayworks Studio & Permaculture Lab",
        "tagline": "Biophilic pottery studio, rammed-earth workshop, and design sustainability think-tank.",
        "category": "coworking_maker",
        "category_label": "Pottery & Biophilic Design Lab",
        "neighborhood": "Gandipet & Lakefront",
        "zone": "gandipet-lakefront",
        "address": "Near Chilkur Reserve Forest, Gandipet Road, Hyderabad 500075",
        "coordinates": {"lat": 17.3750, "lng": 78.2910},
        "vibe_tags": ["Hand-Thrown Ceramics", "Electric & Wood Kilns", "Permaculture Garden", "Tactile Making"],
        "price_tier": "₹₹₹",
        "hours": "09:30 AM – 06:00 PM (Tue–Sun)",
        "peak_creative_hours": "10:00 AM – 02:00 PM",
        "hiring_status": "Studio Residencies",
        "contacts": {
            "primary_person": "Devika Narain",
            "primary_role": "Master Ceramist & Founder",
            "phone": "+91 98490 11990",
            "whatsapp": "+919849011990",
            "email": "workshops@clayworkshyd.com",
            "instagram": "@clayworks_hyd",
            "instagram_url": "https://instagram.com/clayworks_hyd",
            "website": "https://clayworkshyd.com",
            "secondary_person": "Studio Assistant: Anand Kumar"
        },
        "dossier": {
            "about": "Surrounded by mango orchards and organic farm terraces, Clayworks is Hyderabad's premier ceramic arts studio. Featuring 10 electric pottery wheels, a gas reduction kiln, and a wood-fired anagama kiln, it hosts residencies for industrial designers and sculptors exploring clay.",
            "insider_tip": "Book their weekend 2-day Wheel Throwing Intensive. Working with natural local red clay under the shade of neem trees resets modern digital burnout.",
            "amenities": ["10 Shimpo Pottery Wheels", "Anagama Wood Kiln", "Clay Glaze Testing Lab", "Organic Farm Cafe", "Open Terraces"]
        },
        "latest_drop": {
            "timestamp": "1h ago",
            "type": "Residency Call",
            "title": "Winter Ceramic Resident Fellowship 2026",
            "snippet": "Fully funded 4-week residency for 2 sculptors working with Telangana indigenous clays."
        }
    }
]

places.extend(extra_places)

with open('/Users/py/.gemini/antigravity/scratch/hyderabad-creative-map/data/places.json', 'w', encoding='utf-8') as f:
    json.dump(places, f, indent=2, ensure_ascii=False)

print(f"Dataset successfully compiled with {len(places)} total places across all Hyderabad zones!")
