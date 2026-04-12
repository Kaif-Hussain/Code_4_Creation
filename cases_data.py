"""
cases_data.py
Local case database + lawyer data for LexMatch AI
Patna, Bihar Edition — Hackathon 2026
Lawyer data sourced from freelaw.in/advocates/directory (Bihar)
"""

LOCAL_CASES = [
    {
        "id": "LC-2024-001",
        "title": "State vs. Rahman — Corporate Fraud & Embezzlement",
        "category": "criminal",
        "year": 2024,
        "court": "Patna High Court",
        "summary": "Corporate executive charged with embezzling ₹2.3Cr from company funds using forged documents and fake vendor invoices over 3 years. Digital evidence and whistleblower testimony used.",
        "outcome": "Convicted",
        "sentence": "5 years imprisonment + ₹50L fine",
        "key_facts": ["fraud", "embezzlement", "forged documents", "digital evidence", "corporate"],
        "lawyer": None,
        "source": "📁 Local DB",
    },
    {
        "id": "LC-2023-088",
        "title": "Mehta vs. BuildCorp — Property & Builder Fraud",
        "category": "civil",
        "year": 2023,
        "court": "Bihar District Court",
        "summary": "Builder took full payment but failed to deliver promised property. 47 victims involved. Landmark ruling on builder liability under RERA.",
        "outcome": "Judgment for Petitioner",
        "sentence": "Full refund + 12% interest + ₹2L damages",
        "key_facts": ["property", "builder", "breach of contract", "refund", "RERA"],
        "lawyer": None,
        "source": "📁 Local DB",
    },
    {
        "id": "LC-2024-045",
        "title": "Gupta vs. Gupta — Divorce, Custody & Domestic Violence",
        "category": "family",
        "year": 2024,
        "court": "Family Court Patna",
        "summary": "High-conflict divorce with child custody dispute, domestic abuse allegations under DV Act, and ₹40L asset division. Section 498A also invoked.",
        "outcome": "Custody to Mother",
        "sentence": "Assets split 60-40, monthly alimony ₹25,000",
        "key_facts": ["divorce", "custody", "domestic abuse", "498A", "alimony", "DV act"],
        "lawyer": None,
        "source": "📁 Local DB",
    },
    {
        "id": "LC-2023-211",
        "title": "TechCo vs. Ex-CTO — Trade Secret & IP Theft",
        "category": "corporate",
        "year": 2023,
        "court": "Delhi High Court",
        "summary": "Former CTO stole trade secrets and proprietary source code worth ₹5Cr before joining competitor startup. Emergency injunction filed.",
        "outcome": "Injunction Granted",
        "sentence": "Permanent injunction + ₹2Cr damages",
        "key_facts": ["intellectual property", "trade secret", "source code", "employee", "corporate", "injunction"],
        "lawyer": None,
        "source": "📁 Local DB",
    },
    {
        "id": "LC-2022-178",
        "title": "Citizens vs. Municipal Corp — PIL Housing Rights",
        "category": "constitutional",
        "year": 2022,
        "court": "Patna High Court",
        "summary": "PIL against illegal demolition of 200 homes without prior notice. Right to shelter under Article 21 and due process rights invoked.",
        "outcome": "Relief Granted",
        "sentence": "Demolition stayed, compensation ordered",
        "key_facts": ["PIL", "demolition", "housing", "Article 21", "fundamental rights", "municipal"],
        "lawyer": None,
        "source": "📁 Local DB",
    },
    {
        "id": "LC-2024-033",
        "title": "River Alliance vs. Industrial Zone — NGT Pollution",
        "category": "environmental",
        "year": 2024,
        "court": "NGT East Zone Kolkata",
        "summary": "Factory discharging toxic effluents into Ganga river, killing fish and contaminating drinking water in 3 villages. Satellite imagery as evidence.",
        "outcome": "Operations Stayed",
        "sentence": "Interim stay on factory + ₹1Cr fine",
        "key_facts": ["pollution", "river", "factory", "NGT", "toxic", "Ganga", "environment"],
        "lawyer": None,
        "source": "📁 Local DB",
    },
    {
        "id": "LC-2023-156",
        "title": "State vs. Singh — Blackmail & Extortion",
        "category": "criminal",
        "year": 2023,
        "court": "Sessions Court Patna",
        "summary": "Accused recorded private conversation without consent and demanded ₹5L threatening to leak it. WhatsApp evidence and bank transfer receipts used. Section 384 IPC applied.",
        "outcome": "Convicted",
        "sentence": "3 years imprisonment + ₹1L fine",
        "key_facts": ["blackmail", "extortion", "threat", "Section 384", "WhatsApp", "private conversation"],
        "lawyer": None,
        "source": "📁 Local DB",
    },
    {
        "id": "LC-2022-099",
        "title": "Patel vs. InsureCorp — Medical Insurance Claim Denial",
        "category": "civil",
        "year": 2022,
        "court": "Consumer Forum Bihar",
        "summary": "Insurance company wrongfully denied ₹15L medical claim citing pre-existing condition clause unfairly. Consumer court escalated to State Commission.",
        "outcome": "Judgment for Petitioner",
        "sentence": "Full claim + ₹1L compensation for mental harassment",
        "key_facts": ["insurance", "medical claim", "denial", "consumer", "hospital", "health insurance"],
        "lawyer": None,
        "source": "📁 Local DB",
    },
    {
        "id": "LC-2023-302",
        "title": "Kumar vs. Employer — Wrongful Termination",
        "category": "corporate",
        "year": 2023,
        "court": "Labour Court Patna",
        "summary": "Employee terminated without cause after filing workplace harassment complaint. Retaliation clearly evidenced through email trail. 5 years tenure without prior warnings.",
        "outcome": "Reinstatement Ordered",
        "sentence": "Reinstatement + back wages + ₹50,000 compensation",
        "key_facts": ["termination", "harassment", "workplace", "labour law", "retaliation", "employment"],
        "lawyer": None,
        "source": "📁 Local DB",
    },
    {
        "id": "LC-2024-088",
        "title": "State vs. Cybercrime Gang — Online Fraud",
        "category": "criminal",
        "year": 2024,
        "court": "Sessions Court Patna",
        "summary": "Gang of 5 defrauded 200+ victims through fake investment apps totaling ₹1.2Cr. Cyber forensics, device seizure and digital banking evidence used.",
        "outcome": "Convicted",
        "sentence": "4-6 years for each accused",
        "key_facts": ["cyber fraud", "online fraud", "investment scam", "digital evidence", "cyber crime", "IT Act"],
        "lawyer": None,
        "source": "📁 Local DB",
    },
]

