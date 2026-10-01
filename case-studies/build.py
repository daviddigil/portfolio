# Generates all case-study pages from _template.html + the DATA list below.
# Run: python build.py
import re, os

TPL = open('_template.html', encoding='utf-8').read()

def p(*lines): return "\n        ".join('<p>'+l+'</p>' for l in lines)
def ul(*items): return '<ul>\n          ' + "\n          ".join('<li>'+i+'</li>' for i in items) + '\n        </ul>'
def stat(big, small): return f'<div><b>{big}</b><span>{small}</span></div>'
def fact(k, v): return f'<li><span>{k}</span><span>{v}</span></li>'
def stack(*items): return "".join(f'<span>{i}</span>' for i in items)
def link(label, href): return f'<a class="btn" href="{href}" target="_blank" rel="noopener">{label} ↗</a>'
def linkghost(label, href): return f'<a class="btn ghost" href="{href}" target="_blank" rel="noopener">{label} ↗</a>'

DATA = []

# ============================= DESIGN PROJECTS =============================

DATA.append(dict(
  slug="wurth-uae-eshop", section="design", section_label="Design",
  title="Würth UAE eShop", title_html="Würth UAE <em>eShop</em>",
  desc="How I led the end-to-end redesign of Würth UAE's B2B/B2C e-commerce checkout, lifting conversion by 18% through research, a Figma design system and cross-platform handoff.",
  status="Live", category="E-commerce · B2B/B2C",
  dek="A fastener and tooling wholesaler's online shop, redesigned around how trade buyers actually reorder: fast, repeatable, and trustworthy enough to move real procurement budgets online.",
  role="Senior UI/UX Designer &amp; Product Design Lead", timeline="Jul 2020 – Present", platform="Web · Responsive", client="Würth UAE",
  c1="#8c0012", c2="#e2001a", cover_text="Würth Online Shop",
  links=[link("Visit the live shop", "https://eshop.wurth.ae")],
  challenge=p(
    "Würth UAE sells tools, fasteners and industrial supplies to both trade professionals and individual buyers across the GCC. The existing checkout flow was built for a single buyer type and leaked conversions at exactly the moment it mattered most: between adding items to cart and completing payment.",
    "B2B buyers needed bulk reorder, quote requests and account-level pricing; B2C buyers needed something closer to a standard retail checkout. Serving both through one undifferentiated flow meant neither got what they needed, and usability testing showed drop-off was concentrated around cart review and payment method selection."
  ),
  approach=p(
    "I ran user research and usability testing across both buyer segments to find where the flow actually broke down, rather than guessing from analytics alone. That surfaced friction points in step count, unclear order summaries, and a lack of trust signals at the payment step.",
    "From there I mapped the end-to-end journey for both B2B and B2C paths, then designed a shared checkout shell with segment-aware steps, so the two audiences diverge only where their needs actually differ, keeping the system maintainable rather than forked into two separate codebases."
  ),
  solution=p(
    "A redesigned checkout flow with clearer order review, simplified payment selection and fewer required steps, built on a comprehensive Figma design system I built and maintained for cross-platform consistency.",
    "The design system reduced data management errors by standardising components, spacing and states across web and the teams building against it, which also improved developer handoff efficiency by 30% — designers and engineers were finally working from the same source of truth instead of redlines."
  ) + ul(
    "Segment-aware checkout steps for B2B (bulk, quotes, account pricing) and B2C (retail-style, faster path)",
    "A shared Figma design system covering components, tokens and states, used across the wider digital product",
    "Clearer cart review and payment UI informed directly by usability testing, not assumption"
  ),
  outcome_intro=p("The redesign shipped with measurable results on both the conversion and the engineering side."),
  stats=stat("18%","lift in conversion rate") + stat("30%","better dev handoff efficiency") + stat("B2B/B2C","unified checkout system"),
  outcome_extra=p("Because the design system is still the one in active use at Würth UAE, this isn't a one-off redesign — it's the foundation new features get built on, which is where the real compounding value of the 30% handoff improvement shows up over time."),
  stack=stack("Figma","Figma Design Systems","Adobe Illustrator","Usability Testing","HTML/CSS handoff"),
  facts=fact("Market","GCC")+fact("Buyer types","B2B &amp; B2C")+fact("Deliverable","Design system + checkout UX")+fact("Status","Live in production"),
))

