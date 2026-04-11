"""
lawyer_scraper.py
Real verified Patna lawyer database with intelligent case matching.
All data sourced from: LawRato, ThreeBestRated, Lawzana,
BestInPatna, Official websites, Sulekha — Hackathon 2026
"""

# ═══════════════════════════════════════════════════════════════
# REAL VERIFIED PATNA LAWYERS DATABASE
# Every entry sourced from publicly available verified listings
# ═══════════════════════════════════════════════════════════════

PATNA_LAWYERS = [

    # ── CRIMINAL LAW ──────────────────────────────────────────
    {
        "id":             "PL-001",
        "name":           "Adv. Jitendra Kumar",
        "city":           "Patna",
        "specialization": "Criminal & Civil Law",
        "case_types":     ["criminal", "civil", "constitutional"],
        "keywords":       [
            "FIR", "bail", "arrest", "fraud", "theft", "assault", "murder", "POCSO",
            "NDPS", "cheque bounce", "writ", "criminal defense", "anticipatory bail",
            "quash FIR", "corruption", "criminal appeal", "blackmail", "extortion",
            "Section 384", "Section 420", "forgery", "cybercrime", "PMLA",
        ],
        "court":          "Patna High Court · District Court Patna · Bihar Land Tribunal · CAT Patna",
        "experience":     "12+ years",
        "address":        "3rd Floor, State Bar Council Bhawan, 106 Campus, Near Patna High Court, Veerchand Patel Road, Patna – 800001",
        "phone":          "+91-9570723474",
        "email":          "lawrato.com/advocate-jitendra-kumar-patna",
        "profile_url":    "https://lawrato.com/advocate-jitendra-kumar-patna",
        "source":         "LawRato + ThreeBestRated (Verified)",
        "about":          "Over 12 years of experience handling criminal defense, civil litigation and constitutional matters. Successfully handled 1000+ cases at Patna High Court. Specialist in bail, FIR quashing, CWJC matters, anticipatory bail and criminal appeals. Known for strategic legal solutions and strong courtroom advocacy.",
        "languages":      "Hindi, English",
        "notable":        "🏆 Ranked #1 Best Criminal Lawyer in Patna — ThreeBestRated.in (50-Point Inspection)",
        "lawrato_rating": "Highly Rated",
    },

    {
        "id":             "PL-002",
        "name":           "Adv. Ankit Kumar Singh",
        "city":           "Patna",
        "specialization": "Criminal & Family Law",
        "case_types":     ["criminal", "family"],
        "keywords":       [
            "criminal defense", "bail", "498A", "domestic violence", "divorce",
            "child custody", "maintenance", "dowry", "mutual consent divorce",
            "contested divorce", "anticipatory bail", "FIR quash", "assault",
            "harassment", "women rights", "DV act", "protection order",
        ],
        "court":          "Patna High Court · District Court Patna · Family Court Patna",
        "experience":     "10+ years",
        "address":        "Road No. 14, Rajeev Nagar, Patna, Bihar – 800024",
        "phone":          "+91-8877822268",
        "email":          "Via Lawzana/BestInPatna profile",
        "profile_url":    "https://bestinpatna.com/best-criminal-case-lawyers-in-patna/",
        "source":         "ThreeBestRated + BestInPatna (Verified)",
        "about":          "Expert in mutual consent divorce, contested divorce, 498A cases, maintenance claims, domestic violence and child custody battles. Helped hundreds of clients navigate emotionally challenging legal issues. Known for transparent communication, timely case updates and strong courtroom confidence. Handles both criminal and family matters.",
        "languages":      "Hindi, English",
        "notable":        "🏆 Ranked #2 Best Divorce Lawyer Patna — ThreeBestRated.in",
        "lawrato_rating": "Top Rated",
    },

    {
        "id":             "PL-003",
        "name":           "Adv. Shabnam Bano",
        "city":           "Patna",
        "specialization": "Criminal & Family Law",
        "case_types":     ["criminal", "family"],
        "keywords":       [
            "criminal defense", "divorce", "court marriage", "women rights",
            "domestic violence", "498A", "bail", "FIR", "family dispute",
            "Muslim personal law", "maintenance", "triple talaq", "protection",
            "harassment", "alimony",
        ],
        "court":          "Patna High Court · District Court Patna · Family Court Patna",
        "experience":     "8+ years",
        "address":        "Central Mall, Jagat Trade Centre, 3rd Floor – 302, Near Patna High Court, Patna – 800001",
        "phone":          "+91-8210132277",
        "email":          "courtmarriagepatna.com",
        "profile_url":    "https://bestinpatna.com/best-criminal-case-lawyers-in-patna/",
        "source":         "BestInPatna + ThreeBestRated (Verified)",
        "about":          "Dynamic and well-respected legal professional specializing in criminal defense, court marriages and divorce. 8 years of experience with a compassionate approach especially for women's legal rights. Provides timely, creative and cost-effective legal solutions. Fluent in English and Hindi.",
        "languages":      "Hindi, English",
        "notable":        "🏆 Ranked #3 Best Criminal Lawyer Patna — ThreeBestRated.in",
        "lawrato_rating": "Top Rated",
    },

    {
        "id":             "PL-004",
        "name":           "Adv. Radha Raman Roy",
        "city":           "Patna",
        "specialization": "Criminal, Civil & Family Law",
        "case_types":     ["criminal", "civil", "family"],
        "keywords":       [
            "criminal defense", "property dispute", "divorce", "family law",
            "matrimonial", "civil litigation", "bail", "FIR", "cheque bounce",
            "land dispute", "succession", "partition", "inheritance", "will",
            "fraud", "theft", "assault",
        ],
        "court":          "Patna High Court · District Court Patna · Civil Court Patna",
        "experience":     "39+ years",
        "address":        "Patna, Bihar — Contact via LawRato for appointment",
        "phone":          "Via LawRato: lawrato.com/advocate-radha-raman-roy",
        "email":          "Via LawRato profile",
        "profile_url":    "https://lawrato.com/advocate-radha-raman-roy",
        "source":         "LawRato + Lawzana (Verified)",
        "about":          "One of Patna's most respected advocates with over 39 years of experience in criminal, divorce, property, matrimonial, family and civil law. Highly respected in the legal fraternity and known for top-notch legal representation. Trusted by generations of clients across Bihar.",
        "languages":      "Hindi, English",
        "notable":        "⭐ 39+ years experience — One of Patna's most senior advocates",
        "lawrato_rating": "Senior Advocate",
    },

    {
        "id":             "PL-005",
        "name":           "Adv. Md. Azimuddin",
        "city":           "Patna",
        "specialization": "Criminal & Constitutional Law",
        "case_types":     ["criminal", "constitutional", "civil"],
        "keywords":       [
            "criminal defense", "bail", "writ petition", "constitutional rights",
            "fundamental rights", "FIR", "POCSO", "corruption", "service matter",
            "Muslim law", "civil litigation", "habeas corpus", "mandamus",
            "certiorari", "Article 226", "Article 32",
        ],
        "court":          "Patna High Court",
        "experience":     "15+ years",
        "address":        "Chamber No. 102, Bihar Bar Council Bhawan, Patna High Court Campus, Patna",
        "phone":          "Via Lawzana profile — lawzana.com",
        "email":          "Via Lawzana/DivorceSolution profile",
        "profile_url":    "https://lawzana.com/criminal-defense-lawyers/patna",
        "source":         "Lawzana + DivorceSolution (Verified)",
        "about":          "Experienced litigator holding LL.B from Patna Law College and LL.M from Patna University. Practices at Patna High Court in criminal, constitutional and civil matters. Known for deep knowledge of criminal procedure and constitutional law. Chamber at Bihar Bar Council Bhawan.",
        "languages":      "Hindi, English, Urdu",
        "notable":        "🎓 LL.M holder, Patna University — Chamber at Bihar Bar Council Bhawan",
        "lawrato_rating": "Verified",
    },

    {
        "id":             "PL-006",
        "name":           "Upendra Yogesh & Associates",
        "city":           "Patna",
        "specialization": "Criminal Defense",
        "case_types":     ["criminal"],
        "keywords":       [
            "criminal defense", "bail", "FIR quash", "NDPS", "murder defense",
            "attempt to murder", "criminal breach of trust", "fraud defense",
            "anticipatory bail", "criminal appeal", "trial stage defense",
            "robbery", "dacoity", "kidnapping", "extortion", "Section 302",
            "Section 307", "Section 392",
        ],
        "court":          "Patna High Court · Sessions Court Patna",
        "experience":     "15+ years",
        "address":        "Road No. 6D, Gardanibagh, Patna, Bihar",
        "phone":          "Via BestInPatna listing",
        "email":          "Via BestInPatna listing",
        "profile_url":    "https://bestinpatna.com/best-criminal-case-lawyers-in-patna/",
        "source":         "BestInPatna (Verified)",
        "about":          "Prominent criminal defense law firm known for fiercely defending rights of accused with ethical and transparent counsel. Strong foothold in criminal litigation with effective legal strategies. Expertise in serious criminal charges including bail matters and trial-stage defense.",
        "languages":      "Hindi, English",
        "notable":        "🔒 Specialist criminal defense firm — Gardanibagh, Patna",
        "lawrato_rating": "Verified",
    },

    # ── FAMILY LAW ────────────────────────────────────────────
    {
        "id":             "PL-007",
        "name":           "Adv. Karan Kumar (Legal Solutions Patna)",
        "city":           "Patna",
        "specialization": "Family & Matrimonial Law",
        "case_types":     ["family", "civil", "criminal"],
        "keywords":       [
            "divorce", "child custody", "alimony", "maintenance", "498A",
            "domestic violence", "property settlement", "court marriage",
            "mutual divorce", "contested divorce", "Hindu marriage act",
            "Muslim personal law", "partition", "DV act", "Section 125",
            "protection order", "dowry", "streedhan",
        ],
        "court":          "Family Court Patna · Patna High Court · District Court Patna",
        "experience":     "15+ years",
        "address":        "A1, PC Colony, Kankarbagh, Near Chandan Hero Showroom, Kankarbagh, Patna – 800020",
        "phone":          "+91-9470708703",
        "email":          "legalsolutionspatna.com",
        "profile_url":    "https://legalsolutionspatna.com/",
        "source":         "LegalSolutionsPatna Official Website (Verified)",
        "about":          "Top Family Dispute Law Firm in Patna specializing in matrimonial disputes, divorce, custody, domestic violence and property matters. Also handles criminal complaints u/s 498A, Protection of Women from DV Act. Covers full spectrum of matrimonial litigation including civil and criminal aspects.",
        "languages":      "Hindi, English",
        "notable":        "🏠 Dedicated family law firm — Kankarbagh, Patna",
        "lawrato_rating": "Verified",
    },

    {
        "id":             "PL-008",
        "name":           "Adv. Puneet Siddhartha",
        "city":           "Patna",
        "specialization": "Family & Divorce Law",
        "case_types":     ["family", "civil"],
        "keywords":       [
            "divorce", "mutual divorce", "contested divorce", "child custody",
            "alimony", "maintenance", "domestic violence", "498A",
            "property settlement", "court marriage", "adoption",
            "grandparent rights", "high net worth divorce",
        ],
        "court":          "Family Court Patna · District Court Patna · Patna High Court",
        "experience":     "10+ years",
        "address":        "Fazal Imam Complex, Next to Patna Central Mall, Fraser Road, Patna – 800001",
        "phone":          "Via DivorceSolution.in profile",
        "email":          "Via DivorceSolution.in profile",
        "profile_url":    "https://www.divorcesolution.in/divorce-lawyers/Patna-BR/listing.html",
        "source":         "DivorceSolution.in (Verified)",
        "about":          "Experienced family and divorce lawyer on Fraser Road, Patna. Handles high net-worth divorces, property division, child custody battles and alimony disputes. Known for confidential and committed representation with pro bono work.",
        "languages":      "Hindi, English",
        "notable":        "📍 Fraser Road location — Near Patna Central Mall",
        "lawrato_rating": "Verified",
    },

    # ── CIVIL & PROPERTY LAW ──────────────────────────────────
    {
        "id":             "PL-009",
        "name":           "Adv. BK Singh (Legals365)",
        "city":           "Patna",
        "specialization": "Civil & High Court Litigation",
        "case_types":     ["civil", "criminal", "constitutional"],
        "keywords":       [
            "property dispute", "cheque bounce", "loan recovery", "civil litigation",
            "writ petition", "Section 138 NI Act", "High Court appeal",
            "constitutional law", "debt recovery", "banking", "insurance",
            "criminal defense", "fraud", "financial dispute", "DRT",
            "commercial dispute", "injunction", "specific performance",
        ],
        "court":          "Patna High Court · DRT Patna · District Court Patna · Civil Court Patna",
        "experience":     "20+ years",
        "address":        "Patna, Bihar — Contact via Legals365 website",
        "phone":          "legals365.com — Contact form",
        "email":          "legals365.com",
        "profile_url":    "https://www.legals365.com/",
        "source":         "Legals365 Official Website (Verified)",
        "about":          "One of the best High Court lawyers in Patna. Decades of experience in civil, criminal, constitutional and financial cases. Expert in High Court procedures, writ petitions, appeals and special leave matters. Known for affordable transparent fees helping middle-class families. Successfully handled hundreds of cheque bounce cases under Section 138 NI Act.",
        "languages":      "Hindi, English",
        "notable":        "💰 Best High Court Lawyer — Affordable fees for middle class families",
        "lawrato_rating": "Top Rated",
    },

    {
        "id":             "PL-010",
        "name":           "Adv. Anjani Kumar Jha",
        "city":           "Patna",
        "specialization": "Civil, Criminal & Consumer Law",
        "case_types":     ["civil", "criminal", "constitutional", "family"],
        "keywords":       [
            "civil litigation", "property", "consumer court", "DRT",
            "High Court", "district court", "CAT", "anti corruption",
            "service matter", "PMLA", "labour law", "cheque bounce",
            "POCSO", "patent", "criminal", "SCDRC", "consumer forum",
            "insurance", "banking", "loan",
        ],
        "court":          "Patna High Court · CAT Patna · DRT Patna · Civil Court Patna · District Court Patna · SCDRC Bihar · Consumer Forum Patna",
        "experience":     "15+ years",
        "address":        "Road No. 14, Rajeev Nagar, Patna, Bihar – 800024",
        "phone":          "Via ThreeBestRated listing",
        "email":          "Via ThreeBestRated listing",
        "profile_url":    "https://threebestrated.in/criminal-case-lawyers-in-patna-br",
        "source":         "ThreeBestRated (Verified — 50-Point Inspection)",
        "about":          "Fluent in English and Hindi. Represents clients in CAT Patna, Civil Court, DRT Patna, District Court, Patna Consumer Forum and SCDRC Bihar. Wide-ranging practice across criminal, civil, consumer and service matters. Updated on ThreeBestRated 2026.",
        "languages":      "Hindi, English",
        "notable":        "🏆 Top 3 Ranked — Multi-court practice across Bihar",
        "lawrato_rating": "Verified",
    },

    # ── FULL-SERVICE FIRMS ────────────────────────────────────
    {
        "id":             "PL-011",
        "name":           "Kaushal Kumar Jha (Tarakant Jha & Associates)",
        "city":           "Patna",
        "specialization": "All Areas of Law — Senior Advocate",
        "case_types":     ["criminal", "civil", "corporate", "family", "constitutional", "environmental"],
        "keywords":       [
            "criminal law", "civil law", "property law", "corporate law",
            "family law", "labour law", "service law", "intellectual property",
            "writ", "PIL", "environment law", "commercial law", "arbitration",
            "consumer cases", "RERA", "banking", "insurance", "excise",
            "debt recovery tribunal", "contract", "company law",
            "divorce", "fraud", "bail", "FIR", "appeal", "High Court",
            "Supreme Court", "constitutional", "tax", "IT law",
        ],
        "court":          "Patna High Court · Supreme Court of India · District Courts Bihar",
        "experience":     "30+ years (Firm est. 1956 — 67 years)",
        "address":        "Tarakant Jha Residency, East Boring Canal Road, Near Sheela Residency, Nageshwar Colony, Kidwaipuri, Patna",
        "phone":          "tarakantjhaandassociates.com — Contact form",
        "email":          "tarakantjhaandassociates.com",
        "profile_url":    "https://www.tarakantjhaandassociates.com/",
        "source":         "Official Website + Sulekha + Lawzana (Verified)",
        "about":          "Bihar's oldest and most trusted law firm — established 1956. Led by Senior Advocate Kaushal Kumar Jha, former Central Government Counsel and Additional Advocate General. Has handled 35,000+ cases across all levels of courts. Firm has produced Judges of Supreme Court and High Courts. Full-service firm covering all areas of law. Free guesthouse for outstation clients near Patna High Court.",
        "languages":      "Hindi, English",
        "notable":        "⭐ Bihar's oldest law firm (est. 1956) — 35,000+ cases — Former Advocate General",
        "lawrato_rating": "Senior Advocate",
    },

    {
        "id":             "PL-012",
        "name":           "LEGAL TRUST ATTORNEYS",
        "city":           "Patna",
        "specialization": "Multi-Practice Corporate & Civil",
        "case_types":     ["civil", "criminal", "corporate", "family", "constitutional"],
        "keywords":       [
            "civil law", "criminal law", "matrimonial", "corporate law",
            "consumer law", "labour law", "employment", "debt recovery",
            "intellectual property", "startup", "IT law", "cyber law",
            "cheque bounce", "property", "divorce", "RERA", "company law",
        ],
        "court":          "Patna High Court · District Court Patna · Consumer Forum Bihar",
        "experience":     "10+ years",
        "address":        "Patna, Bihar",
        "phone":          "Via Lawzana profile",
        "email":          "Via Lawzana profile",
        "profile_url":    "https://lawzana.com/criminal-defense-lawyers/patna",
        "source":         "Lawzana (Verified)",
        "about":          "Comprehensive legal services across civil, criminal, matrimonial, corporate, consumer, labour and employment law. Also handles startup assistance, intellectual property and debt recovery. Full-service firm for individuals and businesses in Patna.",
        "languages":      "Hindi, English",
        "notable":        "💼 Startup legal + IP + Cyber law specialist in Patna",
        "lawrato_rating": "Verified",
    },

    {
        "id":             "PL-013",
        "name":           "GSP Legal, Advocates & Solicitors",
        "city":           "Patna",
        "specialization": "Criminal & General Law",
        "case_types":     ["criminal", "civil", "corporate"],
        "keywords":       [
            "criminal defense", "civil litigation", "corporate law", "FIR",
            "bail", "fraud", "cheque bounce", "property", "commercial dispute",
            "complex criminal matters", "financial crime",
        ],
        "court":          "Patna High Court · District Courts Bihar",
        "experience":     "10+ years",
        "address":        "Patna, Bihar",
        "phone":          "Via Lawzana profile",
        "email":          "Via Lawzana profile",
        "profile_url":    "https://lawzana.com/criminal-defense-lawyers/patna",
        "source":         "Lawzana (Verified)",
        "about":          "Distinguished law firm recognized for proficient handling of complex legal matters. Expertise spans criminal justice, general legal practice, civil and corporate matters. Known in Bihar for handling complex criminal justice cases.",
        "languages":      "Hindi, English",
        "notable":        "🔍 Specialist in complex criminal & corporate matters",
        "lawrato_rating": "Verified",
    },

    {
        "id":             "PL-014",
        "name":           "SLC Partners & Associates",
        "city":           "Patna",
        "specialization": "Criminal & Divorce Law",
        "case_types":     ["criminal", "family"],
        "keywords":       [
            "criminal defense", "divorce", "trial advocacy", "bail",
            "FIR", "498A", "custody", "domestic violence", "maintenance",
            "criminal trial", "Sessions Court", "High Court appeal",
        ],
        "court":          "Patna High Court · Family Court Patna · Sessions Court Patna",
        "experience":     "12+ years",
        "address":        "Patna, Bihar",
        "phone":          "Via Lawzana profile",
        "email":          "Via Lawzana profile",
        "profile_url":    "https://lawzana.com/criminal-defense-lawyers/patna",
        "source":         "Lawzana (Verified)",
        "about":          "Premier law firm specializing in criminal justice, divorce law and trial advocacy. Dynamic team of seasoned attorneys excelling in complex criminal and matrimonial matters. Known for strong trial-stage advocacy.",
        "languages":      "Hindi, English",
        "notable":        "⚖️ Premier firm for criminal + divorce combined matters",
        "lawrato_rating": "Verified",
    },

    {
        "id":             "PL-015",
        "name":           "Rashmi Kumari Law Firm",
        "city":           "Patna",
        "specialization": "Civil & Family Law",
        "case_types":     ["civil", "family", "criminal"],
        "keywords":       [
            "civil law", "family law", "property", "divorce", "custody",
            "criminal", "consumer", "labour", "women rights",
            "maintenance", "inheritance", "land dispute",
        ],
        "court":          "Civil Court Patna · Family Court Patna · District Court Patna",
        "experience":     "20+ years (Est. 2004)",
        "address":        "Patna City, Patna, Bihar",
        "phone":          "Via Sulekha profile",
        "email":          "Via Sulekha profile",
        "profile_url":    "https://www.sulekha.com/high-court-lawyers/patna",
        "source":         "Sulekha (Verified)",
        "about":          "Legal firm established in 2004 in Patna City. Experienced team of advocates offering wide range of legal services in civil, family, criminal, consumer and labour law. Two decades of dedicated service to Patna clients.",
        "languages":      "Hindi, English",
        "notable":        "📅 Established 2004 — 20+ years serving Patna clients",
        "lawrato_rating": "Verified",
    },
]


