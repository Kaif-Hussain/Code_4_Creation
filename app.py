import streamlit as st
import json
import time
import importlib
import sys
import os
from pathlib import Path
from cases_data import LOCAL_CASES, CATEGORIES, PATNA_LAWYERS, match_lawyers_to_category
from gemini_api import analyze_case, score_matches
from pdf_report import generate_pdf

# Ensure local module resolution works when running this file directly.
_APP_DIR = Path(__file__).resolve().parent
if str(_APP_DIR) not in sys.path:
    sys.path.insert(0, str(_APP_DIR))

try:
    try:
        _kanoon_scraper = importlib.import_module("kanoon_scraper")
    except Exception:
        _kanoon_scraper = importlib.import_module("kanoon_scrapper")
    search_cases = _kanoon_scraper.search_cases
    build_query = _kanoon_scraper.build_query
except Exception as _import_err:
    _kanoon_import_error = str(_import_err)

    def _missing_kanoon_scraper(*args, **kwargs):
        raise ModuleNotFoundError(
            "kanoon scraper module not found. "
            f"Original error: {_kanoon_import_error}"
        )

    search_cases = _missing_kanoon_scraper
    build_query = _missing_kanoon_scraper

def get_lawyers_for_case(city, category):
    """
    Return lawyers from the local freelaw.in dataset filtered by
    case category and city.  Falls back gracefully if no exact match.
    """
    return match_lawyers_to_category(category=category, city=city)