CATEGORIES = [
    {
        "id": "criminal",
        "label": "Criminal Law",
        "icon": "⚖️",
        "sub": ["FIR & Bail", "Fraud & Cheating", "Assault & Violence", "Blackmail & Extortion",
                "Cyber Crime", "Drug Offenses", "Murder Defense", "Corruption & PMLA"],
    },
    {
        "id": "civil",
        "label": "Civil Litigation",
        "icon": "📜",
        "sub": ["Contract Dispute", "Property", "Insurance Claim", "Defamation",
                "Cheque Bounce", "Debt Recovery", "Consumer Complaint"],
    },
    {
        "id": "family",
        "label": "Family Law",
        "icon": "🏛️",
        "sub": ["Divorce", "Child Custody", "Domestic Violence", "Alimony & Maintenance",
                "498A Cases", "Adoption", "Court Marriage"],
    },
    {
        "id": "corporate",
        "label": "Corporate Law",
        "icon": "🏢",
        "sub": ["IP & Trade Secret", "Employment Dispute", "Company Compliance",
                "Mergers & Acquisition", "Startup Legal", "RERA & Builder"],
    },
    {
        "id": "constitutional",
        "label": "Constitutional",
        "icon": "📋",
        "sub": ["PIL", "Fundamental Rights", "RTI", "Due Process", "Writ Petition",
                "Equal Protection", "Habeas Corpus"],
    },
    {
        "id": "environmental",
        "label": "Environmental",
        "icon": "🌿",
        "sub": ["NGT Petition", "Pollution Complaint", "Land Use", "Wildlife Protection",
                "Industrial Violations", "Water Contamination"],
    },
]

