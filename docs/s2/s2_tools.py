"""Small Semantic Scholar helper (Graph API v1). The API key is read from the S2_API_KEY environment
variable (header x-api-key) and is never printed or stored. Without a key the shared pool is used and 429s are retried."""
import csv, json, os, sys, time, urllib.parse, urllib.request, urllib.error

BASE = "https://api.semanticscholar.org/graph/v1"
FIELDS = "title,year,venue,publicationVenue,authors,externalIds,abstract,citationCount,publicationTypes"
KEY = os.environ.get("S2_API_KEY")
PAUSE = 1.1 if KEY else 4.0


def _req(url, data=None, tries=6):
    headers = {"User-Agent": "thesis-lit-search/1.0"}
    if KEY:
        headers["x-api-key"] = KEY
    if data is not None:
        headers["Content-Type"] = "application/json"
        data = json.dumps(data).encode()
    wait = 5
    for _ in range(tries):
        try:
            with urllib.request.urlopen(urllib.request.Request(url, data=data, headers=headers), timeout=60) as r:
                time.sleep(PAUSE)
                return json.load(r)
        except urllib.error.HTTPError as e:
            if e.code in (429, 500, 502, 503, 504):
                time.sleep(wait); wait = min(wait * 2, 60); continue
            raise
    raise RuntimeError("too many retries: " + url.split("?")[0])


def batch(ids):
    return _req(f"{BASE}/paper/batch?fields={FIELDS}", {"ids": ids})


def search(query, limit=20, year=None):
    p = {"query": query, "limit": limit, "fields": FIELDS}
    if year:
        p["year"] = year
    return _req(f"{BASE}/paper/search?" + urllib.parse.urlencode(p)).get("data", [])


def row(query, rank, p):
    ex = p.get("externalIds") or {}
    return [query, rank, p.get("paperId"), p.get("title"), p.get("year"), p.get("venue"), p.get("citationCount"),
            ex.get("DOI"), ex.get("ArXiv"), "; ".join(a["name"] for a in (p.get("authors") or [])[:4]),
            (p.get("abstract") or "").replace("\n", " ")[:600]]
HEAD = ["query", "rank", "paperId", "title", "year", "venue", "citations", "doi", "arxiv", "authors", "abstract_600"]