DATA.append(dict(
  slug="nextipz", section="design", section_label="Design",
  title="Nextipz", title_html="Nextipz",
  desc="A QR-code tipping product for hospitality staff in the UAE — scan, tip, done — designed as a Figma prototype with payouts through local gateways.",
  status="Prototype", category="Fintech · Hospitality",
  dek="Tipping in the UAE is still mostly cash or awkward card workarounds. Nextipz turns a table tent or badge QR code into a tip in under 15 seconds, with the payout landing directly with the staff member who earned it.",
  role="Solo product designer", timeline="Concept → Figma prototype", platform="Mobile web (QR entry point)", client="Independent product",
  c1="#0f766e", c2="#2dd4bf", cover_text="Nextipz",
  links=[link("Open the Figma prototype", "https://www.figma.com/proto/iU8xI6dBXds22BbDEkJ59I?node-id=1-3&t=P0wdUVQHjiZitkpx-6")],
  challenge=p(
    "Hospitality staff in UAE restaurants, cafés and hotels mostly rely on cash tips or ad-hoc transfers, which are easy to forget, awkward to request, and leave no record for the staff member or the venue.",
    "Any digital tipping flow has to work for a guest who has never used the product before, on their own phone, usually one-handed, often mid-meal — so the entire path from scanning a code to a completed tip has to ask for almost nothing and explain itself instantly."
  ),
  approach=p(
    "I designed the flow backwards from the guest's moment of intent: they've decided to tip, and every screen between that decision and payment confirmation is a chance to lose them. That meant minimising input fields, pre-set tip amounts over free-text entry by default, and a payment step that reuses familiar local gateway UI patterns rather than inventing new ones.",
    "On the staff side, I designed a lightweight dashboard view so individual staff or venue managers can see tips received without needing a full back-office system — keeping the product narrow and shippable rather than trying to be a full POS replacement."
  ),
  solution=p("A QR-first mobile flow: scan a code at the table, pick or enter a tip amount, pay through a local gateway, done.") + ul(
    "Guest flow: scan → amount → pay → confirmation, no account creation required",
    "Staff-facing view of tips received, scoped to the individual or the venue",
    "Payment integration designed around local UAE payment gateways for familiar, trusted checkout UI"
  ),
  outcome_intro=p("This is a prototype stage product — the value delivered so far is a validated, clickable Figma flow ready to hand to engineering."),
  stats=stat("&lt;15s","target time to complete a tip") + stat("0","accounts required for guests") + stat("UAE","local payment gateway focus"),
  outcome_extra=p("The prototype is the reference design for a planned build-out; if you're a restaurant group or hotel operator interested in piloting it, that's a conversation worth having."),
  stack=stack("Figma","Figma Prototyping","UX Research","Mobile-first design"),
  facts=fact("Stage","Figma prototype")+fact("Primary user","Hospitality guests")+fact("Secondary user","Staff / venue managers")+fact("Market","UAE"),
))

DATA.append(dict(
  slug="nexnowgo", section="design", section_label="Design",
  title="NexNowGo", title_html="NexNowGo",
  desc="A full product design file covering flows, screens and the UI system for NexNowGo, built in Figma.",
  status="Figma file", category="Product Design",
  dek="A complete product design pass — information architecture, core flows, and a coherent UI system — built to take a concept from idea to something a development team could build directly from.",
  role="Product designer", timeline="Figma design file", platform="Mobile / Web", client="Independent product",
  c1="#312e81", c2="#818cf8", cover_text="NexNowGo",
  links=[link("Open the Figma file", "https://www.figma.com/design/KcIt9iWfiE5PtmlhHesPEo/NEXNOWGO?m=auto&t=P0wdUVQHjiZitkpx-6")],
  challenge=p(
    "Early-stage products often skip straight to screens without first settling the underlying flows and system — which means every new feature either breaks visual consistency or requires re-deriving decisions that were never made explicit the first time.",
    "NexNowGo needed the opposite: a design foundation solid enough that screens could be added later without a redesign, and clear enough that engineering could build directly from the file without a long back-and-forth."
  ),
  approach=p(
    "I started with the core user flows rather than individual screens, mapping how someone moves through the product end-to-end before deciding what any single screen looks like. Once the flows held together, I built out a UI system — type scale, spacing, components, states — so every subsequent screen reused the same decisions instead of reinventing them.",
    "That system-first approach is the same one I use in the design systems I build at Würth UAE, just applied at product scale rather than enterprise scale."
  ),
  solution=p("A complete Figma file covering the product's core flows, full screen set and an underlying UI system.") + ul(
    "End-to-end flow mapping before any screen design began",
    "A reusable component and UI system underneath every screen",
    "Screens built to be handed directly to engineering with minimal redlining"
  ),
  outcome_intro=p("The result is a product design file that functions as both the design spec and the design system in one place."),
  stats=stat("Full","flow + screen coverage") + stat("1","unified UI system") + stat("Figma","single source of truth"),
  outcome_extra=p("Because the system was built before the screens, extending the product later is a matter of composing existing pieces, not starting over."),
  stack=stack("Figma","Design Systems","Information Architecture","UI/UX Design"),
  facts=fact("Deliverable","Full product design file")+fact("Format","Figma")+fact("Scope","Flows + screens + system"),
))

