"""Repeat the arXiv search strings S1-S5 on Semantic Scholar (bulk search, boolean) and apply the same three keyword criteria.
Criteria are re-implemented from their written definition (c1.tex, 'Screening criteria'); the original arXiv script was not kept."""
import csv, json, re, urllib.parse, datetime, s2_tools as s2
L = '"latent diffusion"'; A = '(autoencoder | VAE | tokenizer)'
STR = {
 "S1": f'{L} + {A} + (augmentation | "data augmentation")',
 "S2": f'{L} + {A} + (adversarial | KL | regularization | "latent channels")',
 "S3": f'{L} + {A} + (aerial | agricultural | crop | plant | UAV | "remote sensing")',
 "S4": f'(masked | masking) + {L} + {A}',
 "S5": f'{L} + depth + (RGB | appearance) + (joint | jointly | "shared latent")',
}
FIELDS = "title,abstract,year,venue,externalIds,publicationDate"
C1 = re.compile(r"augment|\bmask(ed|ing)\b|adversarial|\bKL\b|kullback|regulari[sz]|latent (channel|dimension)|number of (latent )?channels|fine-?tun", re.I)
C2 = re.compile(r"\bFID\b|\bKID\b|fr[eé]chet|(generation|generated|generative|sample|image|synthesis|synthetic)[ -](quality|image|images|synthesis|data)|image generation|image synthesis|sample quality|synthesi[sz]", re.I)
C3_DATA = re.compile(r"(small|limited|scarce|scarcity|few|low|insufficient)[- ](scale )?(data|dataset|datasets|images|samples|training|annotations?|labels?)|few-shot|data[- ]efficien|data scarcity|homogeneous|low-data", re.I)
C3_DOM = re.compile(r"aerial|agricultur|\bcrops?\b|\bplants?\b|\bUAV|remote sensing|satellite|medical|\bMRI\b|\bCT\b|clinical|radiolog", re.I)
norm = lambda s: re.sub(r"[^a-z0-9]", "", (s or "").lower())

def fetch(q):
    out, token = [], None
    while True:
        p = {"query": q, "year": "2022-", "fields": FIELDS}
        if token: p["token"] = token
        r = s2._req(f"{s2.BASE}/paper/search/bulk?" + urllib.parse.urlencode(p))
        out += r.get("data", []); token = r.get("token")
        if not token or len(out) >= 3000: break
    return out

recs, per = {}, {}
for sid, q in STR.items():
    r = fetch(q); per[sid] = len(r)
    for p in r:
        d = recs.setdefault(p["paperId"], {"p": p, "from": []}); d["from"].append(sid)
    print(sid, len(r), flush=True)

arx = list(csv.DictReader(open("../screening_arxiv_2026-10-11.csv", encoding="utf8")))
arx_ids = {re.sub(r"v\d+$", "", r["arxiv_id"]) for r in arx}; arx_titles = {norm(r["titulo"]) for r in arx}

rows = []
for pid, d in recs.items():
    p = d["p"]; txt = (p.get("title") or "") + " " + (p.get("abstract") or "")
    ex = p.get("externalIds") or {}
    c1, c2 = bool(C1.search(txt)), bool(C2.search(txt)); c3d, c3m = bool(C3_DATA.search(txt)), bool(C3_DOM.search(txt))
    in_arx = (ex.get("ArXiv") in arx_ids) or (norm(p.get("title")) in arx_titles)
    rows.append([pid, p.get("year"), p.get("venue"), p.get("title"), ex.get("DOI"), ex.get("ArXiv"), ";".join(d["from"]), int(c1), int(c2), int(c3d), int(c3m), int(in_arx), int(bool(p.get("abstract"))), (p.get("abstract") or "").replace("\n", " ")[:900]])
head = ["paperId","year","venue","title","doi","arxiv","strings","C1","C2","C3_pocos_datos","C3_dominio","ya_en_arxiv","tiene_resumen","abstract_900"]
with open("screening_s2_2026-10-18.csv", "w", newline="", encoding="utf8") as f:
    w = csv.writer(f); w.writerow(head); w.writerows(sorted(rows, key=lambda r: (-r[7]*r[8], r[3] or "")))
n = len(rows); c12 = [r for r in rows if r[7] and r[8]]; c123 = [r for r in c12 if r[9] or r[10]]
summ = {"fecha": str(datetime.date(2026,10,18)), "endpoint": "paper/search/bulk", "year": "2022-", "strings": STR, "registros_por_cadena": per,
        "unicos": n, "ya_en_arxiv": sum(r[11] for r in rows), "nuevos_vs_arxiv": n - sum(r[11] for r in rows), "sin_resumen": sum(1-r[12] for r in rows),
        "C1": sum(r[7] for r in rows), "C1_y_C2": len(c12), "C1_C2_y_C3": len(c123), "C1_C2_y_C3_nuevos": sum(1 for r in c123 if not r[11])}
json.dump(summ, open("screening_s2_2026-10-18_summary.json", "w"), indent=1, ensure_ascii=False)
print(json.dumps({k: v for k, v in summ.items() if k != "strings"}, indent=1, ensure_ascii=False))