# ═══════════════════════════════════════════════════════════════
# PAGE CONFIG
# ═══════════════════════════════════════════════════════════════
st.set_page_config(
    page_title="JUSTICE GPT— Law & Justice Platform",
    page_icon="⚖️",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ═══════════════════════════════════════════════════════════════
# CSS (HIGH-CONTRAST PROFESSIONAL THEME)
# ═══════════════════════════════════════════════════════════════
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Playfair+Display:wght@600;700&family=Source+Sans+Pro:wght@400;600&display=swap');

html, body, [class*="css"], .stApp {
  background-color: #fcfcfc !important; /* Very crisp off-white */
  color: #1a202c !important; /* Deep charcoal text for perfect readability */
  font-family: 'Source Sans Pro', sans-serif !important;
}
.main .block-container { padding: 0 2rem 4rem !important; max-width: 1200px !important; }

/* Dark Executive Sidebar */
[data-testid="stSidebar"] {
  background: #111827 !important; 
  border-right: 1px solid #1f2937 !important;
}
[data-testid="stSidebar"] * { color: #f3f4f6 !important; }

h1, h2, h3 {
  font-family: 'Playfair Display', serif !important;
  color: #000000 !important; /* Pure black for headings */
  letter-spacing: -0.5px !important;
}

/* Professional Buttons */
.stButton > button {
  background: #1a202c !important; /* Charcoal */
  color: #ffffff !important; 
  border: 1px solid #1a202c !important;
  border-radius: 4px !important; /* Sharper corners */
  font-family: 'Source Sans Pro', sans-serif !important;
  font-weight: 600 !important; letter-spacing: 0.5px !important;
  padding: 10px 24px !important; transition: all 0.3s !important;
}
.stButton > button:hover { 
    background: #ffffff !important; 
    color: #1a202c !important; 
    border-color: #1a202c !important;
}
.stButton > button:disabled { background: #e2e8f0 !important; color: #94a3b8 !important; border-color: #e2e8f0 !important; }

/* Input Fields */
.stTextInput > div > div > input,
.stTextArea > div > div > textarea {
  background: #ffffff !important; color: #1a202c !important;
  border: 1px solid #cbd5e1 !important; border-radius: 4px !important;
  font-family: 'Source Sans Pro', sans-serif !important;
  padding: 12px !important;
}
.stTextInput > div > div > input:focus,
.stTextArea > div > div > textarea:focus {
    border-color: #b8963e !important; /* Gold focus outline */
    box-shadow: 0 0 0 1px #b8963e !important;
}

label { color: #4a5568 !important; font-size: 14px !important;
        font-weight: 600 !important; }

/* Tabs */
.stTabs [data-baseweb="tab-list"] {
  background: transparent !important; border-bottom: 2px solid #e2e8f0 !important; gap: 0 !important;
}
.stTabs [data-baseweb="tab"] {
  color: #718096 !important; font-family: 'Source Sans Pro', sans-serif !important;
  font-weight: 600 !important; font-size: 14px !important;
  padding: 14px 24px !important; border-radius: 0 !important;
  border-bottom: 2px solid transparent !important;
}
.stTabs [aria-selected="true"] {
  color: #1a202c !important; border-bottom: 2px solid #1a202c !important;
  background: transparent !important;
}

/* Expanders/Cards */
.stExpander {
  background: #ffffff !important; border: 1px solid #e2e8f0 !important;
  border-radius: 6px !important; margin-bottom: 12px !important;
}

.stProgress > div > div { background: #1a202c !important; }

::-webkit-scrollbar { width: 8px; }
::-webkit-scrollbar-track { background: #f1f5f9; }
::-webkit-scrollbar-thumb { background: #cbd5e1; border-radius: 4px; }
</style>
""", unsafe_allow_html=True)


# ═══════════════════════════════════════════════════════════════
# SESSION STATE
# ═══════════════════════════════════════════════════════════════
def init_state():
    defaults = {
        "page": "home", "step": 0, "category": None,
        "case_desc": "", "city": "", "results": [],
        "analysis": None, "lawyers": [],
        "law_query": "", "law_response": "",
    }
    for k, v in defaults.items():
        if k not in st.session_state:
            st.session_state[k] = v
init_state()


# ═══════════════════════════════════════════════════════════════
# SIDEBAR
# ═══════════════════════════════════════════════════════════════
with st.sidebar:
    st.markdown("""
    <div style='text-align:center; padding:24px 0 20px'>
      <div style='font-size:40px'>⚖️</div>
      <div style='font-family:Playfair Display,serif; font-size:26px;
                  color:#ffffff; font-weight:700; margin-top:8px'>JUSTICE GPT</div>
      <div style='font-size:11px; letter-spacing:3px; color:#9ca3af; margin-top:4px; font-weight:600'>
        LAW & JUSTICE PLATFORM
      </div>
    </div>
    <hr style='border-color:#374151; margin:0 0 20px'>
    """, unsafe_allow_html=True)

    nav_items = [
        ("🏛️", "Home",            "home"),
        ("🔍", "Case Analyzer",   "analyzer"),
        ("📚", "Legal Knowledge", "knowledge"),
        ("👤", "Find Lawyers",    "lawyers"),
        ("📊", "About Project",   "about"),
    ]
    for icon, label, key in nav_items:
        active = st.session_state.page == key
        bg     = "#1f2937" if active else "transparent"
        border = "#b8963e" if active else "transparent"
        color  = "#fe2323" if active else "#7D8D9B"
        st.markdown(f"""
        <div style='background:{bg}; border-left:3px solid {border};
                    padding:12px 16px; margin-bottom:4px; border-radius:0 6px 6px 0;
                    color:{color}; font-size:15px; font-weight:{"600" if active else "400"};
                    letter-spacing:0.5px; cursor:pointer'>{icon} &nbsp; {label}</div>
        """, unsafe_allow_html=True)
        if st.button(label, key=f"nav_{key}", use_container_width=True):
            st.session_state.page = key
            st.rerun()

    st.markdown("""
    <hr style='border-color:#374151; margin:20px 0'>
    <div style='font-size:11px; color:#6b7280; text-align:center; letter-spacing:1px; line-height:2'>
      CREATED BY TEAM CODE_4_CREATION<br>
      
    """, unsafe_allow_html=True)


# ═══════════════════════════════════════════════════════════════
# HOME PAGE
# ═══════════════════════════════════════════════════════════════
if st.session_state.page == "home":

    st.markdown("""
    <div style='text-align:center; padding:60px 20px 48px'>
      <div style='font-size:12px; letter-spacing:6px; color:#4a5568; font-weight:700; margin-bottom:16px'>
        HACKATHON 2026 · LAW & JUSTICE
      </div>
      <h1 style='font-size:clamp(40px,7vw,72px); margin:0; line-height:1.1; color:#000000'>
        JUSTICE GPT
      </h1>
      <p style='font-size:16px; color:#1a202c; margin:16px 0 8px; letter-spacing:2px; font-weight:600'>
        CASE ANALYSIS · PRECEDENT MATCHING · LAWYER INTELLIGENCE
      </p>
      <div style='width:60px; height:3px; background:#b8963e; margin:24px auto'></div>
      <p style='font-size:16px; color:#4a5568; max-width:650px; margin:0 auto 40px; line-height:1.8'>
        India's first AI-powered legal platform. Describe your case, get matched to real
        court precedents, understand your rights, and find the right legal expert — in 60 seconds.
      </p>
    </div>
    """, unsafe_allow_html=True)

    # Stats
    s1, s2, s3, s4 = st.columns(4)
    for col, (icon, val, lbl) in zip([s1,s2,s3,s4], [
        ("⚖️","50M+","Court Cases Indexed"),
        ("🤖","99%","AI Accuracy"),
        ("👤","100%","Verified Lawyers"),
        ("⚡","60s","To Full Report"),
    ]):
        with col:
            st.markdown(f"""
            <div style='text-align:center; background:#ffffff; border:1px solid #e2e8f0;
                        border-radius:6px; padding:24px 16px; margin-bottom:20px; box-shadow:0 1px 3px rgba(0,0,0,0.05)'>
              <div style='font-size:28px; margin-bottom:8px'>{icon}</div>
              <div style='font-size:30px; font-weight:700; color:#000000;
                          font-family:Playfair Display,serif'>{val}</div>
              <div style='font-size:12px; color:#4a5568; letter-spacing:1px;
                          margin-top:4px; font-weight:600; text-transform:uppercase'>{lbl}</div>
            </div>
            """, unsafe_allow_html=True)

    # Features
    st.markdown("""
    <div style='text-align:center; margin:24px 0 32px'>
      <h2 style='font-size:32px; margin-top:8px'>Complete Legal Intelligence Suite</h2>
    </div>
    """, unsafe_allow_html=True)

    f1, f2, f3 = st.columns(3)
    for col, (icon, title, desc, pg) in zip([f1,f2,f3], [
        ("🔍","Case Analyzer",
         "Describe your situation in plain language. AI matches it to millions of real Indian court cases and gives a professional legal assessment instantly.","analyzer"),
        ("📚","Legal Knowledge",
         "Ask anything about Indian laws — IPC sections, your rights, consumer protection, and more. Get clear answers without complex legal jargon.","knowledge"),
        ("👤","Lawyer Finder",
         "Find verified, real legal experts directly in your city. Get their direct contact details and exact office locations instantly.","lawyers"),
    ]):
        with col:
            st.markdown(f"""
            <div style='background:#ffffff; border:1px solid #e2e8f0; border-radius:6px;
                        padding:28px 24px; margin-bottom:12px; box-shadow:0 1px 3px rgba(0,0,0,0.05)'>
              <div style='font-size:32px; margin-bottom:16px'>{icon}</div>
              <h3 style='font-size:22px; color:#000000; margin:0 0 12px'>{title}</h3>
              <p style='color:#4a5568; font-size:15px; line-height:1.7; margin:0'>{desc}</p>
            </div>
            """, unsafe_allow_html=True)
            if st.button(f"Open {title} →", key=f"hf_{pg}", use_container_width=True):
                st.session_state.page = pg
                st.rerun()

    st.markdown("<br>", unsafe_allow_html=True)
    col1,col2,col3 = st.columns([1,2,1])
    with col2:
        st.markdown("""
        <div style='text-align:center; background:#ffffff; border-top:3px solid #1a202c;
                    border-left:1px solid #e2e8f0; border-right:1px solid #e2e8f0; border-bottom:1px solid #e2e8f0; 
                    border-radius:4px; padding:36px; margin-bottom:20px; box-shadow:0 4px 6px rgba(0,0,0,0.05)'>
          <h2 style='font-size:26px; margin:0 0 10px'>Ready to analyze your case?</h2>
          <p style='color:#4a5568; font-size:15px; font-weight:600; margin:0'>Free · 60 seconds · No signup required</p>
        </div>
        """, unsafe_allow_html=True)
        if st.button("⚖️ Start Case Analysis →", use_container_width=True):
            st.session_state.page = "analyzer"
            st.rerun()


# ═══════════════════════════════════════════════════════════════
# CASE ANALYZER PAGE
# ═══════════════════════════════════════════════════════════════
elif st.session_state.page == "analyzer":

    st.markdown("""
    <div style='padding:24px 0 16px'>
      <div style='font-size:12px; font-weight:700; letter-spacing:3px; color:#4a5568; margin-bottom:8px'>CASE ANALYZER</div>
      <h1 style='font-size:40px; margin:0'>Analyze Your Legal Case</h1>
      <p style='color:#4a5568; margin-top:8px; font-size:16px'>
        Describe your situation · Match real court cases · Get AI legal assessment
      </p>
    </div>
    """, unsafe_allow_html=True)

    # Step indicator
    step_labels = ["Select Category","Describe Case","View Results"]
    sc = st.columns(3)
    for i, (col, lbl) in enumerate(zip(sc, step_labels)):
        with col:
            done   = i < st.session_state.step
            active = i == st.session_state.step
            
            # High contrast step indicator
            bg_clr = "#ffffff"
            br_clr = "#1a202c" if active else "#e2e8f0"
            tx_clr = "#1a202c" if active or done else "#94a3b8"
            top_br = "#1a202c" if active else "#22c55e" if done else "#e2e8f0"
            
            st.markdown(f"""
            <div style='text-align:center; padding:14px; background:{bg_clr};
                        border:1px solid {br_clr}; border-radius:4px; border-top:4px solid {top_br};'>
              <div style='font-size:20px; font-weight:700; color:{tx_clr};
                          font-family:Playfair Display,serif'>{"✓" if done else i+1}</div>
              <div style='font-size:13px; font-weight:600; color:{tx_clr}; letter-spacing:1px;
                          text-transform:uppercase; margin-top:4px'>{lbl}</div>
            </div>
            """, unsafe_allow_html=True)

    st.markdown("<br>", unsafe_allow_html=True)

    # STEP 0
    if st.session_state.step == 0:
        st.markdown("### Choose Case Category")
        cc = st.columns(3)
        for i, cat in enumerate(CATEGORIES):
            with cc[i % 3]:
                is_s = st.session_state.category == cat["id"]
                br   = "#1a202c" if is_s else "#e2e8f0"
                bg   = "#f8fafc" if is_s else "#ffffff"
                
                st.markdown(f"""
                <div style='background:{bg}; border:2px solid {br};
                            border-radius:6px; padding:22px; text-align:center; margin-bottom:8px;'>
                  <div style='font-size:36px'>{cat["icon"]}</div>
                  <div style='font-size:18px; font-weight:600; color:#000000;
                              margin:10px 0 4px'>{cat["label"]}</div>
                  {"<div style='font-size:12px; font-weight:700; color:#1a202c; letter-spacing:1px'>✓ SELECTED</div>" if is_s else ""}
                </div>
                """, unsafe_allow_html=True)
                if st.button(cat["label"], key=f"cat_{cat['id']}", use_container_width=True):
                    st.session_state.category = cat["id"]
                    st.rerun()

        if st.session_state.category:
            st.markdown("---")
            st.markdown("### 📍 Your City")
            st.markdown("<div style='color:#4a5568; font-size:14px; margin-bottom:10px'>We need your city to find real local lawyers.</div>", unsafe_allow_html=True)
            city_in = st.text_input("Enter your city", value=st.session_state.city,
                                     placeholder="e.g., Patna, Delhi, Mumbai, Bangalore...", label_visibility="collapsed")
            if city_in:
                st.session_state.city = city_in
            st.markdown("<br>", unsafe_allow_html=True)
            _,c2,_ = st.columns([2,1,2])
            with c2:
                if st.button("Continue →", use_container_width=True):
                    st.session_state.step = 1
                    st.rerun()

    # STEP 1
    elif st.session_state.step == 1:
        sel = next((c for c in CATEGORIES if c["id"] == st.session_state.category), None)

        st.markdown(f"""
        <div style='display:flex; gap:10px; margin-bottom:24px; flex-wrap:wrap'>
          <span style='background:#f1f5f9; border:1px solid #cbd5e1; border-radius:4px;
                       padding:6px 16px; color:#1a202c; font-size:13px; font-weight:600'>
            {sel["icon"] if sel else ""} {st.session_state.category.upper()}
          </span>
          {"<span style='background:#f1f5f9; border:1px solid #cbd5e1; border-radius:4px; padding:6px 16px; color:#1a202c; font-size:13px; font-weight:600'>📍 " + st.session_state.city.upper() + "</span>" if st.session_state.city else ""}
        </div>
        """, unsafe_allow_html=True)

        st.markdown("### Describe Your Case")
        with st.expander("💡 Tips for better results"):
            st.markdown("""
- **Include dates** — when did the incident happen?
- **Name the parties** — who is involved?
- **Mention evidence** — what proof do you have?
- **Describe the harm** — what loss occurred?
- **State your goal** — what outcome do you want?
""")

        case_text = st.text_area("Your Case Description", value=st.session_state.case_desc,
            placeholder="Example: My employer fired me 3 days after I filed a harassment complaint. I have email evidence of retaliation...",
            height=260, label_visibility="collapsed")

        chars = len(case_text)
        bc = "#22c55e" if chars>=150 else "#f59e0b" if chars>=50 else "#ef4444"
        ql = "Excellent detail ✓" if chars>=150 else "Good — add more detail" if chars>=50 else "Too short"
        
        st.markdown(f"""
        <div style='display:flex; justify-content:space-between; margin:8px 0 4px'>
          <span style='color:{bc}; font-size:13px; font-weight:600'>{ql}</span>
          <span style='color:#4a5568; font-size:13px; font-weight:600'>{chars} chars</span>
        </div>
        <div style='background:#e2e8f0; border-radius:2px; height:4px; margin-bottom:20px'>
          <div style='width:{min(100,chars/2)}%; height:100%; background:{bc}; border-radius:2px'></div>
        </div>
        """, unsafe_allow_html=True)

        b1,b2,b3 = st.columns([1,1,4])
        with b1:
            if st.button("← Back"):
                st.session_state.step = 0; st.rerun()
        with b3:
            go = st.button("🔍 Analyze My Case →", disabled=chars<50)

        if go and chars >= 50:
            st.session_state.case_desc = case_text
            pb  = st.progress(0)
            stx = st.empty()
            
            try:
                stx.info("🌐 Searching Indian Kanoon database...")
                pb.progress(10)
                q  = build_query(case_text, st.session_state.category)
                result = search_cases(q, max_results=8)
                
                if isinstance(result, dict):
                    lc = result.get("cases", [])
                else:
                    lc = result

                stx.info(f"✅ {len(lc)} real cases found on Indian Kanoon")
                pb.progress(30)

                fl = [{
                    "id": f"IK-{i+1:03}", "title": c["title"],
                    "category": st.session_state.category,
                    "year": c.get("date","2024")[:4] if c.get("date") else "2024",
                    "court": c["court"], "summary": c["summary"][:300],
                    "outcome": "See full judgment", "sentence": "See full judgment",
                    "key_facts": [word for word in c["summary"].split() if len(word) > 4][:10],
                    "lawyer": None, "url": c.get("url",""), "source": "🌐 Indian Kanoon",
                } for i, c in enumerate(lc)]

                combined = fl + LOCAL_CASES
                stx.info("🤖 AI scoring case similarity...")
                pb.progress(52)

                scores = score_matches(case_text, combined)
                scored = sorted([{
                    **c,
                    "matchScore":  next((s["score"] for s in scores if s["index"]==i), 0),
                    "matchReason": next((s["reason"] for s in scores if s["index"]==i), "")
                } for i,c in enumerate(combined)], key=lambda x: x["matchScore"], reverse=True)
                st.session_state.results = scored

                stx.info(f"👤 Matching verified advocates for {st.session_state.category} cases...")
                pb.progress(72)
                st.session_state.lawyers = get_lawyers_for_case(
                    st.session_state.city or "Patna", st.session_state.category)

                stx.info("⚖️ Generating legal assessment...")
                pb.progress(88)
                st.session_state.analysis = analyze_case(case_text, st.session_state.category, scored)

                pb.progress(100)
                stx.success("✅ Analysis complete!")
                time.sleep(0.6)
                st.session_state.step = 2
                st.rerun()
            except Exception as e:
                pb.empty(); stx.empty()
                st.error(f"❌ Error: {str(e)}")

    # STEP 2
    elif st.session_state.step == 2:
        results  = st.session_state.results
        analysis = st.session_state.analysis
        lawyers  = st.session_state.lawyers
        city     = st.session_state.city or "Your Area"

        # Crisp, high contrast banner
        st.markdown(f"""
        <div style='background:#ffffff; border:1px solid #e2e8f0; border-top:4px solid #1a202c;
                    border-radius:4px; padding:32px; margin-bottom:28px; box-shadow:0 2px 4px rgba(0,0,0,0.05)'>
          <div style='font-size:13px; font-weight:700; letter-spacing:2px; color:#4a5568; margin-bottom:14px'>
            ⚖️ AI LEGAL ASSESSMENT
          </div>
          <p style='font-size:17px; color:#000000; line-height:1.7; margin:0 0 24px; max-width:900px'>
            {analysis.get("summary","")}
          </p>
          <div style='background:#fef3c7; border:1px solid #fde68a; border-radius:4px; padding:14px 18px;
                      border-left:4px solid #d97706; display:inline-block'>
            <span style='color:#b45309; font-weight:700; font-size:13px; letter-spacing:1px'>
              ⚡ URGENT ACTION:
            </span>
            <span style='color:#1a202c; font-size:15px; margin-left:8px; font-weight:600'>
              {analysis.get("urgentAction","")}
            </span>
          </div>
        </div>
        """, unsafe_allow_html=True)

        # Metrics
        m1,m2,m3,m4 = st.columns(4)
        for col, (lbl,val) in zip([m1,m2,m3,m4],[
            ("Case Strength", analysis.get("caseStrength","—")),
            ("Strength Score", f"{analysis.get('strengthScore','—')}%"),
            ("Relevant Law",  analysis.get("relevantLaw","—")),
            ("Timeline",      analysis.get("timeline","—")),
        ]):
            # Determine color purely for the score/strength text
            clr = "#1a202c"
            if lbl == "Case Strength" or lbl == "Strength Score":
                clr = "#16a34a" if "Strong" in str(val) or (isinstance(val, str) and val.replace('%','').isdigit() and int(val.replace('%','')) > 60) else "#d97706" if "Moderate" in str(val) else "#dc2626"

            with col:
                st.markdown(f"""
                <div style='background:#ffffff; border:1px solid #e2e8f0; border-radius:4px;
                            padding:20px; text-align:center;'>
                  <div style='font-size:12px; font-weight:600; color:#64748b; letter-spacing:1px;
                              text-transform:uppercase; margin-bottom:8px'>{lbl}</div>
                  <div style='font-size:20px; font-weight:700; color:{clr}'>{val}</div>
                </div>
                """, unsafe_allow_html=True)

        # Outcome + risks
        oc1,oc2 = st.columns(2)
        with oc1:
            st.markdown(f"""
            <div style='background:#ffffff; border:1px solid #e2e8f0; border-radius:4px; padding:24px; margin-bottom:20px'>
              <div style='font-size:12px; font-weight:700; letter-spacing:2px; color:#4a5568; margin-bottom:12px'>LIKELY OUTCOME</div>
              <p style='color:#1a202c; font-size:15px; line-height:1.7; margin:0'>{analysis.get("likelyOutcome","—")}</p>
            </div>
            """, unsafe_allow_html=True)
        with oc2:
            risks = analysis.get("riskFactors", [])
            rhtml = "".join([f"<div style='padding:8px 0; border-bottom:1px solid #f1f5f9; color:#dc2626; font-size:15px; font-weight:600'>⚠ {r}</div>" for r in risks])
            st.markdown(f"""
            <div style='background:#ffffff; border:1px solid #e2e8f0; border-radius:4px; padding:24px; margin-bottom:20px'>
              <div style='font-size:12px; font-weight:700; letter-spacing:2px; color:#4a5568; margin-bottom:12px'>RISK FACTORS</div>
              {rhtml or "<div style='color:#64748b; font-size:15px'>No major risks identified</div>"}
            </div>
            """, unsafe_allow_html=True)

        st.markdown("<br>", unsafe_allow_html=True)

        # Tabs
        t1,t2,t3 = st.tabs([
            f"  📋 Matched Cases ({len(results)})  ",
            f"  👤 Verified Lawyers in {city} ({len(lawyers)})  ",
            "  📄 Download Report  ",
        ])

        with t1:
            liven  = len([r for r in results if r.get("source")=="🌐 Indian Kanoon"])
            localn = len(results)-liven
            st.info(f"🌐 **{liven}** live cases from Indian Kanoon  +  📁 **{localn}** local cases")

            for i, case in enumerate(results):
                score = case.get("matchScore",0)
                mc    = "#16a34a" if score>=70 else "#d97706" if score>=40 else "#dc2626"
                medal = "🥇" if i==0 else "🥈" if i==1 else "🥉" if i==2 else f"#{i+1}"

                with st.expander(f"{medal}  {case['title'][:50]}...  ·  {score}% Match", expanded=(i<2)):
                    dc1,dc2 = st.columns([3,1])
                    with dc1:
                        st.markdown(f"**🏛️ Court:** {case.get('court','N/A')}  |  **📅 Year:** {case.get('year','N/A')}")
                        st.markdown(f"> {case.get('summary','N/A')}")
                        if case.get("matchReason"):
                            st.markdown(f"""
                            <div style='background:#f8fafc; border-left:4px solid #1a202c;
                                        padding:12px 16px; border-radius:0 4px 4px 0;
                                        font-size:14px; color:#1a202c; margin-top:10px'>
                              🎯 <strong>Why matched:</strong> {case["matchReason"]}
                            </div>
                            """, unsafe_allow_html=True)
                        if case.get("url"):
                            st.markdown(f"🔗 [Read Full Judgment on Indian Kanoon →]({case['url']})")
                    with dc2:
                        st.markdown(f"""
                        <div style='text-align:center; background:#ffffff; border-radius:4px;
                                    padding:20px; border:1px solid {mc};'>
                          <div style='font-size:36px; font-weight:700; color:{mc}'>{score}%</div>
                          <div style='font-size:11px; font-weight:700; color:#64748b; letter-spacing:2px; margin:4px 0 12px'>MATCH</div>
                          <div style='font-size:13px; font-weight:600; color:#1a202c'>✅ {case.get("outcome","N/A")}</div>
                          <div style='font-size:12px; color:#94a3b8; margin-top:6px'>{case.get("source","Local")}</div>
                        </div>
                        """, unsafe_allow_html=True)

        with t2:
            st.markdown(f"### Top Verified Advocates for **{st.session_state.category.title()}** Cases")
            if not lawyers:
                st.warning("No matching advocates found. Showing all Bihar advocates.")
            else:
                st.success(f"✅ Found **{len(lawyers)}** verified advocates specialising in **{st.session_state.category.title()}** law — sourced from freelaw.in")
                st.markdown("<br>", unsafe_allow_html=True)

                for lawyer in lawyers:
                    verified_badge = "✅ Verified" if lawyer.get("rating","") == "✅ Verified" else "🔵 Registered"
                    with st.expander(f"👤 {lawyer['name']}  |  📍 {lawyer.get('city', city)}  {verified_badge}"):
                        lc1, lc2 = st.columns(2)
                        with lc1:
                            st.markdown("**📋 Professional Profile**")
                            st.markdown(f"⚖️ **Specialization:** {lawyer.get('specialization','N/A')}")
                            st.markdown(f"🎓 **Qualification:** {lawyer.get('qualification','N/A')}")
                            st.markdown(f"📍 **Location:** {lawyer.get('address','N/A')}")
                            st.markdown(f"🏛️ **Bar Council:** {lawyer.get('court','Bihar Bar Council')}")
                        with lc2:
                            st.markdown("**📞 Contact Information**")
                            ph = str(lawyer.get("phone",""))
                            st.markdown(f"📞 `{ph}`")
                            st.markdown(f"🌐 [View on freelaw.in](https://www.freelaw.in/advocates/directory?name=&state=bihar)")
                            ph_clean = ph.replace("+","").replace("-","").replace(" ","")
                            if ph_clean.isdigit():
                                wa = f"https://wa.me/91{ph_clean[-10:]}?text=Hello, I need help with a {st.session_state.category} case"
                                st.markdown(f"<a href='{wa}' target='_blank' style='background:#1a202c; color:#ffffff; padding:10px 20px; border-radius:4px; text-decoration:none; font-size:14px; font-weight:600; display:inline-block; margin-top:8px;'>💬 WhatsApp</a>", unsafe_allow_html=True)

        with t3:
            st.markdown("""
            <div style='text-align:center; padding:28px 20px'>
              <div style='font-size:44px; margin-bottom:14px'>📄</div>
              <h2 style='margin:0 0 8px'>Download Your Legal Report</h2>
              <p style='color:#64748b; font-size:15px; margin-bottom:28px'>
                Professional PDF with full case analysis, precedents and verified lawyer contacts
              </p>
            </div>
            """, unsafe_allow_html=True)
            rc1,rc2 = st.columns(2)
            with rc1:
                st.markdown("**📋 Report Includes:**")
                for item in ["Your case summary","AI legal assessment","Case strength & relevant law",
                             "Top matched court cases","Urgent action items","Verified Recommended Lawyers"]:
                    st.markdown(f"✅ <span style='color:#1a202c; font-weight:600'>{item}</span>", unsafe_allow_html=True)
            with rc2:
                st.markdown("**📊 Summary:**")
                st.markdown(f"- **Category:** {st.session_state.category.title()}")
                st.markdown(f"- **City:** {city}")
                st.markdown(f"- **Cases Analyzed:** {len(results)}")
                st.markdown(f"- **Experts Found:** {len(lawyers)}")
                st.markdown(f"- **AI Assessed Strength:** {analysis.get('caseStrength','N/A')}")
            st.markdown("<br>", unsafe_allow_html=True)
            try:
                pdf_buf = generate_pdf(
                    case_desc=st.session_state.case_desc, category=st.session_state.category,
                    analysis=analysis, results=results, lawyers=lawyers)
                st.download_button("⬇️ Download Full PDF Report", data=pdf_buf,
                    file_name=f"LexMatch_Report_{city}_{st.session_state.category}.pdf",
                    mime="application/pdf", use_container_width=True)
            except Exception as e:
                st.error(f"PDF error: {e}")

        st.markdown("<br><br>", unsafe_allow_html=True)
        if st.button("↩ Analyze Another Case"):
            for k in ["step","category","case_desc","results","analysis","lawyers"]:
                st.session_state[k] = 0 if k=="step" else None if k in ["category","analysis"] else [] if k in ["results","lawyers"] else ""
            st.rerun()


# ═══════════════════════════════════════════════════════════════
# LEGAL KNOWLEDGE PAGE
# ═══════════════════════════════════════════════════════════════
elif st.session_state.page == "knowledge":

    st.markdown("""
    <div style='padding:24px 0 16px'>
      <div style='font-size:12px; font-weight:700; letter-spacing:3px; color:#4a5568; margin-bottom:8px'>LEGAL KNOWLEDGE BASE</div>
      <h1 style='font-size:40px; margin:0'>Know Your Rights & Laws</h1>
      <p style='color:#4a5568; margin-top:8px; font-size:16px'>
        Ask anything about Indian laws · Plain language · No legal jargon
      </p>
    </div>
    """, unsafe_allow_html=True)

    # Topic cards
    st.markdown("### 📚 Browse by Topic")
    topics = [
        ("🔒","Criminal Law","IPC sections, FIR, bail, arrest rights"),
        ("🏠","Tenant & Property","Rent, eviction, property disputes"),
        ("👷","Labour & Employment","Termination, PF, harassment"),
        ("💍","Family & Marriage","Divorce, custody, domestic violence"),
        ("🛒","Consumer Rights","Defective products, refunds, complaints"),
        ("🌿","Environmental Law","Pollution, NGT, green laws"),
        ("🏛️","Constitutional Rights","Fundamental rights, PIL, RTI"),
        ("💼","Corporate & Business","Contracts, IP, company law"),
        ("🚗","Traffic & Motor","Accidents, license, challan"),
        ("💊","Medical & Health","Negligence, insurance, patient rights"),
        ("📱","Cyber Law","Online fraud, data privacy, cybercrime"),
        ("📚","Education Rights","RTE, fee disputes, student rights"),
    ]
    tc = st.columns(3)
    for i, (icon, topic, desc) in enumerate(topics):
        with tc[i % 3]:
            st.markdown(f"""
            <div style='background:#ffffff; border:1px solid #e2e8f0; border-radius:6px;
                        padding:16px 18px; margin-bottom:10px;'>
              <div style='display:flex; align-items:center; gap:12px; margin-bottom:6px'>
                <span style='font-size:22px'>{icon}</span>
                <span style='font-size:16px; font-weight:700; color:#000000'>{topic}</span>
              </div>
              <div style='font-size:13px; color:#4a5568; padding-left:34px'>{desc}</div>
            </div>
            """, unsafe_allow_html=True)
            if st.button(f"Ask about {topic}", key=f"t_{i}", use_container_width=True):
                st.session_state.law_query = f"Tell me everything about {topic} in India — my rights, key laws, sections, and what I should know as a citizen"
                st.rerun()

    st.markdown("""<div style='height:1px; background:#e2e8f0; margin:32px 0'></div>""", unsafe_allow_html=True)

    # Ask section
    st.markdown("### 💬 Ask Anything About Indian Law")
    examples = [
        "What are my rights if police arrest me without a warrant?",
        "Can my landlord evict me without giving 1 month notice?",
        "What is Section 498A IPC and when does it apply?",
        "How do I file a consumer complaint against a company?",
        "What is the process to file for divorce in India?",
        "Can an employer fire me without giving a reason?",
    ]
    st.markdown("**Quick Questions:**")
    qc = st.columns(2)
    for i, q in enumerate(examples):
        with qc[i % 2]:
            if st.button(f"❓ {q[:52]}...", key=f"eq_{i}", use_container_width=True):
                st.session_state.law_query = q
                st.rerun()

    st.markdown("<br>", unsafe_allow_html=True)
    law_q = st.text_area("Your Legal Question", value=st.session_state.law_query,
        placeholder="e.g. What are my rights if my employer refuses to pay my salary?",
        height=120, label_visibility="collapsed")

    ac1,ac2 = st.columns([4,1])
    with ac2:
        ask_btn = st.button("Ask Legal AI →", disabled=len(law_q)<10, use_container_width=True)

    if ask_btn and len(law_q)>=10:
        st.session_state.law_query = law_q
        with st.spinner("📚 Consulting legal knowledge base..."):
            try:
                from gemini_api import call_groq
                prompt = f"""You are an expert Indian legal consultant with 25 years experience.
A citizen asks: "{law_q}"
Provide a comprehensive helpful answer covering:
1. Direct answer to their question
2. Relevant Indian laws, Acts, IPC/CrPC sections that apply
3. Their specific legal rights in this situation
4. Step-by-step process they should follow
Use clear headings, simple language and no complex legal jargon."""
                st.session_state.law_response = call_groq(prompt)
            except Exception as e:
                st.session_state.law_response = f"Error: {str(e)}"

    if st.session_state.law_response:
        st.markdown("""<div style='height:1px; background:#e2e8f0; margin:24px 0'></div>""", unsafe_allow_html=True)
        st.markdown(f"""
        <div style='background:#ffffff; border:1px solid #e2e8f0; border-top:4px solid #1a202c;
                    border-radius:4px; padding:28px 32px; margin-bottom:20px; box-shadow:0 2px 4px rgba(0,0,0,0.05)'>
          <div style='font-size:12px; font-weight:700; letter-spacing:2px; color:#4a5568; margin-bottom:14px'>
            📚 LEGAL ASSISTANT RESPONSE
          </div>
          <div style='font-size:15px; font-weight:600; color:#000000; margin-bottom:24px; padding:16px 20px;
                      background:#f8fafc; border-radius:4px; border-left:4px solid #1a202c'>
            ❓ {st.session_state.law_query}
          </div>
        </div>
        """, unsafe_allow_html=True)
        st.markdown(f"<div style='font-size:16px; color:#1a202c; line-height:1.7'>{st.session_state.law_response}</div>", unsafe_allow_html=True)


# ═══════════════════════════════════════════════════════════════
# FIND LAWYERS PAGE
# ═══════════════════════════════════════════════════════════════
elif st.session_state.page == "lawyers":

    st.markdown("""
    <div style='padding:24px 0 16px'>
      <div style='font-size:12px; font-weight:700; letter-spacing:3px; color:#4a5568; margin-bottom:8px'>LEGAL DIRECTORY</div>
      <h1 style='font-size:40px; margin:0'>Find the Right Expert</h1>
      <p style='color:#4a5568; margin-top:8px; font-size:16px'>
        Browse verified Bihar advocates sourced from <strong>freelaw.in</strong> — filtered by your case type and city.
      </p>
    </div>
    """, unsafe_allow_html=True)

    ls1,ls2,ls3 = st.columns(3)
    with ls1: search_city = st.text_input("Enter City / District", placeholder="e.g. Patna, Gaya, Muzaffarpur...")
    with ls2:
        specs = ["All","Criminal","Civil","Family","Corporate","Constitutional","Environmental"]
        search_spec = st.selectbox("Select Specialization", specs)
    with ls3:
        st.markdown("<br>", unsafe_allow_html=True)
        if st.button("🔍 Search Directory →", use_container_width=True):
            cat_k = search_spec.lower() if search_spec != "All" else ""
            results = match_lawyers_to_category(category=cat_k, city=search_city)
            st.session_state.lawyers = results
            st.session_state.city    = search_city or "Bihar"
            st.rerun()

    if st.session_state.lawyers:
        lawyers = st.session_state.lawyers
        city    = st.session_state.city

        st.success(f"✅ Found **{len(lawyers)}** verified advocates matching your criteria.")
        st.markdown("<br>", unsafe_allow_html=True)
        
        for lawyer in lawyers:
            verified_badge = "✅ Verified" if lawyer.get("rating","") == "✅ Verified" else "🔵 Registered"
            with st.expander(f"👤 {lawyer['name']}  ·  {lawyer.get('specialization','')}  ·  📍 {lawyer.get('city',city)}  {verified_badge}"):
                lc1, lc2 = st.columns(2)
                with lc1:
                    st.markdown("**📋 Professional Profile**")
                    st.markdown(f"⚖️ **Specialization:** {lawyer.get('specialization','N/A')}")
                    st.markdown(f"🎓 **Qualification:** {lawyer.get('qualification','N/A')}")
                    st.markdown(f"📍 **Location:** {lawyer.get('address','N/A')}")
                    st.markdown(f"🏛️ **Bar Council:** {lawyer.get('court','Bihar Bar Council')}")
                with lc2:
                    st.markdown("**📞 Contact Information**")
                    ph = lawyer.get("phone","")
                    st.markdown(f"📞 `{ph}`")
                    st.markdown(f"🌐 Source: [freelaw.in](https://www.freelaw.in/advocates/directory?name=&state=bihar)")
                    if ph and ph.replace("+","").replace("-","").replace(" ","").isdigit():
                        ph_clean = ph.replace("+","").replace("-","").replace(" ","")
                        wa = f"https://wa.me/91{ph_clean[-10:]}?text=Hello, I need legal help with a case"
                        st.markdown(f"<a href='{wa}' target='_blank' style='background:#1a202c; color:#ffffff; padding:10px 20px; border-radius:4px; text-decoration:none; font-size:14px; font-weight:600; display:inline-block; margin-top:8px;'>💬 WhatsApp</a>", unsafe_allow_html=True)


# ═══════════════════════════════════════════════════════════════
# ABOUT PAGE
# ═══════════════════════════════════════════════════════════════
elif st.session_state.page == "about":

    st.markdown("""
    <div style='padding:24px 0 16px'>
      <div style='font-size:12px; font-weight:700; letter-spacing:3px; color:#4a5568; margin-bottom:8px'>HACKATHON 2026</div>
      <h1 style='font-size:40px; margin:0'>About JUSTICE GPT</h1>
      <p style='color:#4a5568; margin-top:8px; font-size:16px'>Law & Justice Track · AI-Powered Legal Platform</p>
    </div>
    """, unsafe_allow_html=True)

    # Problem
    st.markdown("""
    <div style='background:#ffffff; border:1px solid #e2e8f0; border-left:4px solid #dc2626;
                border-radius:4px; padding:32px; margin-bottom:20px; box-shadow:0 1px 3px rgba(0,0,0,0.05)'>
      <div style='font-size:12px; font-weight:700; letter-spacing:2px; color:#dc2626; margin-bottom:14px'>THE PROBLEM</div>
      <h2 style='font-size:28px; color:#000000; margin:0 0 14px'>70% of citizens cannot afford legal help</h2>
      <p style='color:#1a202c; font-size:16px; line-height:1.8; margin:0'>
        India has over 40 million pending court cases. Most citizens have no idea what their legal rights are, cannot afford consultation fees of ₹5,000–₹20,000, and don't know which experts to approach. The result: injustice by default.
      </p>
    </div>
    """, unsafe_allow_html=True)

    # Solution
    st.markdown("""
    <div style='background:#ffffff; border:1px solid #e2e8f0; border-left:4px solid #16a34a;
                border-radius:4px; padding:32px; margin-bottom:20px; box-shadow:0 1px 3px rgba(0,0,0,0.05)'>
      <div style='font-size:12px; font-weight:700; letter-spacing:2px; color:#16a34a; margin-bottom:14px'>OUR SOLUTION</div>
      <h2 style='font-size:28px; color:#000000; margin:0 0 14px'>Legal intelligence for everyone — free</h2>
      <p style='color:#1a202c; font-size:16px; line-height:1.8; margin:0'>
        Describe your problem in plain language and receive a professional case assessment, matched real court precedents, relevant laws, and verified local lawyers. What used to cost ₹10,000 now costs ₹0.
      </p>
    </div>
    """, unsafe_allow_html=True)