DATA.append(dict(
  slug="nursing-job-pro", section="design", section_label="Design",
  title="Nursing Job Pro", title_html="Nursing Job <em>Pro</em>",
  desc="A healthcare jobs marketplace app designed around how nursing professionals actually search for and apply to roles, built as a Figma mobile app design.",
  status="Figma file", category="Jobs Marketplace · Healthcare",
  dek="General-purpose job boards treat healthcare hiring like any other hiring — but credentials, shift types and licensing requirements mean nurses search differently than most job seekers. Nursing Job Pro is built around that difference.",
  role="Product / UX designer", timeline="Figma mobile app design", platform="Mobile app", client="Independent product",
  c1="#075985", c2="#38bdf8", cover_text="Nursing Job Pro",
  links=[link("Open the Figma file", "https://www.figma.com/design/TNOFVteGdS9TAZTSn1Xwiv/Nursing-Job-Pro?m=auto&t=P0wdUVQHjiZitkpx-6")],
  challenge=p(
    "Nursing professionals searching for work care about things most job boards don't surface well: shift pattern, unit type, licensing and credential match, and proximity to facilities with the right specialty. Generic job-search UX (keyword search, flat filters) doesn't map well onto those priorities.",
    "The design challenge was building a job-search experience specific enough to feel built for healthcare workers, without the added complexity turning into a cluttered, filter-heavy interface that's slower than a generic board."
  ),
  approach=p(
    "I designed the search and filter experience around the specific variables that matter in nursing hiring — credential type, shift pattern, facility type and specialty — surfaced as fast, tappable filters rather than buried in an advanced-search panel.",
    "The application flow itself was kept as lightweight as the generic competitors, so the product's advantage is in relevance and speed-to-apply, not in asking candidates to do more work."
  ),
  solution=p("A mobile job-search experience purpose-built for healthcare professionals.") + ul(
    "Search and filtering built around credential, shift pattern and specialty, not generic keyword search",
    "Fast, low-friction application flow once a relevant role is found",
    "Mobile-first design, since healthcare shift workers are searching between shifts, not at a desk"
  ),
  outcome_intro=p("A complete, ready-to-build mobile app design for a focused healthcare jobs marketplace."),
  stats=stat("Healthcare","focused marketplace") + stat("Mobile","first design") + stat("Figma","full app design"),
  outcome_extra=p("The differentiated filtering model is the core bet of the product — designing for the specific job-search behaviour of nurses rather than adapting a generic job board template."),
  stack=stack("Figma","Mobile UX","Information Architecture","Healthcare UX"),
  facts=fact("Audience","Nursing professionals")+fact("Format","Mobile app")+fact("Deliverable","Figma design file"),
))

