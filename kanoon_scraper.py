"""
kanoon_scraper.py
Scrapes real court cases from Indian Kanoon (indiankanoon.org)
LexMatch AI — Hackathon 2026
"""

import requests
from bs4 import BeautifulSoup
import time

HEADERS = {
    "User-Agent": (
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
        "AppleWebKit/537.36 (KHTML, like Gecko) "
        "Chrome/120.0.0.0 Safari/537.36"
    ),
    "Accept-Language": "en-US,en;q=0.9",
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
}


def build_query(case_description: str, category: str) -> str:
    """
    Build a smart Indian Kanoon search query from user's case description.
    """
    category_keywords = {
        "criminal":       "IPC criminal case India",
        "civil":          "civil suit High Court India",
        "family":         "family court divorce custody India",
        "corporate":      "company law corporate dispute India",
        "constitutional": "PIL fundamental rights writ India",
        "environmental":  "NGT environment pollution India",
    }

    # Extract meaningful words from case description (skip common words)
    stop_words = {
        "the", "a", "an", "and", "or", "but", "in", "on", "at", "to",
        "for", "of", "with", "by", "from", "is", "was", "are", "were",
        "my", "me", "he", "she", "we", "i", "his", "her", "they", "it",
        "have", "has", "had", "been", "be", "do", "did", "does", "will",
        "that", "this", "which", "who", "what", "how", "when", "where",
    }
    words      = case_description.lower().split()
    key_words  = [w for w in words if w not in stop_words and len(w) > 4][:6]
    short_desc = " ".join(key_words)

    base = category_keywords.get(category, "India court case")
    return f"{short_desc} {base}".strip()


def search_cases(query: str, max_results: int = 8) -> list:
    """
    Search Indian Kanoon for cases matching the query.
    Returns list of case dicts with title, court, summary, url.
    """
    cases = []
    url   = f"https://indiankanoon.org/search/?formInput={query}&pagenum=0"

    try:
        resp = requests.get(url, headers=HEADERS, timeout=12)
        if resp.status_code != 200:
            return []

        soup    = BeautifulSoup(resp.text, "lxml")
        results = soup.find_all("div", class_="result")

        for result in results[:max_results]:
            try:
                # Title & link
                title_tag = result.find("div", class_="result_title")
                if not title_tag:
                    continue
                a_tag = title_tag.find("a")
                if not a_tag:
                    continue

                title = a_tag.text.strip()
                link  = "https://indiankanoon.org" + a_tag.get("href", "")

                # Court / source
                cite_tag = result.find("div", class_="docsource_main")
                court    = cite_tag.text.strip() if cite_tag else "Indian Court"

                # Date
                date_tag = result.find("div", class_="doc_date")
                date     = date_tag.text.strip() if date_tag else "N/A"

                # Snippet
                snippet_tags = result.find_all("p")
                snippet      = " ".join(p.text.strip() for p in snippet_tags[:2])[:300]

                cases.append({
                    "title":   title,
                    "court":   court,
                    "date":    date,
                    "summary": snippet or "See full judgment for details.",
                    "url":     link,
                    "source":  "🌐 Indian Kanoon",
                })

            except Exception:
                continue

        time.sleep(0.5)  # Be respectful to the server

    except requests.exceptions.Timeout:
        print("Indian Kanoon timeout — using local cases only")
    except requests.exceptions.ConnectionError:
        print("No internet connection — using local cases only")
    except Exception as e:
        print(f"Kanoon scrape error: {e}")

    return cases


def fetch_full_judgment(url: str) -> dict:
    """
    Fetch the full judgment text from a specific Indian Kanoon case URL.
    """
    try:
        resp = requests.get(url, headers=HEADERS, timeout=12)
        soup = BeautifulSoup(resp.text, "lxml")

        judgment_div = soup.find("div", id="judgments")
        full_text    = judgment_div.get_text(separator=" ")[:4000] if judgment_div else ""

        court_tag = soup.find("div", class_="docsource_main")
        court     = court_tag.text.strip() if court_tag else ""

        date_tag = soup.find("div", class_="doc_date")
        date     = date_tag.text.strip() if date_tag else ""

        title_tag = soup.find("h2", class_="doc_title")
        title     = title_tag.text.strip() if title_tag else url

        return {
            "title":     title,
            "court":     court,
            "date":      date,
            "full_text": full_text,
            "url":       url,
        }

    except Exception as e:
        print(f"Judgment fetch error: {e}")
        return {}