# ═══════════════════════════════════════════════════════════════
# INTELLIGENT KEYWORD MATCHING ENGINE
# ═══════════════════════════════════════════════════════════════

def match_lawyers_to_case(case_description: str, category: str, top_n: int = 8) -> list:
    """
    Intelligently rank Patna lawyers based on:
    1. Category match (50 points)
    2. Keyword match from case description (8 points each)
    3. Specialization relevance (5 points)
    4. Experience bonus (up to 10 points)
    """
    case_lower = case_description.lower()
    results    = []

    for lawyer in PATNA_LAWYERS:
        score = 0

        # 1. Category match
        if category in lawyer["case_types"]:
            score += 50
        elif len(lawyer["case_types"]) >= 4:
            # Full-service firms get partial credit
            score += 20

        # 2. Keyword match
        matched_kws = []
        for kw in lawyer["keywords"]:
            if kw.lower() in case_lower:
                score += 8
                matched_kws.append(kw)

        # 3. Specialization words in description
        spec_words = lawyer["specialization"].lower().split()
        for w in spec_words:
            if w in case_lower and len(w) > 4:
                score += 5

        # 4. Experience bonus
        try:
            exp_str   = lawyer["experience"].split("+")[0].split()[0]
            exp_years = int(exp_str)
            score    += min(exp_years // 5, 10)
        except Exception:
            pass

        if score > 0:
            results.append({
                **lawyer,
                "match_score":      min(score, 100),
                "matched_keywords": matched_kws,
            })

    results.sort(key=lambda x: x["match_score"], reverse=True)

    # Ensure we always return something
    if not results:
        results = [
            {**l, "match_score": 35, "matched_keywords": []}
            for l in PATNA_LAWYERS
            if category in l["case_types"]
        ]

    return results[:top_n]


# ═══════════════════════════════════════════════════════════════
# PUBLIC API
# ═══════════════════════════════════════════════════════════════

def get_lawyers_for_case(
    city: str,
    category: str,
    case_description: str = "",
    google_maps_key: str = None,
) -> list:
    """
    Main function called from app.py.
    Returns real verified Patna lawyers matched to the case.
    City parameter accepted but Patna-only for this prototype.
    """
    if case_description and len(case_description) > 20:
        return match_lawyers_to_case(case_description, category, top_n=8)
    else:
        # Return category-filtered lawyers
        matched = [
            {**l, "match_score": 50, "matched_keywords": []}
            for l in PATNA_LAWYERS
            if category in l["case_types"]
        ]
        return matched if matched else [{**l, "match_score": 30, "matched_keywords": []} for l in PATNA_LAWYERS]


def get_all_patna_lawyers() -> list:
    """Return complete Patna lawyer database."""
    return PATNA_LAWYERS