DATA.append(dict(
  slug="tamil-calendar-2026", section="design", section_label="Design",
  title="Tamil Calendar 2026", title_html="Tamil Calendar <em>2026</em>",
  desc="A calendar app designed for Tamil-speaking users, covering festivals, auspicious dates and daily details, built as a Figma mobile app design.",
  status="Figma file", category="Mobile App · Localisation",
  dek="Tamil calendars carry cultural and astrological information — festival dates, auspicious timings, daily panchangam details — that a generic Gregorian calendar app has no concept of. This app is designed around that specific content model.",
  role="Product / UX designer", timeline="Figma mobile app design", platform="Mobile app", client="Independent product",
  c1="#b45309", c2="#fbbf24", cover_text="Tamil Calendar 2026",
  links=[link("Open the Figma file", "https://www.figma.com/design/aKl6gECFPQSqdcxytUo5jP/Tamil-Calendar-2026?m=auto&t=P0wdUVQHjiZitkpx-6")],
  challenge=p(
    "Tamil-speaking users looking for a calendar app are often looking for something a Western calendar simply doesn't contain: festival dates tied to the Tamil lunar calendar, daily auspicious and inauspicious timings, and culturally specific date information laid out the way a printed Tamil calendar traditionally presents it.",
    "The design challenge was translating that dense, information-rich print format into a clean mobile UI, without losing the specific daily details that make the app useful in the first place."
  ),
  approach=p(
    "I treated the daily detail view as the core screen, since it's the one users will open every day, and designed the information hierarchy around what's most commonly checked first — the day's date in both calendar systems, key timings, and festival flags — with secondary detail available but not competing for attention.",
    "Localisation here isn't just translated text; it's a different underlying data model (lunar dates, regional festival variation) driving a UI built specifically around it, rather than a Tamil-language skin over a generic calendar template."
  ),
  solution=p("A mobile calendar app built around the Tamil calendar system.") + ul(
    "Daily detail view surfacing auspicious timings and panchangam-style information",
    "Festival and date flagging specific to the Tamil lunar calendar",
    "An information hierarchy designed for daily, habitual use, not one-off lookup"
  ),
  outcome_intro=p("A complete mobile app design ready for development, aimed at an underserved, culturally specific niche."),
  stats=stat("2026","edition designed") + stat("Tamil","calendar system") + stat("Daily","use case design"),
  outcome_extra=p("Localisation-first products like this are a small but genuine niche — most calendar apps treat non-Gregorian systems as an afterthought, if they support them at all."),
  stack=stack("Figma","Mobile UX","Localisation","Information Design"),
  facts=fact("Audience","Tamil-speaking users")+fact("Format","Mobile app")+fact("Edition","2026"),
))

DATA.append(dict(
  slug="boodoo", section="design", section_label="Design",
  title="Boodoo", title_html="Boodoo",
  desc="An astrology, horoscope and community app designed in Figma, combining personal horoscope content with a social community layer.",
  status="Figma file", category="Astrology · Community",
  dek="Most astrology apps are single-player: you check your horoscope and leave. Boodoo adds a community layer on top, so astrology becomes something people discuss and share, not just privately consume.",
  role="Product / UX designer", timeline="Figma mobile app design", platform="Mobile app", client="Independent product",
  c1="#581c87", c2="#c084fc", cover_text="Boodoo",
  links=[link("Open the Figma file", "https://www.figma.com/design/XhocrTndjGbDDjNmnc7o9x/Boodoo---Astrology---Horoscope--Community-?m=auto&t=P0wdUVQHjiZitkpx-6")],
  challenge=p(
    "Horoscope apps are typically a solitary daily-check habit with little reason to open the app beyond the daily read. Adding a community layer introduces real design complexity: how do you let people share and discuss horoscope content without the app turning into an undifferentiated generic social feed?",
    "The challenge was keeping astrology content as the clear anchor of the product, with community as something that grows out of it — comments on a shared sign's horoscope, compatibility discussions — rather than a bolt-on feed competing for attention."
  ),
  approach=p(
    "I designed the personal horoscope experience first as a strong, self-sufficient core — daily reading, sign and compatibility info — then layered community features onto specific, astrology-relevant moments: a horoscope you can react to or discuss, rather than a separate open-ended social timeline.",
    "This kept the product's identity clear: it's an astrology app with community built in, not a social app with horoscopes bolted on."
  ),
  solution=p("A mobile astrology and horoscope app with an integrated community layer.") + ul(
    "Daily personal horoscope and sign-based content as the core experience",
    "Community interaction scoped to astrology content — reactions, discussion — rather than a generic feed",
    "A UI designed to feel personal and daily-habit-forming, consistent with how horoscope apps are actually used"
  ),
  outcome_intro=p("A complete mobile app design combining a strong single-player astrology experience with social features that reinforce rather than dilute it."),
  stats=stat("Astrology","+ community combined") + stat("Daily","engagement design") + stat("Figma","full app design"),
  outcome_extra=p("The community-layer approach — anchored to content rather than a generic feed — is the kind of product decision that has to be made at the design stage, before any engineering begins."),
  stack=stack("Figma","Mobile UX","Community Design","UI/UX Design"),
  facts=fact("Category","Astrology / Horoscope")+fact("Layer","+ Community")+fact("Format","Mobile app"),
))

# ============================= CODING PROJECTS =============================