# ─────────────────────────────────────────────
# EXPERTISE KEYWORD MAPPING  (used for filtering)
# ─────────────────────────────────────────────
CATEGORY_KEYWORDS = {
    "criminal":       ["criminal", "bail", "fir", "ipc", "fraud", "extortion", "crime",
                       "cyber", "murder", "cheating", "section 420", "section 302"],
    "civil":          ["civil", "property", "contract", "injunction", "consumer", "insurance",
                       "cheque", "debt", "defamation", "recovery", "rera"],
    "family":         ["family", "divorce", "custody", "matrimonial", "498a", "dv act",
                       "alimony", "maintenance", "adoption", "domestic"],
    "corporate":      ["corporate", "company", "commercial", "labour", "employment",
                       "ip", "trade secret", "startup", "compliance", "arbitration"],
    "constitutional": ["constitutional", "writ", "article 21", "fundamental rights",
                       "pil", "rti", "habeas corpus", "due process"],
    "environmental":  ["environment", "pollution", "ngt", "water", "forest", "wildlife",
                       "green", "effluent", "ganga"],
}


def _derive_expertise(qualification: str, specialization: str = "") -> list:
    """Derive expertise tags from qualification + specialization text."""
    text = (qualification + " " + specialization).lower()
    tags = set()

    if any(w in text for w in ["criminal", "ipc", "crpc"]):
        tags.add("criminal")
    if any(w in text for w in ["civil", "property", "consumer"]):
        tags.add("civil")
    if any(w in text for w in ["family", "matrimonial", "divorce"]):
        tags.add("family")
    if any(w in text for w in ["corporate", "company", "commercial", "labour", "llm"]):
        tags.add("corporate")
    if any(w in text for w in ["constitutional", "writ", "pil"]):
        tags.add("constitutional")
    if any(w in text for w in ["environment", "ngt", "pollution"]):
        tags.add("environmental")

    # Default — every advocate can handle general civil/criminal
    if not tags:
        tags.update(["criminal", "civil"])

    return sorted(tags)


def match_lawyers_to_category(category: str, city: str = "") -> list:
    """
    Return PATNA_LAWYERS filtered by category expertise.
    Optionally filter by city (case-insensitive substring match).
    Always falls back to all lawyers if no exact match found.
    """
    category = (category or "").lower()
    city = (city or "").strip().lower()

    matched = [
        l for l in PATNA_LAWYERS
        if category in l["expertise"]
        and (not city or city in l["city"].lower() or city in l["address"].lower())
    ]

    if not matched:
        # Fallback: city match only
        matched = [
            l for l in PATNA_LAWYERS
            if not city or city in l["city"].lower() or city in l["address"].lower()
        ]

    if not matched:
        # Final fallback: return all
        matched = PATNA_LAWYERS[:]

    return matched


