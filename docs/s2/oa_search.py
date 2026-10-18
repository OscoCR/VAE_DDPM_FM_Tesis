"""Discovery search on OpenAlex (no key needed). Used for the narrative Background; metadata of cited works is re-checked on Semantic Scholar."""
import csv, json, sys, time, urllib.parse, urllib.request
def abstract(inv):
    if not inv: return ""
    pos = {}
    for w, ps in inv.items():
        for p in ps: pos[p] = w
    return " ".join(pos[i] for i in sorted(pos))
def search(q, n=12, since="2012-01-01"):
    p = {"search": q, "per-page": n, "filter": f"from_publication_date:{since},type:article|preprint|book-chapter|proceedings-article",
         "select": "id,doi,title,publication_year,primary_location,authorships,cited_by_count,type,abstract_inverted_index"}
    url = "https://api.openalex.org/works?" + urllib.parse.urlencode(p)
    for k in range(5):
        try:
            with urllib.request.urlopen(urllib.request.Request(url, headers={"User-Agent": "thesis-lit-search/1.0"}), timeout=60) as r:
                return json.load(r)["results"]
        except Exception as e:
            time.sleep(3 * (k + 1))
    return []
Q = [
 "UAV plant counting deep learning",
 "drone imagery crop counting object detection",
 "pineapple detection counting UAV",
 "You only look once real-time object detection",
 "learning to count objects in images density estimation",
 "deep learning in agriculture survey",
 "UAV imagery agriculture annotation cost limited labeled data",
 "synthetic images diffusion model data augmentation object detection agriculture",
 "generative data augmentation plant counting",
 "training-free few-shot object detection foundation model agriculture",
 "real-time object detection UAV onboard embedded",
 "domain shift crop field generalization deep learning UAV",
 "Faster R-CNN region proposal networks object detection",
 "plant counting survey remote sensing deep learning",
]
if __name__ == "__main__":
    with open("topic_search_openalex_2026-10-18.csv", "w", newline="", encoding="utf8") as f:
        w = csv.writer(f); w.writerow(["query","rank","title","year","venue","citations","doi","authors","abstract_500"])
        for q in Q:
            r = search(q)
            for i, x in enumerate(r, 1):
                loc = (x.get("primary_location") or {}).get("source") or {}
                au = "; ".join(a["author"]["display_name"] for a in (x.get("authorships") or [])[:4])
                w.writerow([q, i, x["title"], x["publication_year"], loc.get("display_name"), x["cited_by_count"], x.get("doi"), au, abstract(x.get("abstract_inverted_index"))[:500]])
            print(f"{q[:62]:62s} {len(r)}", flush=True)
            time.sleep(0.5)