DATA.append(dict(
  slug="chatcart-pro", section="code", section_label="Code",
  title="ChatCart Pro", title_html="ChatCart <em>Pro</em>",
  desc="A WhatsApp-native AI commerce platform I designed and built: customers order in chat, stock syncs with the POS, and an AI voice agent takes calls. Live with a pilot supermarket in Tamil Nadu.",
  status="Live", category="AI Commerce · UAE &amp; India",
  dek="Most small restaurants and grocery stores in the UAE and India don't have the margin or the technical team to run a custom ordering app. ChatCart Pro meets customers where they already are — WhatsApp — and gives the business an AI chatbot, a voice agent, and a POS-synced inventory, all in one product.",
  role="Founder · Product design + full-stack build", timeline="In active development, live pilot", platform="WhatsApp Cloud API · Web · Voice", client="Independent product (Nexsofture)",
  c1="#064e3b", c2="#25d366", cover_text="ChatCart Pro",
  links=[link("Visit chatcartpro.com", "https://chatcartpro.com"), linkghost("AI chatbot for websites", "https://chatcartpro.com/ai-chatbot-for-website/"), linkghost("AI voice calling agent", "https://chatcartpro.com/ai-voice-calling-agent/"), linkghost("Restaurant WhatsApp + Voice + POS", "https://chatcartpro.com/restaurant-pos-voice-chat/")],
  challenge=p(
    "Restaurants and grocery stores lose orders every time a phone line is busy, a customer doesn't want to install another app, or a message on social media never gets a reply. These businesses also typically run on a POS system with its own stock numbers, disconnected from any new ordering channel.",
    "I wanted to build something that didn't ask small business owners to change how their customers already behave — people already message businesses on WhatsApp — while still solving the real operational problem of stock going out of sync between channels."
  ),
  approach=p(
    "I designed and built ChatCart Pro around WhatsApp as the primary ordering surface, since it requires zero download and zero behaviour change from the customer. On the business side, the core engineering problem was keeping cart, stock and POS numbers consistent in real time, so an order placed in chat doesn't oversell inventory that was just sold in-store.",
    "I added an AI voice calling agent on top of the chat flow for customers who'd rather call — covering the case where WhatsApp isn't the right channel, like an older customer or a quick phone order — and an AI chatbot for businesses that want a similar experience embedded on their own website, not just WhatsApp."
  ),
  solution=p("A WhatsApp-native commerce platform with POS-synced stock and an AI voice ordering option.") + ul(
    "WhatsApp Cloud API integration for in-chat ordering, no app install required",
    "Real-time POS stock sync so WhatsApp orders and in-store sales share one inventory source of truth",
    "AI voice calling agent that takes phone orders and logs them into the same system",
    "A white-label AI chatbot product for restaurants' own websites",
    "Restaurant-specific flow combining WhatsApp + voice + POS ordering in one package"
  ),
  outcome_intro=p("ChatCart Pro is live with a pilot supermarket in Tamil Nadu, India, validating the core WhatsApp-plus-POS-sync model in a real retail environment."),
  stats=stat("Live","pilot supermarket, Tamil Nadu") + stat("3","products: chat, voice, website bot") + stat("UAE &amp; India","target markets"),
  outcome_extra=p("As the founder and sole product/engineering lead on this, I own everything from the WhatsApp integration logic to the voice agent's conversation design to the POS sync architecture — the kind of full-stack ownership that doesn't come up in an employed design role."),
  stack=stack("WhatsApp Cloud API","Node.js","Voice AI","POS Integration","React"),
  facts=fact("Founder","Yes (Nexsofture)")+fact("Pilot","Supermarket, Tamil Nadu")+fact("Channels","WhatsApp, voice, web chatbot")+fact("Status","Live, in development"),
))

