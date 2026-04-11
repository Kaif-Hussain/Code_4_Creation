"""
cases_data.py
Local case database + lawyer data for LexMatch AI
Patna, Bihar Edition — Hackathon 2026
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

# Static lawyer reference (for PDF generation fallback)
LAWYERS = {
    "Adv. Jitendra Kumar": {
        "phone": "+91-9570723474",
        "email": "lawrato.com/advocate-jitendra-kumar-patna",
        "specialization": "Criminal & Civil Law",
        "experience": "12+ years",
        "rating": "Top Rated",
        "wins": "1000+ cases",
        "losses": "N/A",
        "charges": "Contact directly",
        "office": "State Bar Council Bhawan, Near Patna High Court",
    },
    "Kaushal Kumar Jha (Tarakant Jha & Associates)": {
        "phone": "tarakantjhaandassociates.com",
        "email": "tarakantjhaandassociates.com",
        "specialization": "All Areas of Law",
        "experience": "30+ years (Firm since 1956)",
        "rating": "Senior Advocate",
        "wins": "35,000+ cases",
        "losses": "N/A",
        "charges": "Contact directly",
        "office": "East Boring Canal Road, Nageshwar Colony, Patna",
    },
}


def _derive_expertise(specialization: str) -> list:
    text = (specialization or "").lower()
    keywords = set()

    if "criminal" in text:
        keywords.update(["criminal", "bail", "fir", "trial", "ipc"])
    if "civil" in text:
        keywords.update(["civil", "property", "injunction", "contract"])
    if "family" in text:
        keywords.update(["family", "divorce", "custody", "maintenance"])
    if "corporate" in text:
        keywords.update(["corporate", "company", "compliance", "commercial"])
    if "constitutional" in text:
        keywords.update(["constitutional", "writ", "article", "fundamental rights"])
    if "environment" in text:
        keywords.update(["environmental", "pollution", "ngt", "water"])

    return sorted(keywords)


# Backward-compatible export used by lawyer_scraper.py
PATNA_LAWYERS = [
    {
        "id": f"PL-{index:03d}",
        "name": name,
        "city": "Patna",
        "specialization": info.get("specialization", "General Law"),
        "experience": info.get("experience", "N/A"),
        "rating": info.get("rating", "N/A"),
        "wins": info.get("wins", "N/A"),
        "losses": info.get("losses", "N/A"),
        "charges": info.get("charges", "N/A"),
        "phone": info.get("phone", "N/A"),
        "email": info.get("email", "N/A"),
        "court": "Patna High Court",
        "address": info.get("office", "Patna, Bihar"),
        "expertise": _derive_expertise(info.get("specialization", "")),
    }
    for index, (name, info) in enumerate(LAWYERS.items(), start=1)
]
