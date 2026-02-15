"""
SEO Content — Service pages, location pages, and FAQ data.

Each service page targets specific keywords people search on Google.
Each location page captures "[service] in [city]" searches.
FAQ schema markup gets you featured snippets in search results.
"""

# === Service Pages ===
# Each page targets a primary keyword + related long-tail keywords

SERVICE_PAGES = [
    {
        "slug": "landscaping",
        "name": "Landscaping",
        "page_title": "Professional Landscaping in New Braunfels, TX",
        "h1": "Landscaping Services in New Braunfels",
        "meta_description": "Professional landscaping design and installation in New Braunfels, TX. Custom landscapes, flower beds, tree planting, drainage solutions. Free estimates from Brewer Lawn Designs.",
        "tagline": "Custom landscape design and installation for homes and businesses",
        "hero_image": "https://images.unsplash.com/photo-1585320806297-9794b3e4eeae?w=1600&q=80",
        "gallery_images": [
            "https://images.unsplash.com/photo-1585320806297-9794b3e4eeae?w=600&q=80",
            "https://images.unsplash.com/photo-1558904541-efa843a96f01?w=600&q=80",
            "https://images.unsplash.com/photo-1416879595882-3373a0480b5b?w=600&q=80",
            "https://images.unsplash.com/photo-1600573472592-401b489a3cdc?w=600&q=80",
        ],
        "content": """
            <h2>Professional Landscaping in New Braunfels, TX</h2>
            <p>Brewer Lawn Designs delivers professional landscaping services throughout New Braunfels and the surrounding Texas Hill Country. Whether you need a complete landscape overhaul or targeted improvements to your flower beds, trees, and outdoor living spaces, our team brings years of experience and a commitment to quality craftsmanship.</p>

            <h3>Our Landscaping Services Include</h3>
            <ul>
                <li>Custom landscape design tailored to your property and style</li>
                <li>Flower bed installation, renovation, and seasonal rotations</li>
                <li>Tree and shrub planting, including native Texas species</li>
                <li>Drainage solutions and grading to protect your property</li>
                <li>Xeriscaping and drought-tolerant landscape options</li>
                <li>Outdoor lighting design and installation</li>
                <li>Irrigation system design for new landscapes</li>
            </ul>

            <h3>Why Choose Brewer Lawn Designs for Landscaping?</h3>
            <p>We understand the unique challenges of landscaping in the Texas Hill Country. From the rocky limestone soil to the hot summers and unpredictable weather, our team knows which plants thrive here and how to design landscapes that look great year-round while conserving water. Every project starts with a free on-site consultation where we listen to your vision and provide a detailed estimate.</p>

            <h3>Landscaping for New Braunfels Homes and Businesses</h3>
            <p>From brand-new construction homes that need complete landscape packages to established properties looking for a refresh, we handle projects of all sizes. Our commercial landscaping clients include HOAs, apartment complexes, retail centers, and office buildings throughout Comal and Guadalupe counties.</p>
        """,
        "benefits": [
            {"title": "Free On-Site Consultation", "text": "We visit your property, discuss your vision, and provide a detailed estimate at no cost."},
            {"title": "Native Plant Expertise", "text": "We know which plants thrive in the Texas Hill Country climate and rocky soil."},
            {"title": "Full-Service Installation", "text": "From design to installation to cleanup, we handle every step of the process."},
        ],
        "faqs": [
            {"q": "How much does landscaping cost in New Braunfels?", "a": "Landscaping costs in New Braunfels vary depending on the scope of the project. Basic flower bed installation typically starts around $500, while full landscape designs for a typical residential property range from $2,000 to $10,000+. We provide free on-site estimates for every project."},
            {"q": "What is the best time of year to landscape in Texas?", "a": "Fall (September through November) is the ideal time for landscaping in Central Texas. The cooler temperatures and fall rains help new plants establish roots before the summer heat. Spring (March through May) is also a good time, though you will need to water more frequently as summer approaches."},
            {"q": "Do you offer landscaping design services?", "a": "Yes, Brewer Lawn Designs offers complete landscape design services. We work with you to create a custom design that fits your property, style, and budget. Our designs consider factors like sun exposure, soil conditions, drainage, and water conservation."},
            {"q": "What plants grow best in New Braunfels?", "a": "Native and adapted plants that thrive in New Braunfels include Texas Sage, Esperanza, Lantana, Mexican Feathergrass, Live Oak, Texas Mountain Laurel, and Salvia. These plants are drought-tolerant and well-suited to the rocky limestone soil of the Texas Hill Country."},
        ],
    },
    {
        "slug": "hardscaping",
        "name": "Hardscaping",
        "page_title": "Hardscaping Services in New Braunfels, TX",
        "h1": "Hardscaping & Outdoor Living in New Braunfels",
        "meta_description": "Expert hardscaping in New Braunfels, TX. Patios, walkways, retaining walls, outdoor kitchens, fire pits. Quality stone and concrete work by Brewer Lawn Designs.",
        "tagline": "Patios, walkways, retaining walls, and outdoor living spaces",
        "hero_image": "https://images.unsplash.com/photo-1600585154340-be6161a56a0c?w=1600&q=80",
        "gallery_images": [
            "https://images.unsplash.com/photo-1600585154340-be6161a56a0c?w=600&q=80",
            "https://images.unsplash.com/photo-1564013799919-ab600027ffc6?w=600&q=80",
            "https://images.unsplash.com/photo-1600607687939-ce8a6c25118c?w=600&q=80",
            "https://images.unsplash.com/photo-1600566753190-17f0baa2a6c3?w=600&q=80",
        ],
        "content": """
            <h2>Expert Hardscaping in New Braunfels, TX</h2>
            <p>Transform your outdoor space with professional hardscaping from Brewer Lawn Designs. We design and build stunning patios, walkways, retaining walls, outdoor kitchens, and fire features that extend your living space and increase your property value.</p>

            <h3>Hardscaping Services We Offer</h3>
            <ul>
                <li>Paver patios and natural stone patios</li>
                <li>Walkways and garden paths</li>
                <li>Retaining walls and decorative walls</li>
                <li>Outdoor kitchens and BBQ areas</li>
                <li>Fire pits and fireplaces</li>
                <li>Pool decks and surrounding hardscape</li>
                <li>Driveways and entrance features</li>
                <li>Steps, stairs, and elevated platforms</li>
            </ul>

            <h3>Built to Last in the Texas Climate</h3>
            <p>Central Texas soil movement and temperature swings can wreak havoc on poorly installed hardscaping. Our team understands the local soil conditions and uses proper base preparation, drainage, and materials to ensure your hardscape investment lasts for decades. We work with natural stone, pavers, flagstone, limestone, and concrete to create beautiful, durable outdoor features.</p>
        """,
        "benefits": [
            {"title": "Quality Materials", "text": "We use premium pavers, natural stone, and flagstone that stand up to the Texas climate."},
            {"title": "Proper Foundation", "text": "Every project starts with proper base preparation and drainage to prevent shifting and settling."},
            {"title": "Custom Design", "text": "We design each project to complement your home's architecture and landscape."},
        ],
        "faqs": [
            {"q": "How much does a patio cost in New Braunfels?", "a": "Patio costs in New Braunfels depend on the material and size. Basic concrete patios start around $8-12 per square foot, while paver patios typically run $15-25 per square foot, and natural stone patios range from $20-40 per square foot. A typical 300 sq ft patio ranges from $2,400 to $12,000 installed."},
            {"q": "What is the best material for a patio in Texas?", "a": "Travertine pavers and natural limestone are popular choices for Texas patios because they stay cooler underfoot in the summer heat compared to concrete. Concrete pavers are also excellent for durability and come in a wide range of styles and colors."},
            {"q": "Do you build retaining walls?", "a": "Yes, we design and build retaining walls using natural stone, concrete blocks, and other materials. Retaining walls are often necessary in the hilly terrain around New Braunfels to manage slopes, prevent erosion, and create level areas for landscaping or outdoor living."},
        ],
    },
    {
        "slug": "lawn-mowing",
        "name": "Lawn Mowing",
        "page_title": "Lawn Mowing Service in New Braunfels, TX",
        "h1": "Reliable Lawn Mowing in New Braunfels",
        "meta_description": "Affordable, reliable lawn mowing in New Braunfels, TX. Weekly and biweekly residential and commercial mowing. Edging, trimming, blowing included. Free quotes from Brewer Lawn Designs.",
        "tagline": "Weekly and biweekly mowing for homes and businesses",
        "hero_image": "https://images.unsplash.com/photo-1734303023491-db8037a21f09?w=1600&q=80",
        "gallery_images": [
            "https://images.unsplash.com/photo-1592417817098-8fd3d9eb14a5?w=600&q=80",
            "https://images.unsplash.com/photo-1558904541-efa843a96f01?w=600&q=80",
            "https://images.unsplash.com/photo-1600585154340-be6161a56a0c?w=600&q=80",
            "https://images.unsplash.com/photo-1416879595882-3373a0480b5b?w=600&q=80",
        ],
        "content": """
            <h2>Lawn Mowing Services in New Braunfels, TX</h2>
            <p>Keep your lawn looking its best with professional mowing service from Brewer Lawn Designs. We provide reliable, consistent lawn care on a schedule that works for you, whether that is weekly mowing during the growing season or biweekly maintenance year-round.</p>

            <h3>What Is Included in Our Mowing Service</h3>
            <ul>
                <li>Professional mowing at the correct height for your grass type</li>
                <li>String trimming around fences, trees, beds, and obstacles</li>
                <li>Clean edging along sidewalks, driveways, and curbs</li>
                <li>Blowing debris off hard surfaces</li>
                <li>Consistent weekly or biweekly scheduling</li>
            </ul>

            <h3>Residential and Commercial Mowing</h3>
            <p>Whether you have a small residential yard or a large commercial property, we have the equipment and crew to handle it efficiently. Our residential clients enjoy a well-kept lawn without lifting a finger, and our commercial clients benefit from professional grounds that make a great first impression on customers and visitors.</p>

            <h3>The Right Cut for Your Grass</h3>
            <p>Different grass types need different mowing heights. Bermuda grass, which is common in New Braunfels, thrives when mowed at 1 to 1.5 inches. St. Augustine prefers 3 to 4 inches. Zoysia does well at 1 to 2 inches. Our team knows the right height for your lawn and adjusts throughout the season to keep your grass healthy and thick.</p>
        """,
        "benefits": [
            {"title": "Consistent Schedule", "text": "We show up on time, every time. Your lawn always looks its best."},
            {"title": "Complete Service", "text": "Mowing, edging, trimming, and blowing are all included in every visit."},
            {"title": "Fair Pricing", "text": "Simple, transparent pricing with no hidden fees. Most residential lawns start at $35-50 per mow."},
        ],
        "faqs": [
            {"q": "How much does lawn mowing cost in New Braunfels?", "a": "Most residential lawn mowing in New Braunfels costs between $35 and $65 per visit, depending on the size of your yard and terrain. Average-sized yards (quarter acre) typically fall in the $40-50 range. We include mowing, edging, trimming, and blowing in every visit."},
            {"q": "How often should I mow my lawn in Texas?", "a": "During the growing season (April through October), most Texas lawns need weekly mowing. During the cooler months (November through March), biweekly or monthly mowing is usually sufficient. Bermuda grass grows fastest and may need mowing every 5-7 days in peak summer."},
            {"q": "Do you offer one-time mowing services?", "a": "Yes, we offer one-time mowing for special occasions, real estate showings, move-in/move-out situations, or if you just need to catch up after being away. We also offer regular weekly and biweekly service plans."},
        ],
    },
    {
        "slug": "sod-installation",
        "name": "Sod Installation",
        "page_title": "Sod Installation in New Braunfels, TX",
        "h1": "Professional Sod Installation in New Braunfels",
        "meta_description": "Professional sod installation in New Braunfels, TX. Bermuda, St. Augustine, Zoysia sod. New construction, lawn renovation, bare spots. Free estimates from Brewer Lawn Designs.",
        "tagline": "Instant green lawn with expert sod installation",
        "hero_image": "https://images.unsplash.com/photo-1558904541-efa843a96f01?w=1600&q=80",
        "gallery_images": [
            "https://images.unsplash.com/photo-1558904541-efa843a96f01?w=600&q=80",
            "https://images.unsplash.com/photo-1585320806297-9794b3e4eeae?w=600&q=80",
            "https://images.unsplash.com/photo-1416879595882-3373a0480b5b?w=600&q=80",
            "https://images.unsplash.com/photo-1592417817098-8fd3d9eb14a5?w=600&q=80",
        ],
        "content": """
            <h2>Sod Installation in New Braunfels, TX</h2>
            <p>Get a beautiful, green lawn instantly with professional sod installation from Brewer Lawn Designs. Whether you are building a new home, renovating an existing lawn, or filling in bare patches, we handle the complete sod installation process from soil preparation to the final watering.</p>

            <h3>Sod Types We Install</h3>
            <ul>
                <li><strong>Bermuda Grass</strong> — The most popular choice for full-sun lawns in Central Texas. Drought-tolerant, durable, and grows thick.</li>
                <li><strong>St. Augustine</strong> — Great for shaded and semi-shaded areas. Thick, lush blades that create a carpet-like lawn.</li>
                <li><strong>Zoysia</strong> — Low-maintenance and drought-tolerant. Creates a dense, fine-textured lawn that crowds out weeds.</li>
                <li><strong>Buffalo Grass</strong> — Native Texas grass that requires minimal water and mowing. Ideal for large properties and xeriscaping.</li>
            </ul>

            <h3>Our Sod Installation Process</h3>
            <p>A successful sod installation starts with proper soil preparation. We remove old grass and debris, grade the surface for proper drainage, amend the soil as needed, install the fresh sod in a tight pattern, and roll it for good soil contact. We then provide detailed watering instructions to help your new sod establish strong roots.</p>
        """,
        "benefits": [
            {"title": "Instant Results", "text": "Go from bare dirt to a beautiful green lawn in a single day."},
            {"title": "Proper Prep", "text": "We prepare the soil correctly so your sod establishes fast and lasts."},
            {"title": "Expert Advice", "text": "We recommend the right grass type for your sun, shade, and usage needs."},
        ],
        "faqs": [
            {"q": "How much does sod cost in New Braunfels?", "a": "Sod installation in New Braunfels typically costs between $1.50 and $3.00 per square foot installed, depending on the grass type and soil preparation needed. For a typical 5,000 sq ft yard, expect to pay $7,500 to $15,000 for a complete sod installation including soil prep."},
            {"q": "What is the best sod for New Braunfels?", "a": "Bermuda grass is the most popular choice for full-sun lawns in New Braunfels due to its heat and drought tolerance. For shaded areas, St. Augustine is the best option. Zoysia is a great all-around choice that handles both sun and partial shade well."},
            {"q": "When is the best time to install sod in Texas?", "a": "Spring (March through May) and early fall (September through October) are the best times to install sod in Central Texas. The moderate temperatures and seasonal rains help sod establish roots quickly. Summer installation is possible but requires more frequent watering."},
        ],
    },
    {
        "slug": "artificial-turf",
        "name": "Artificial Turf",
        "page_title": "Artificial Turf Installation in New Braunfels, TX",
        "h1": "Artificial Turf Installation in New Braunfels",
        "meta_description": "Professional artificial turf installation in New Braunfels, TX. Low-maintenance, drought-proof lawns, pet areas, putting greens. Free estimates from Brewer Lawn Designs.",
        "tagline": "Low-maintenance, drought-proof artificial grass solutions",
        "hero_image": "https://images.unsplash.com/photo-1600585154340-be6161a56a0c?w=1600&q=80",
        "gallery_images": [
            "https://images.unsplash.com/photo-1600585154340-be6161a56a0c?w=600&q=80",
            "https://images.unsplash.com/photo-1600607687939-ce8a6c25118c?w=600&q=80",
            "https://images.unsplash.com/photo-1600573472592-401b489a3cdc?w=600&q=80",
            "https://images.unsplash.com/photo-1564013799919-ab600027ffc6?w=600&q=80",
        ],
        "content": """
            <h2>Artificial Turf Installation in New Braunfels, TX</h2>
            <p>Save water, eliminate mowing, and enjoy a green lawn year-round with professional artificial turf installation from Brewer Lawn Designs. Modern synthetic grass looks and feels remarkably natural while requiring virtually zero maintenance.</p>

            <h3>Artificial Turf Applications</h3>
            <ul>
                <li>Full front and backyard lawn replacements</li>
                <li>Pet-friendly turf areas with drainage</li>
                <li>Putting greens and sports surfaces</li>
                <li>Pool surrounds and outdoor living areas</li>
                <li>Commercial properties and common areas</li>
                <li>Playgrounds and play areas</li>
                <li>Side yards and hard-to-mow areas</li>
            </ul>

            <h3>Why Artificial Turf Makes Sense in Texas</h3>
            <p>With water restrictions becoming more common across Central Texas and summer temperatures regularly exceeding 100 degrees, artificial turf is an increasingly smart investment. You will save hundreds of dollars per year on water, eliminate mowing and fertilizing costs, and have a lawn that looks perfect 365 days a year.</p>
        """,
        "benefits": [
            {"title": "Zero Mowing", "text": "Never mow, edge, or trim again. Your lawn always looks freshly cut."},
            {"title": "Save Water", "text": "No watering ever. Save hundreds of dollars per year on your water bill."},
            {"title": "Always Green", "text": "No brown patches, no dormancy. Your lawn looks perfect every day of the year."},
        ],
        "faqs": [
            {"q": "How much does artificial turf cost in New Braunfels?", "a": "Artificial turf installation in New Braunfels typically costs between $8 and $15 per square foot installed, depending on the turf quality and base preparation. For a typical 1,000 sq ft area, expect $8,000 to $15,000. The investment pays for itself over 5-7 years through eliminated water, mowing, and fertilizer costs."},
            {"q": "How long does artificial turf last?", "a": "Quality artificial turf lasts 15 to 25 years with minimal maintenance. Modern turf products are UV-resistant and designed to withstand the intense Texas sun without fading or degrading."},
            {"q": "Is artificial turf safe for pets?", "a": "Yes, modern artificial turf is very pet-friendly. We install turf with built-in drainage systems that handle pet waste effectively. The turf is non-toxic and easy to clean with a quick hose-down. Many pet owners prefer artificial turf because it eliminates muddy paws and dead spots from pet urine."},
        ],
    },
    {
        "slug": "concrete-masonry",
        "name": "Concrete & Masonry",
        "page_title": "Concrete & Masonry Services in New Braunfels, TX",
        "h1": "Concrete & Masonry Work in New Braunfels",
        "meta_description": "Expert concrete and masonry work in New Braunfels, TX. Driveways, pool decks, sidewalks, stone walls, stamped concrete. Quality craftsmanship by Brewer Lawn Designs.",
        "tagline": "Driveways, pool decks, sidewalks, and custom stonework",
        "hero_image": "https://images.unsplash.com/photo-1564013799919-ab600027ffc6?w=1600&q=80",
        "gallery_images": [
            "https://images.unsplash.com/photo-1564013799919-ab600027ffc6?w=600&q=80",
            "https://images.unsplash.com/photo-1600566753190-17f0baa2a6c3?w=600&q=80",
            "https://images.unsplash.com/photo-1600607687939-ce8a6c25118c?w=600&q=80",
            "https://images.unsplash.com/photo-1600585154340-be6161a56a0c?w=600&q=80",
        ],
        "content": """
            <h2>Concrete & Masonry Services in New Braunfels, TX</h2>
            <p>Brewer Lawn Designs provides professional concrete and masonry services for residential and commercial properties throughout New Braunfels and the surrounding area. From functional driveways and sidewalks to decorative stamped concrete and stone features, we deliver quality craftsmanship that lasts.</p>

            <h3>Concrete & Masonry Services</h3>
            <ul>
                <li>Concrete driveways — standard, stamped, and decorative</li>
                <li>Pool decks and cool deck coatings</li>
                <li>Sidewalks and walkways</li>
                <li>Stamped and stained concrete</li>
                <li>Stone and block walls</li>
                <li>Concrete patios and slabs</li>
                <li>Foundation repairs and mudjacking</li>
                <li>Curbing and borders</li>
            </ul>

            <h3>Quality Concrete Work for the Texas Climate</h3>
            <p>Proper concrete work in Central Texas requires understanding of how the expansive clay soils and temperature swings affect cured concrete. We use the right mix designs, reinforcement, and joint spacing to minimize cracking and ensure your concrete investment lasts for decades.</p>
        """,
        "benefits": [
            {"title": "Expert Craftsmanship", "text": "Clean, professional concrete work with proper finishing and curing."},
            {"title": "Climate-Adapted", "text": "We design for Texas soil and weather conditions to prevent cracking and heaving."},
            {"title": "Decorative Options", "text": "Stamped, stained, and exposed aggregate finishes to match your style."},
        ],
        "faqs": [
            {"q": "How much does a concrete driveway cost in New Braunfels?", "a": "A standard concrete driveway in New Braunfels typically costs $6-10 per square foot for basic concrete, and $10-18 per square foot for stamped or decorative concrete. A typical two-car driveway (400-600 sq ft) ranges from $2,400 to $10,800 depending on finish and complexity."},
            {"q": "How long does concrete last in Texas?", "a": "Properly installed and maintained concrete in Texas lasts 25-50 years. The key factors are proper base preparation, adequate thickness, appropriate reinforcement, and correct joint spacing to account for soil movement and temperature changes."},
        ],
    },
    {
        "slug": "garden-design",
        "name": "Garden Design",
        "page_title": "Garden Design Services in New Braunfels, TX",
        "h1": "Garden Design in New Braunfels",
        "meta_description": "Custom garden design in New Braunfels, TX. Native Texas gardens, flower gardens, vegetable gardens, pollinator gardens. Expert design by Brewer Lawn Designs.",
        "tagline": "Beautiful, sustainable garden design for Texas homes",
        "hero_image": "https://images.unsplash.com/photo-1585320806297-9794b3e4eeae?w=1600&q=80",
        "gallery_images": [
            "https://images.unsplash.com/photo-1585320806297-9794b3e4eeae?w=600&q=80",
            "https://images.unsplash.com/photo-1416879595882-3373a0480b5b?w=600&q=80",
            "https://images.unsplash.com/photo-1600573472592-401b489a3cdc?w=600&q=80",
            "https://images.unsplash.com/photo-1558904541-efa843a96f01?w=600&q=80",
        ],
        "content": """
            <h2>Garden Design Services in New Braunfels, TX</h2>
            <p>Create the outdoor space of your dreams with custom garden design from Brewer Lawn Designs. We specialize in designing gardens that thrive in the Texas Hill Country climate while creating beautiful, functional outdoor spaces that you will enjoy year-round.</p>

            <h3>Garden Design Options</h3>
            <ul>
                <li>Native Texas perennial gardens</li>
                <li>Color flower bed designs with seasonal rotations</li>
                <li>Pollinator and butterfly gardens</li>
                <li>Herb and vegetable garden layouts</li>
                <li>Rock gardens and xeriscaping</li>
                <li>Shade gardens for difficult areas</li>
                <li>Rain gardens for drainage management</li>
                <li>Foundation plantings and curb appeal upgrades</li>
            </ul>

            <h3>Designed for the Texas Hill Country</h3>
            <p>Our garden designs take into account the unique characteristics of the New Braunfels area: the rocky limestone soil, alkaline water, hot summers, mild winters, and variable rainfall. We select plants and design layouts that look great and perform well in these conditions, reducing maintenance and water needs.</p>
        """,
        "benefits": [
            {"title": "Climate-Smart Design", "text": "Gardens designed specifically for the Texas Hill Country environment."},
            {"title": "Low Maintenance", "text": "We choose plants and layouts that minimize ongoing care and water needs."},
            {"title": "Year-Round Color", "text": "Seasonal bloom schedules ensure your garden has color in every season."},
        ],
        "faqs": [
            {"q": "What flowers grow best in New Braunfels?", "a": "Top-performing flowers in New Braunfels include Lantana, Esperanza (Yellow Bells), Salvia, Black-Eyed Susan, Coneflower, Mexican Honeysuckle, Zinnias, and Turk's Cap. These are drought-tolerant and adapted to the Texas Hill Country climate."},
            {"q": "When should I plant a garden in New Braunfels?", "a": "Fall is the best time to plant perennials, trees, and shrubs in New Braunfels. The cooler temperatures and fall rains help plants establish roots before summer. For annuals and vegetables, plant cool-season varieties in October-November and warm-season varieties in March-April."},
        ],
    },
    {
        "slug": "landscape-maintenance",
        "name": "Landscape Maintenance",
        "page_title": "Landscape Maintenance in New Braunfels, TX",
        "h1": "Landscape Maintenance Services in New Braunfels",
        "meta_description": "Complete landscape maintenance in New Braunfels, TX. Pruning, mulching, bed maintenance, seasonal cleanup, irrigation checks. Keep your property looking great with Brewer Lawn Designs.",
        "tagline": "Keep your landscape looking its best year-round",
        "hero_image": "https://images.unsplash.com/photo-1558904541-efa843a96f01?w=1600&q=80",
        "gallery_images": [
            "https://images.unsplash.com/photo-1558904541-efa843a96f01?w=600&q=80",
            "https://images.unsplash.com/photo-1592417817098-8fd3d9eb14a5?w=600&q=80",
            "https://images.unsplash.com/photo-1585320806297-9794b3e4eeae?w=600&q=80",
            "https://images.unsplash.com/photo-1416879595882-3373a0480b5b?w=600&q=80",
        ],
        "content": """
            <h2>Landscape Maintenance in New Braunfels, TX</h2>
            <p>A beautiful landscape needs regular care to stay healthy and looking great. Brewer Lawn Designs provides complete landscape maintenance services that keep your property in top condition year-round, so you can enjoy your outdoor spaces without the work.</p>

            <h3>Our Maintenance Services</h3>
            <ul>
                <li>Tree and shrub pruning and shaping</li>
                <li>Mulch installation and bed refresh</li>
                <li>Flower bed weeding and maintenance</li>
                <li>Seasonal plant rotations and color changes</li>
                <li>Spring and fall cleanup</li>
                <li>Leaf removal</li>
                <li>Irrigation system checks and adjustments</li>
                <li>Fertilization programs</li>
            </ul>

            <h3>Maintenance Programs</h3>
            <p>We offer flexible maintenance programs to fit your needs and budget. Whether you need monthly visits for basic upkeep or weekly full-service maintenance, we will create a schedule that keeps your landscape healthy and beautiful throughout every season.</p>
        """,
        "benefits": [
            {"title": "Scheduled Service", "text": "Regular visits on a consistent schedule so your property always looks great."},
            {"title": "Seasonal Expertise", "text": "We know what your landscape needs in every season to stay healthy."},
            {"title": "Comprehensive Care", "text": "From pruning to mulching to irrigation, we handle it all."},
        ],
        "faqs": [
            {"q": "How much does landscape maintenance cost in New Braunfels?", "a": "Monthly landscape maintenance in New Braunfels typically ranges from $150 to $500 per month depending on the size of your property and level of service. This includes pruning, bed maintenance, mulching, and seasonal cleanup. Weekly mowing can be added for an additional fee."},
            {"q": "When should I mulch in New Braunfels?", "a": "The best times to mulch in New Braunfels are spring (March-April) and fall (October-November). Mulch helps retain soil moisture during the hot summer months and insulates plant roots during occasional winter freezes. Apply 2-3 inches of mulch around plants and beds."},
        ],
    },
    {
        "slug": "spring-fall-cleanup",
        "name": "Spring & Fall Cleanup",
        "page_title": "Spring & Fall Cleanup Services in New Braunfels, TX",
        "h1": "Seasonal Cleanup Services in New Braunfels",
        "meta_description": "Professional spring and fall yard cleanup in New Braunfels, TX. Leaf removal, bed cleanup, pruning, debris removal. Get your yard ready for the season with Brewer Lawn Designs.",
        "tagline": "Get your yard ready for the season",
        "hero_image": "https://images.unsplash.com/photo-1558904541-efa843a96f01?w=1600&q=80",
        "gallery_images": [
            "https://images.unsplash.com/photo-1416879595882-3373a0480b5b?w=600&q=80",
            "https://images.unsplash.com/photo-1600573472592-401b489a3cdc?w=600&q=80",
            "https://images.unsplash.com/photo-1558904541-efa843a96f01?w=600&q=80",
            "https://images.unsplash.com/photo-1592417817098-8fd3d9eb14a5?w=600&q=80",
        ],
        "content": """
            <h2>Spring & Fall Cleanup in New Braunfels, TX</h2>
            <p>Get your yard ready for the season with professional cleanup services from Brewer Lawn Designs. Our seasonal cleanups remove debris, revitalize your beds, and prepare your landscape for the growing season ahead or the winter dormancy period.</p>

            <h3>Spring Cleanup Services</h3>
            <ul>
                <li>Remove dead foliage and winter debris</li>
                <li>Cut back dormant perennials and ornamental grasses</li>
                <li>Clean and edge all bed lines</li>
                <li>Apply fresh mulch to beds</li>
                <li>Prune shrubs and small trees</li>
                <li>Inspect and test irrigation systems</li>
                <li>Apply pre-emergent weed control</li>
            </ul>

            <h3>Fall Cleanup Services</h3>
            <ul>
                <li>Leaf removal from lawn, beds, and gutters</li>
                <li>Cut back perennials for winter dormancy</li>
                <li>Remove spent annuals and install cool-season color</li>
                <li>Final pruning of shrubs and trees</li>
                <li>Winterize irrigation systems</li>
                <li>Apply fall fertilizer</li>
            </ul>
        """,
        "benefits": [
            {"title": "Complete Service", "text": "We handle every aspect of seasonal cleanup in a single visit."},
            {"title": "Prep for Success", "text": "Proper seasonal prep helps your landscape thrive in the months ahead."},
            {"title": "Curb Appeal Boost", "text": "A thorough cleanup instantly transforms the look of your property."},
        ],
        "faqs": [
            {"q": "How much does a yard cleanup cost in New Braunfels?", "a": "Seasonal yard cleanup in New Braunfels typically costs between $200 and $600 depending on the size of your property and amount of work needed. This includes debris removal, bed cleanup, pruning, and mulch application."},
            {"q": "When should I do spring cleanup in Texas?", "a": "Late February through early March is the ideal time for spring cleanup in Central Texas. This allows you to remove winter damage, cut back dormant plants, and prepare beds before the spring growth surge begins."},
        ],
    },
    {
        "slug": "commercial-landscaping",
        "name": "Commercial Landscaping",
        "page_title": "Commercial Landscaping in New Braunfels, TX",
        "h1": "Commercial Landscaping Services in New Braunfels",
        "meta_description": "Professional commercial landscaping in New Braunfels, TX. HOA maintenance, office parks, retail centers, apartment complexes. Reliable service from Brewer Lawn Designs.",
        "tagline": "Professional grounds maintenance for businesses and communities",
        "hero_image": "https://images.unsplash.com/photo-1558904541-efa843a96f01?w=1600&q=80",
        "gallery_images": [
            "https://images.unsplash.com/photo-1600607687939-ce8a6c25118c?w=600&q=80",
            "https://images.unsplash.com/photo-1600585154340-be6161a56a0c?w=600&q=80",
            "https://images.unsplash.com/photo-1564013799919-ab600027ffc6?w=600&q=80",
            "https://images.unsplash.com/photo-1600566753190-17f0baa2a6c3?w=600&q=80",
        ],
        "content": """
            <h2>Commercial Landscaping in New Braunfels, TX</h2>
            <p>First impressions matter. Brewer Lawn Designs provides professional commercial landscaping services that keep your business, HOA, or multi-property looking sharp year-round. We understand that commercial properties require reliability, consistency, and a professional appearance.</p>

            <h3>Commercial Clients We Serve</h3>
            <ul>
                <li>Homeowner Associations (HOAs) and community common areas</li>
                <li>Apartment complexes and multi-family properties</li>
                <li>Office buildings and business parks</li>
                <li>Retail centers and shopping plazas</li>
                <li>Restaurants and hospitality properties</li>
                <li>Churches and religious facilities</li>
                <li>Medical and dental offices</li>
                <li>New construction and model homes</li>
            </ul>

            <h3>Why Businesses Choose Brewer Lawn Designs</h3>
            <p>Commercial property managers and business owners choose us because we are reliable, professional, and deliver consistent results. We show up on schedule, communicate proactively, and maintain the high standards your property deserves. Our team can handle properties of all sizes, from a single office building to an entire HOA community.</p>
        """,
        "benefits": [
            {"title": "Reliable Service", "text": "Consistent scheduling and communication. We never miss a visit."},
            {"title": "Scalable", "text": "We handle properties from single buildings to large HOA communities."},
            {"title": "Professional Image", "text": "Your property always looks its best for customers and residents."},
        ],
        "faqs": [
            {"q": "Do you offer HOA landscaping in New Braunfels?", "a": "Yes, we provide comprehensive HOA landscaping services including common area mowing, entrance maintenance, seasonal color rotations, tree and shrub care, irrigation management, and more. We work directly with HOA boards and management companies to keep communities looking their best."},
            {"q": "How much does commercial landscaping cost?", "a": "Commercial landscaping costs vary based on the property size and services needed. Monthly maintenance contracts for commercial properties in the New Braunfels area typically start at $500-800 per month for smaller properties and go up from there based on acreage and service frequency. We provide custom proposals for every property."},
        ],
    },
]