DATA.append(dict(
  slug="people-core-hr", section="code", section_label="Code",
  title="People Core HR", title_html="People Core <em>HR</em>",
  desc="A working HR platform prototype I designed and built, deployed and fully clickable as a live demo.",
  status="Live demo", category="HR SaaS",
  dek="A functioning HR platform prototype — not static mockups, but a deployed, clickable application — built to demonstrate core HR workflows end to end.",
  role="Product design + build", timeline="Demo prototype", platform="Web app", client="Independent product",
  c1="#1e3a8a", c2="#60a5fa", cover_text="People Core HR",
  links=[link("Open the live demo", "https://peoplecorehr-demoprototype.vercel.app/")],
  challenge=p(
    "HR software demos are often either static Figma click-throughs that don't survive real interaction, or they're full enterprise platforms that are overkill to spin up just to validate a concept. I wanted something in between: a real, working web app that behaves like the finished product, without the overhead of a production HR system.",
  ),
  approach=p(
    "I designed and built this as a genuine working prototype rather than a static mockup, which meant making real decisions about data model and state, not just visual layout — core HR workflows (like managing people records and processes) had to actually function, not just look clickable in a design tool."
  ),
  solution=p("A deployed, interactive HR platform prototype covering core HR workflows.") + ul(
    "Real application behaviour, not a static click-through prototype",
    "Deployed on Vercel for instant access — no setup required to evaluate it",
    "Built end-to-end by one person: design, front end and deployment"
  ),
  outcome_intro=p("The result is a live, testable artifact rather than a slide deck — the kind of thing you can hand to a stakeholder with a link instead of a meeting."),
  stats=stat("Live","deployed demo") + stat("1","person, full build") + stat("Vercel","hosting"),
  outcome_extra=p("Building a working prototype rather than a static one is slower up front, but it's a far more convincing way to validate an HR product concept with real users or stakeholders."),
  stack=stack("React","Vercel","Web App Design"),
  facts=fact("Type","Working demo prototype")+fact("Hosting","Vercel")+fact("Build","Solo, design + code"),
))

DATA.append(dict(
  slug="edupulse", section="code", section_label="Code",
  title="EduPulse", title_html="EduPulse",
  desc="A school management SaaS platform built on Next.js 14, with four role-based workspaces for admins, teachers, parents and students.",
  status="In development", category="EdTech SaaS",
  dek="Schools have at least four distinct audiences using the same system — admins, teachers, parents and students — each needing a completely different view of the same underlying data. EduPulse is designed around that split from the ground up.",
  role="Product design + full-stack build", timeline="In development", platform="Web (Next.js 14)", client="Independent product (Nexsofture)",
  c1="#831843", c2="#f472b6", cover_text="EduPulse",
  links=[],
  challenge=p(
    "A school management platform has to serve an administrator managing the whole institution, a teacher managing a classroom, a parent tracking one child, and a student navigating their own schedule and work — all from the same underlying data, but with completely different needs, permissions and mental models.",
    "Designing one undifferentiated interface for all four roles, or designing four fully separate apps, are both failure modes: one is confusing, the other is unmaintainable."
  ),
  approach=p(
    "I designed four role-based workspaces sharing one data and component foundation, so admin, teacher, parent and student each get an interface scoped to what they actually need to do, without the engineering team maintaining four separate codebases.",
    "On the build side, Next.js 14 gave me the routing and rendering model to serve these distinct workspaces efficiently from one application, which matters for a product that needs to stay maintainable as a solo or small-team build."
  ),
  solution=p("A role-based school management platform with four distinct, permission-scoped workspaces.") + ul(
    "Admin workspace: institution-wide management and oversight",
    "Teacher workspace: classroom-scoped tools and communication",
    "Parent workspace: single-child tracking and school communication",
    "Student workspace: schedule, assignments and personal progress",
    "Built on Next.js 14 as a shared foundation across all four roles"
  ),
  outcome_intro=p("EduPulse is in active development as a Nexsofture product, built around a role-based architecture designed to scale to more schools without a redesign."),
  stats=stat("4","role-based workspaces") + stat("Next.js 14","foundation") + stat("1","shared data model"),
  outcome_extra=p("The role-based architecture is the core design decision the whole product depends on — getting it right early means new features extend naturally into each workspace instead of requiring four parallel builds."),
  stack=stack("Next.js 14","React","Node.js","SQL","Role-based Access"),
  facts=fact("Roles","Admin, teacher, parent, student")+fact("Framework","Next.js 14")+fact("Status","In development"),
))