# ─────────────────────────────────────────────
# REAL LAWYER DATA  — sourced from freelaw.in
# Bihar Advocates Directory (verified profiles)
# ─────────────────────────────────────────────
LAWYERS_RAW = [
    {
        "name": "Adv. Pulkit Ranjan",
        "city": "Patna",
        "district": "Patna",
        "phone": "9471671044",
        "qualification": "LLB",
        "specialization": "General Law",
        "verified": True,
    },
    {
        "name": "Adv. Parvind Kumar",
        "city": "Patna",
        "district": "Patna",
        "phone": "9430624784",
        "qualification": "LLB",
        "specialization": "General Law",
        "verified": True,
    },
    {
        "name": "Adv. Sonu Kumar",
        "city": "Bihar Sharif",
        "district": "Nalanda",
        "phone": "9934229011",
        "qualification": "LLB",
        "specialization": "General Law",
        "verified": True,
    },
    {
        "name": "Adv. Mithilesh Kumar",
        "city": "Patna",
        "district": "Patna",
        "phone": "9835272595",
        "qualification": "LLB",
        "specialization": "Civil & Criminal Law",
        "verified": True,
    },
    {
        "name": "Adv. Amit Kumar",
        "city": "Gopalganj",
        "district": "Gopalganj",
        "phone": "9911806308",
        "qualification": "LLB",
        "specialization": "Criminal Law",
        "verified": True,
    },
    {
        "name": "Adv. Abneesh Kumar",
        "city": "Patna",
        "district": "Patna",
        "phone": "7903231571",
        "qualification": "LLB",
        "specialization": "Criminal & Civil Law",
        "verified": True,
    },
    {
        "name": "Adv. Vikky Kumar",
        "city": "Muzaffarpur",
        "district": "Muzaffarpur",
        "phone": "9939743606",
        "qualification": "LLB",
        "specialization": "Criminal Law",
        "verified": True,
    },
    {
        "name": "Adv. Rajesh Roushan",
        "city": "Bihar Sharif",
        "district": "Nalanda",
        "phone": "8709751876",
        "qualification": "LLB",
        "specialization": "Civil Law",
        "verified": True,
    },
    {
        "name": "Adv. Kumar Kaushlendra",
        "city": "Patna",
        "district": "Patna",
        "phone": "7277411257",
        "qualification": "LLB",
        "specialization": "Corporate & Commercial Law",
        "verified": False,
    },
    {
        "name": "Adv. Raj Sinha",
        "city": "Muzaffarpur",
        "district": "Muzaffarpur",
        "phone": "9905400151",
        "qualification": "LL.M.",
        "specialization": "Constitutional & Civil Law",
        "verified": False,
    },
    {
        "name": "Adv. Rakesh Kumar",
        "city": "Siwan",
        "district": "Siwan",
        "phone": "9771438478",
        "qualification": "B.A. LLB",
        "specialization": "Criminal Law",
        "verified": False,
    },
    {
        "name": "Adv. Subroteswar De",
        "city": "Patna",
        "district": "Patna",
        "phone": "9934269367",
        "qualification": "LLB",
        "specialization": "Civil & Property Law",
        "verified": False,
    },
    {
        "name": "Adv. Randhir Kumar",
        "city": "Patna",
        "district": "Patna",
        "phone": "9308208630",
        "qualification": "LLB",
        "specialization": "Criminal Law",
        "verified": False,
    },
    {
        "name": "Adv. Pawan Verma",
        "city": "Patna",
        "district": "Patna",
        "phone": "9546975768",
        "qualification": "B.A. LLB",
        "specialization": "Civil & Criminal Law",
        "verified": False,
    },
    {
        "name": "Adv. Jitendra Kumar",
        "city": "Bhagalpur",
        "district": "Bhagalpur",
        "phone": "9939704743",
        "qualification": "LLB MCA MBA",
        "specialization": "Cyber Law & Corporate Law",
        "verified": False,
    },
    {
        "name": "Adv. Rakesh Kumar (Patna HC)",
        "city": "Patna",
        "district": "Patna",
        "phone": "9431033175",
        "qualification": "M.Sc., LLB, M.A.",
        "specialization": "Civil & Constitutional Law",
        "verified": False,
    },
    {
        "name": "Adv. Manmohan Krishna",
        "city": "Nawada",
        "district": "Nawada",
        "phone": "9304303325",
        "qualification": "B.Sc. & LLB",
        "specialization": "Criminal & Civil Law",
        "verified": False,
    },
    {
        "name": "Adv. Sunil Kumar",
        "city": "Gaya",
        "district": "Gaya",
        "phone": "7739727141",
        "qualification": "M.Sc., MBA (Finance), LLM, CAIIB",
        "specialization": "Corporate, Banking & Commercial Law",
        "verified": False,
    },
    {
        "name": "Adv. Syed Mohammad Masihur Rehman",
        "city": "Patna",
        "district": "Patna",
        "phone": "9431019396",
        "qualification": "LL.B",
        "specialization": "Family & Criminal Law",
        "verified": False,
    },
    {
        "name": "Adv. Sanjay Kumar",
        "city": "Patna",
        "district": "Patna",
        "phone": "8581806948",
        "qualification": "LL.B",
        "specialization": "Civil & Criminal Law",
        "verified": False,
    },
    {
        "name": "Adv. Md Khurshid Alam",
        "city": "Patna",
        "district": "Patna",
        "phone": "9470736302",
        "qualification": "LL.B (Hons.)",
        "specialization": "Criminal & Civil Law",
        "verified": False,
    },
    {
        "name": "Adv. Abhishek Mishra",
        "city": "Patna",
        "district": "Patna",
        "phone": "9572190419",
        "qualification": "LL.B",
        "specialization": "Civil & Property Law",
        "verified": False,
    },
    {
        "name": "Adv. Vikash Kumar Singh",
        "city": "Patna",
        "district": "Patna",
        "phone": "9523425020",
        "qualification": "BA LLB",
        "specialization": "Criminal & Labour Law",
        "verified": False,
    },
    {
        "name": "Adv. Mrinal Shankar",
        "city": "Muzaffarpur",
        "district": "Muzaffarpur",
        "phone": "6203405774",
        "qualification": "LL.B",
        "specialization": "Criminal Law",
        "verified": False,
    },
    {
        "name": "Adv. Ashutosh Singh",
        "city": "Bhagalpur",
        "district": "Bhagalpur",
        "phone": "8210351724",
        "qualification": "LL.B",
        "specialization": "Criminal & Civil Law",
        "verified": False,
    },
    {
        "name": "Adv. Shashank Kumar Sinha",
        "city": "Saharsa",
        "district": "Saharsa",
        "phone": "9065840707",
        "qualification": "LL.B",
        "specialization": "Civil Law",
        "verified": False,
    },
    {
        "name": "Adv. Amarjeet S Hriday Singh",
        "city": "Khagaria",
        "district": "Khagaria",
        "phone": "9473382401",
        "qualification": "LL.B",
        "specialization": "Civil & Criminal Law",
        "verified": False,
    },
    {
        "name": "Adv. Sudhanshu Kumar",
        "city": "Arrah",
        "district": "Bhojpur",
        "phone": "9631259492",
        "qualification": "LLB",
        "specialization": "Criminal & Civil Law",
        "verified": False,
    },
    {
        "name": "Adv. Vikash Kumar",
        "city": "Gaya",
        "district": "Gaya",
        "phone": "7503528984",
        "qualification": "B.Com, LL.B., PGDIPR",
        "specialization": "Intellectual Property & Corporate Law",
        "verified": False,
    },
    {
        "name": "Adv. Anuranjan Patel",
        "city": "Patna",
        "district": "Patna",
        "phone": "8969573056",
        "qualification": "M.Sc., LLB",
        "specialization": "Civil & Criminal Law",
        "verified": False,
    },
    {
        "name": "Adv. Kundan Kumar",
        "city": "Patna",
        "district": "Patna",
        "phone": "8210870963",
        "qualification": "LLB",
        "specialization": "Criminal Law",
        "verified": False,
    },
    {
        "name": "Adv. Md Atif Ahsan",
        "city": "Patna",
        "district": "Patna",
        "phone": "8582050888",
        "qualification": "MBA, LLB",
        "specialization": "Corporate & Civil Law",
        "verified": False,
    },
    {
        "name": "Adv. Praful Ranjan",
        "city": "Patna",
        "district": "Patna",
        "phone": "9431072649",
        "qualification": "M.Com, LLB",
        "specialization": "Corporate, Commercial & Civil Law",
        "verified": False,
    },
    {
        "name": "Adv. Anmol Ratan",
        "city": "Hajipur",
        "district": "Vaishali",
        "phone": "9430293103",
        "qualification": "LLB",
        "specialization": "Civil & Criminal Law",
        "verified": False,
    },
    {
        "name": "Adv. Hareram Kumar",
        "city": "Motihari",
        "district": "East Champaran",
        "phone": "8507175823",
        "qualification": "LLB",
        "specialization": "Criminal & Civil Law",
        "verified": False,
    },
    {
        "name": "Adv. Ankit Raj",
        "city": "Dalsingsarai",
        "district": "Samastipur",
        "phone": "6205032891",
        "qualification": "BA LLB",
        "specialization": "Criminal Law",
        "verified": False,
    },
    {
        "name": "Adv. Md Khurshid Ansari",
        "city": "Katihar",
        "district": "Katihar",
        "phone": "9931008950",
        "qualification": "LLB",
        "specialization": "Civil & Criminal Law",
        "verified": False,
    },
    {
        "name": "Adv. Raj Kumar Mishra",
        "city": "Patna",
        "district": "Patna",
        "phone": "9304179710",
        "qualification": "LL.M",
        "specialization": "Constitutional & Civil Law",
        "verified": False,
    },
    {
        "name": "Adv. Md Reyaj",
        "city": "Hajipur",
        "district": "Vaishali",
        "phone": "8804446545",
        "qualification": "BA LLB",
        "specialization": "Criminal & Family Law",
        "verified": False,
    },
    {
        "name": "Adv. Abhishek Kumar",
        "city": "Patna",
        "district": "Patna",
        "phone": "9471433052",
        "qualification": "B.A. LLB",
        "specialization": "Civil & Criminal Law",
        "verified": False,
    },
    {
        "name": "Adv. Shubham Kumar Mishra",
        "city": "Siwan",
        "district": "Siwan",
        "phone": "7979842409",
        "qualification": "LLB",
        "specialization": "Criminal Law",
        "verified": False,
    },
    {
        "name": "Adv. Ram Pratik Choubey",
        "city": "Buxar",
        "district": "Buxar",
        "phone": "8271566348",
        "qualification": "BA (Hons) LL.B",
        "specialization": "Civil & Criminal Law",
        "verified": False,
    },
    {
        "name": "Adv. Nitish Kumar",
        "city": "Samastipur",
        "district": "Samastipur",
        "phone": "9709907573",
        "qualification": "LL.B",
        "specialization": "Civil Law",
        "verified": False,
    },
    {
        "name": "Adv. Bibhuti Anand Jha",
        "city": "Patna",
        "district": "Patna",
        "phone": "9304942428",
        "qualification": "LL.M",
        "specialization": "Constitutional, Civil & Criminal Law",
        "verified": False,
    },
    {
        "name": "Adv. Prakash Kumar Dubey",
        "city": "Bettiah",
        "district": "West Champaran",
        "phone": "9122924131",
        "qualification": "B.Sc. LLB",
        "specialization": "Criminal & Civil Law",
        "verified": False,
    },
    {
        "name": "Adv. Praveen Kumar",
        "city": "Ara",
        "district": "Bhojpur",
        "phone": "8677859704",
        "qualification": "BBA LLB",
        "specialization": "Corporate & Criminal Law",
        "verified": False,
    },
    {
        "name": "Adv. Anand Shekhar",
        "city": "Purnia",
        "district": "Purnia",
        "phone": "9910395606",
        "qualification": "LLB",
        "specialization": "Civil & Criminal Law",
        "verified": False,
    },
    {
        "name": "Adv. Vikas",
        "city": "Munger",
        "district": "Munger",
        "phone": "9334033953",
        "qualification": "M.Com & LL.B",
        "specialization": "Corporate, Commercial & Civil Law",
        "verified": False,
    },
    {
        "name": "Adv. Daud Ali",
        "city": "Siwan",
        "district": "Siwan",
        "phone": "7050911786",
        "qualification": "LLB",
        "specialization": "Criminal & Family Law",
        "verified": False,
    },
    {
        "name": "Adv. Brijmohan Bhagat",
        "city": "Jamui",
        "district": "Jamui",
        "phone": "8210505522",
        "qualification": "M.A. (LL.B)",
        "specialization": "Civil & Constitutional Law",
        "verified": False,
    },
    {
        "name": "Adv. Rakesh Kumar Patel",
        "city": "Bettiah",
        "district": "West Champaran",
        "phone": "7667708138",
        "qualification": "LLB",
        "specialization": "Civil & Criminal Law",
        "verified": False,
    },
]


# Build structured PATNA_LAWYERS list (used throughout app.py)
PATNA_LAWYERS = [
    {
        "id": f"FL-{idx:03d}",
        "name": l["name"],
        "city": l["city"],
        "district": l["district"],
        "specialization": l["specialization"],
        "qualification": l["qualification"],
        "experience": "Registered Advocate",
        "rating": "✅ Verified" if l["verified"] else "Registered",
        "wins": "N/A",
        "phone": l["phone"],
        "email": "N/A",
        "court": "Bihar Bar Council",
        "address": f"{l['city']}, {l['district']}, Bihar",
        "source": "freelaw.in",
        "expertise": _derive_expertise(l["qualification"], l["specialization"]),
    }
    for idx, l in enumerate(LAWYERS_RAW, start=1)
]


# Legacy alias kept for backward compatibility with pdf_report.py
LAWYERS = {
    l["name"]: {
        "phone": l["phone"],
        "email": l["email"],
        "specialization": l["specialization"],
        "experience": l["experience"],
        "rating": l["rating"],
        "wins": l["wins"],
        "losses": "N/A",
        "charges": "Contact directly",
        "office": l["address"],
    }
    for l in PATNA_LAWYERS
}