# === Location Pages ===
# Each page captures "[service] in [city]" Google searches

LOCATION_PAGES = [
    {
        "slug": "new-braunfels",
        "name": "New Braunfels",
        "page_title": "Landscaping in New Braunfels, TX",
        "h1": "Landscaping Services in New Braunfels, TX",
        "meta_description": "Brewer Lawn Designs provides professional landscaping, hardscaping, lawn mowing, sod installation, and garden design in New Braunfels, TX. 5-star rated. Free estimates.",
        "hero_image": "https://images.unsplash.com/photo-1558904541-efa843a96f01?w=1600&q=80",
        "short": "Our home base. Full-service landscaping for New Braunfels homes and businesses.",
        "content": """
            <h2>Your Local Landscaping Company in New Braunfels</h2>
            <p>Brewer Lawn Designs is a New Braunfels-based landscaping company providing full-service lawn care, landscape design, hardscaping, and maintenance to homeowners and businesses throughout the city. As locals ourselves, we understand the unique landscape challenges of the Texas Hill Country and take pride in keeping our community looking beautiful.</p>

            <h3>Landscaping for New Braunfels Neighborhoods</h3>
            <p>We serve homeowners across New Braunfels, including neighborhoods like Vintage Oaks, River Chase, Gruene, Mission Hills, Landa Park area, Westpointe, and all surrounding communities. Whether you need weekly mowing, a complete landscape renovation, or anything in between, we are your local go-to landscaper.</p>

            <h3>Why New Braunfels Homeowners Choose Us</h3>
            <p>With a 5.0-star Google rating and 7 reviews, our reputation speaks for itself. We are locally owned, fully insured, and committed to delivering quality work at fair prices. Every project starts with a free on-site estimate and a conversation about your goals for your outdoor space.</p>
        """,
        "faqs": [
            {"q": "What landscaping services are available in New Braunfels?", "a": "Brewer Lawn Designs offers a complete range of landscaping services in New Braunfels including landscape design and installation, hardscaping (patios, walkways, retaining walls), lawn mowing, sod installation, artificial turf, concrete and masonry, garden design, and seasonal cleanup. We serve both residential and commercial properties."},
            {"q": "How much does lawn care cost in New Braunfels?", "a": "Lawn care costs in New Braunfels vary by service type. Weekly mowing typically runs $35-65 per visit for residential properties. Monthly landscape maintenance ranges from $150-500. Full landscape design and installation projects start around $2,000 and go up based on scope. We provide free estimates for all services."},
        ],
    },
    {
        "slug": "schertz",
        "name": "Schertz",
        "page_title": "Landscaping in Schertz, TX",
        "h1": "Landscaping Services in Schertz, TX",
        "meta_description": "Professional landscaping services in Schertz, TX. Lawn mowing, landscape design, hardscaping, sod installation. Serving Schertz homes and businesses. Free estimates from Brewer Lawn Designs.",
        "hero_image": "https://images.unsplash.com/photo-1585320806297-9794b3e4eeae?w=1600&q=80",
        "short": "Full landscaping services for Schertz homes, businesses, and communities.",
        "content": """
            <h2>Landscaping Services in Schertz, TX</h2>
            <p>Brewer Lawn Designs proudly serves homeowners and businesses in Schertz, TX with professional landscaping, lawn care, and hardscaping services. Located just minutes from our New Braunfels base, Schertz is one of our primary service areas.</p>

            <h3>Serving Schertz Neighborhoods and Businesses</h3>
            <p>We work with homeowners and property managers throughout Schertz, including communities along FM 3009, Main Street, Schertz Parkway, and all surrounding neighborhoods. Our commercial clients in Schertz include HOAs, apartment complexes, retail centers, and office buildings.</p>

            <p>As one of the fastest-growing cities in the San Antonio metro area, Schertz has seen tremendous new construction and development. We work with builders and new homeowners to design and install complete landscapes for newly built homes.</p>
        """,
        "faqs": [
            {"q": "Do you provide landscaping services in Schertz?", "a": "Yes, Schertz is one of our primary service areas. We provide the full range of landscaping services to Schertz homes and businesses including lawn mowing, landscape design, hardscaping, sod installation, artificial turf, and seasonal maintenance."},
            {"q": "How far is Brewer Lawn Designs from Schertz?", "a": "Our New Braunfels base is approximately 15 minutes from most Schertz locations. We have crews in the Schertz area regularly and can typically schedule service within a few days of your inquiry."},
        ],
    },
    {
        "slug": "cibolo",
        "name": "Cibolo",
        "page_title": "Landscaping in Cibolo, TX",
        "h1": "Landscaping Services in Cibolo, TX",
        "meta_description": "Professional landscaping in Cibolo, TX. Lawn mowing, landscape design, sod installation, hardscaping for Cibolo homes and businesses. Free estimates from Brewer Lawn Designs.",
        "hero_image": "https://images.unsplash.com/photo-1558904541-efa843a96f01?w=1600&q=80",
        "short": "Professional landscaping for Cibolo's growing community.",
        "content": """
            <h2>Landscaping Services in Cibolo, TX</h2>
            <p>Brewer Lawn Designs provides professional landscaping services to the growing community of Cibolo, TX. From new construction landscaping to ongoing lawn maintenance, we help Cibolo homeowners and businesses create and maintain beautiful outdoor spaces.</p>

            <h3>Growing with Cibolo</h3>
            <p>Cibolo is one of the fastest-growing cities in Texas, with new neighborhoods and developments popping up regularly. We work with new homeowners to design and install complete landscapes, and we provide ongoing maintenance to keep established properties looking their best. Our services cover all of Cibolo, including the Turning Stone, Deer Creek, and Cibolo Valley Ranch neighborhoods.</p>
        """,
        "faqs": [
            {"q": "Do you serve Cibolo, TX?", "a": "Yes, Cibolo is within our primary service area. We provide all of our landscaping services to Cibolo homes and businesses, including lawn mowing, landscape design and installation, hardscaping, sod installation, and seasonal maintenance."},
        ],
    },
    {
        "slug": "san-marcos",
        "name": "San Marcos",
        "page_title": "Landscaping in San Marcos, TX",
        "h1": "Landscaping Services in San Marcos, TX",
        "meta_description": "Professional landscaping in San Marcos, TX. Lawn mowing, landscape design, hardscaping, commercial landscaping. Serving San Marcos homes and businesses. Brewer Lawn Designs.",
        "hero_image": "https://images.unsplash.com/photo-1585320806297-9794b3e4eeae?w=1600&q=80",
        "short": "Full-service landscaping for San Marcos homes and businesses.",
        "content": """
            <h2>Landscaping Services in San Marcos, TX</h2>
            <p>Brewer Lawn Designs serves homeowners and businesses in San Marcos, TX with professional landscaping, lawn care, and hardscaping services. Located along the I-35 corridor between Austin and San Antonio, San Marcos is within our service area and we have crews in the area regularly.</p>

            <h3>Residential and Commercial Landscaping in San Marcos</h3>
            <p>Whether you own a home near the San Marcos River, manage a commercial property along Wonder World Drive, or oversee an apartment complex near Texas State University, Brewer Lawn Designs has the expertise and equipment to keep your property looking its best.</p>
        """,
        "faqs": [
            {"q": "Do you provide landscaping in San Marcos?", "a": "Yes, we serve San Marcos and surrounding areas. Our New Braunfels base is approximately 20 minutes from San Marcos, and we have crews in the area regularly for both residential and commercial clients."},
        ],
    },
    {
        "slug": "seguin",
        "name": "Seguin",
        "page_title": "Landscaping in Seguin, TX",
        "h1": "Landscaping Services in Seguin, TX",
        "meta_description": "Professional landscaping in Seguin, TX. Lawn mowing, landscape design, hardscaping, sod installation. Serving Seguin homes and businesses. Free estimates from Brewer Lawn Designs.",
        "hero_image": "https://images.unsplash.com/photo-1558904541-efa843a96f01?w=1600&q=80",
        "short": "Quality landscaping for Seguin homes and businesses.",
        "content": """
            <h2>Landscaping Services in Seguin, TX</h2>
            <p>Brewer Lawn Designs provides professional landscaping services to homeowners and businesses in Seguin, TX. Just east of New Braunfels along I-10, Seguin is within our regular service area and we are happy to serve this historic Texas community.</p>

            <h3>Full-Service Landscaping for Seguin</h3>
            <p>From lawn mowing and maintenance to complete landscape design and installation, we offer the full range of landscaping services to Seguin residents and businesses. Our team handles properties of all sizes, from residential lawns to commercial complexes and HOA communities.</p>
        """,
        "faqs": [
            {"q": "Do you serve Seguin, TX?", "a": "Yes, Seguin is within our service area. Located about 20 minutes east of our New Braunfels base, we provide all landscaping services to Seguin homes and businesses including mowing, landscape design, hardscaping, and maintenance."},
        ],
    },
    {
        "slug": "garden-ridge",
        "name": "Garden Ridge",
        "page_title": "Landscaping in Garden Ridge, TX",
        "h1": "Landscaping Services in Garden Ridge, TX",
        "meta_description": "Professional landscaping in Garden Ridge, TX. Lawn mowing, landscape design, hardscaping, sod installation. Serving Garden Ridge estates and properties. Brewer Lawn Designs.",
        "hero_image": "https://images.unsplash.com/photo-1600585154340-be6161a56a0c?w=1600&q=80",
        "short": "Premium landscaping for Garden Ridge estates and properties.",
        "content": """
            <h2>Landscaping Services in Garden Ridge, TX</h2>
            <p>Brewer Lawn Designs provides premium landscaping services to homeowners in Garden Ridge, TX. Known for its beautiful properties and large lots, Garden Ridge is home to some of the finest landscapes in the area, and we are proud to help maintain and enhance them.</p>

            <h3>Serving Garden Ridge's Unique Properties</h3>
            <p>Garden Ridge properties often feature large acreage, mature trees, and established landscapes that require knowledgeable, experienced care. Our team understands the unique needs of Garden Ridge properties, from managing oak wilt prevention to maintaining expansive lawns and sophisticated garden designs.</p>
        """,
        "faqs": [
            {"q": "Do you provide landscaping in Garden Ridge?", "a": "Yes, Garden Ridge is within our primary service area. We provide all landscaping services including mowing, landscape maintenance, hardscaping, and full landscape design and installation for Garden Ridge homes and properties."},
        ],
    },
    {
        "slug": "canyon-lake",
        "name": "Canyon Lake",
        "page_title": "Landscaping in Canyon Lake, TX",
        "h1": "Landscaping Services in Canyon Lake, TX",
        "meta_description": "Professional landscaping in Canyon Lake, TX. Lawn mowing, landscape design, hardscaping, sod installation. Serving Canyon Lake homes and vacation properties. Brewer Lawn Designs.",
        "hero_image": "https://images.unsplash.com/photo-1558904541-efa843a96f01?w=1600&q=80",
        "short": "Landscaping for Canyon Lake homes, cabins, and vacation properties.",
        "content": """
            <h2>Landscaping Services in Canyon Lake, TX</h2>
            <p>Brewer Lawn Designs serves homeowners and property managers in the Canyon Lake area with professional landscaping and lawn care services. Whether you have a full-time residence, a vacation home, or a rental property near the lake, we keep your outdoor spaces looking great.</p>

            <h3>Canyon Lake Landscaping Challenges</h3>
            <p>Canyon Lake properties come with unique landscaping challenges including steep terrain, rocky limestone soil, deer browsing, and the need for drought-tolerant plantings. Our team has extensive experience working with these conditions and can design landscapes that thrive in the Hill Country environment around Canyon Lake.</p>
        """,
        "faqs": [
            {"q": "Do you serve Canyon Lake?", "a": "Yes, we serve the Canyon Lake area including properties along the lake, in Canyon Lake subdivisions, and in the surrounding Hill Country. We provide lawn mowing, landscape design, hardscaping, and maintenance services for Canyon Lake homes and vacation properties."},
        ],
    },
]


def get_all_services():
    """Return a list of service dicts with slug and name for sidebar/navigation."""
    return [{"slug": s["slug"], "name": s["name"]} for s in SERVICE_PAGES]


def get_all_areas():
    """Return a list of area dicts with slug, name, and short description."""
    return [{"slug": a["slug"], "name": a["name"], "short": a.get("short", "")} for a in LOCATION_PAGES]


def get_service_page(slug: str):
    """Get a service page by slug."""
    for s in SERVICE_PAGES:
        if s["slug"] == slug:
            return s
    return None


def get_location_page(slug: str):
    """Get a location page by slug."""
    for a in LOCATION_PAGES:
        if a["slug"] == slug:
            return a
    return None