DATA.append(dict(
  slug="sheetmind-ai", section="code", section_label="Code",
  title="SheetMind AI", title_html="SheetMind <em>AI</em>",
  desc="An Excel add-in I designed and built that lets people ask a language model about their spreadsheets, formulas and data — sold on Gumroad.",
  status="Sold on Gumroad", category="Productivity · AI",
  dek="Most people using Excel don't write formulas fluently — they copy one from a forum, half-understand it, and move on. SheetMind AI puts an LLM directly inside the spreadsheet so you can just ask what a formula does, or ask for the formula you need, without leaving the sheet.",
  role="Founder · Product design + build", timeline="Shipped, sold on Gumroad", platform="Excel add-in", client="Independent product (Nexsofture)",
  c1="#14532d", c2="#4ade80", cover_text="SheetMind AI",
  links=[],
  challenge=p(
    "Excel formulas are powerful but notoriously unreadable once they get past a few nested functions, and most users don't have a reliable way to ask 'what does this actually do' or 'what formula gets me this result' without leaving the spreadsheet and searching online.",
    "An AI add-in only works if it fits the existing Excel workflow — if it requires copy-pasting data out to a separate chat window, most of the value of 'staying in your spreadsheet' is lost."
  ),
  approach=p(
    "I designed SheetMind AI to live inside Excel as a native add-in, so the language model has direct context on the actual spreadsheet, formulas and data the user is working with, rather than requiring them to describe or paste it manually.",
    "The product and packaging decisions mattered as much as the engineering here: shipping it as a self-serve product on Gumroad meant designing an onboarding and pricing experience that works without a sales conversation."
  ),
  solution=p("An Excel add-in that lets users query an LLM about their live spreadsheet.") + ul(
    "In-sheet AI chat with direct context on formulas and data, no copy-pasting required",
    "Explains existing formulas in plain language",
    "Generates new formulas from a plain-language description of what's needed",
    "Packaged and sold as a self-serve product on Gumroad"
  ),
  outcome_intro=p("SheetMind AI is a shipped, sold product — one of the clearer examples of taking an AI product from concept through build to a paying customer base without outside funding or a sales team."),
  stats=stat("Shipped","&amp; sold") + stat("Gumroad","self-serve distribution") + stat("In-sheet","LLM context"),
  outcome_extra=p("This is the kind of product that only gets built end-to-end by someone comfortable owning design, prompt engineering, the Excel add-in integration, and the commercial packaging all at once."),
  stack=stack("Excel Add-in APIs","LLM Integration","Prompt Engineering","Gumroad"),
  facts=fact("Platform","Microsoft Excel")+fact("Distribution","Gumroad")+fact("Founder","Yes (Nexsofture)")+fact("Status","Shipped &amp; sold"),
))

DATA.append(dict(
  slug="voicepilot", section="code", section_label="Code",
  title="VoicePilot", title_html="VoicePilot",
  desc="An AI voice agent platform concept designed for businesses that speak Tamil, Malayalam and Hindi — extending the voice-agent work from ChatCart Pro into a dedicated, multilingual regional product.",
  status="Concept · Product spec", category="Voice AI",
  dek="Most voice AI platforms are built English-first, with regional languages as an afterthought if supported at all. VoicePilot flips that: it's designed from the ground up for businesses that operate in Tamil, Malayalam and Hindi.",
  role="Product design (spec stage)", timeline="Concept / product spec", platform="Voice AI platform", client="Independent concept (Nexsofture)",
  c1="#7c2d12", c2="#fb923c", cover_text="VoicePilot",
  links=[],
  challenge=p(
    "Voice AI platforms generally treat non-English languages as a secondary feature bolted onto an English-first product — accents, regional phrasing and code-switching (mixing English and a regional language mid-sentence, which is extremely common in South Asian business contexts) are often poorly handled.",
    "Businesses operating primarily in Tamil, Malayalam or Hindi are underserved by this default, even though the underlying use case — an AI agent taking calls, answering questions, routing requests — is identical to what English-first platforms already offer well."
  ),
  approach=p(
    "This grew directly out of building the voice agent for ChatCart Pro, where I saw firsthand what it actually takes to make a voice AI agent work naturally in a regional language context, rather than as a translated afterthought.",
    "VoicePilot is the product spec for taking that capability and generalising it: a voice agent platform where Tamil, Malayalam and Hindi are first-class, not retrofitted, so any business operating in those languages can deploy an agent without compromise."
  ),
  solution=p("A product specification for a multilingual, regional-first AI voice agent platform.") + ul(
    "First-class support for Tamil, Malayalam and Hindi, not translated-English fallback",
    "Built on learnings from the production voice agent inside ChatCart Pro",
    "Positioned for businesses in South Asian and diaspora markets underserved by English-first voice AI"
  ),
  outcome_intro=p("VoicePilot is currently at the concept and product-spec stage — the next step after ChatCart Pro proved the underlying voice-agent approach works in a live commercial setting."),
  stats=stat("3","languages: Tamil, Malayalam, Hindi") + stat("Concept","stage, spec complete") + stat("Derived from","ChatCart Pro's voice agent"),
  outcome_extra=p("Spec-stage work like this is where a product gets scoped honestly before any code is written — defining exactly what 'first-class regional language support' has to mean in practice, not just as a marketing claim."),
  stack=stack("Voice AI","Product Specification","Multilingual NLP","Conversation Design"),
  facts=fact("Stage","Concept / product spec")+fact("Languages","Tamil, Malayalam, Hindi")+fact("Origin","ChatCart Pro voice agent"),
))

DATA.append(dict(
  slug="shift-breaker", section="code", section_label="Code",
  title="Shift Breaker", title_html="Shift <em>Breaker</em>",
  desc="An open-source app published on GitHub, available to browse and run directly from source.",
  status="Open source", category="App · GitHub",
  dek="An open-source app, published with full source available on GitHub for anyone to inspect, run or contribute to.",
  role="Developer", timeline="Published, open source", platform="GitHub", client="Open-source project",
  c1="#422006", c2="#eab308", cover_text="Shift Breaker",
  links=[link("Browse the source on GitHub", "https://github.com/daviddigil/shiftbreaker")],
  challenge=p(
    "Not every project needs a storefront, a pitch deck or a go-to-market plan — sometimes the right outcome is simply a well-built, open piece of software that does its job and is available for anyone to use or learn from.",
  ),
  approach=p(
    "Shift Breaker was built and published as an open-source repository rather than a packaged commercial product, with the README and source itself as the primary documentation for anyone wanting to understand or run it."
  ),
  solution=p("An open-source application, published on GitHub.") + ul(
    "Full source available for review, use or contribution",
    "Documented via its GitHub README",
    "Published under daviddigil's GitHub, alongside the rest of the code work"
  ),
  outcome_intro=p("As with any open-source project, the best way to evaluate it is directly — the README and commit history on GitHub are the primary source of truth."),
  stats=stat("Open","source, public repo") + stat("GitHub","hosted"),
  outcome_extra=p(""),
  stack=stack("GitHub"),
  facts=fact("Type","Open-source app")+fact("Hosting","GitHub")+fact("Docs","See repo README"),
))

# ============================= GENERATE =============================

def esc(s): return s  # content is already hand-authored HTML-safe

ORDER = [d['slug'] for d in DATA]

for i, d in enumerate(DATA):
    prev = DATA[(i-1) % len(DATA)]
    nxt = DATA[(i+1) % len(DATA)]
    html = TPL
    repl = {
        "{{TITLE}}": d['title'],
        "{{TITLE_HTML}}": d['title_html'],
        "{{DESC}}": d['desc'],
        "{{SLUG}}": d['slug'],
        "{{SECTION}}": d['section'],
        "{{SECTION_LABEL}}": d['section_label'],
        "{{STATUS}}": d['status'],
        "{{CATEGORY}}": d['category'],
        "{{DEK}}": d['dek'],
        "{{ROLE}}": d['role'],
        "{{TIMELINE}}": d['timeline'],
        "{{PLATFORM}}": d['platform'],
        "{{CLIENT}}": d['client'],
        "{{C1}}": d['c1'],
        "{{C2}}": d['c2'],
        "{{COVER_TEXT}}": d['cover_text'],
        "{{LINKS}}": "\n      ".join(d['links']) if d['links'] else "",
        "{{CHALLENGE}}": d['challenge'],
        "{{APPROACH}}": d['approach'],
        "{{SOLUTION}}": d['solution'],
        "{{OUTCOME_INTRO}}": d['outcome_intro'],
        "{{STATS}}": d['stats'],
        "{{OUTCOME_EXTRA}}": d['outcome_extra'],
        "{{STACK}}": d['stack'],
        "{{FACTS}}": d['facts'],
        "{{PREV_HREF}}": prev['slug'] + ".html",
        "{{PREV_TITLE}}": prev['title'],
        "{{NEXT_HREF}}": nxt['slug'] + ".html",
        "{{NEXT_TITLE}}": nxt['title'],
    }
    for k, v in repl.items():
        html = html.replace(k, v)
    out_path = d['slug'] + ".html"
    with open(out_path, 'w', encoding='utf-8') as f:
        f.write(html)
    print("wrote", out_path)

print("done,", len(DATA), "pages")
