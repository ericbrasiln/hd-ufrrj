import requests

HEADERS = {"Accept": "application/json", "User-Agent": "oasisbr-oficina/0.4"}

def busca(term, limit=10, offset=0):
    base = "https://oasisbr.ibict.br/vufind/api/v1/search"
    params = {"lookfor": term, "type": "AllFields", "limit": limit, "offset": offset}
    r = requests.get(base, params=params, headers=HEADERS, timeout=30)
    r.raise_for_status()
    return r.json().get("records", [])

resultados = busca("historia digital", limit=10)

for rec in resultados:
    titulo = rec.get("title") or rec.get("displayTitle") or rec.get("title_short")
    autores = rec.get("authors", {}).get("primary", {})
    ano = rec.get("publishDate") or rec.get("year") or rec.get("publishDateSort")
    urls = [u.get("url") for u in rec.get("urls", [])] if rec.get("urls") else []
    print("ID:", rec.get("id"))
    print("Título:", titulo)
    print("Autores:", ", ".join(autores.keys()) if autores else None)
    print("Ano:", ano)
    print("URLs:", urls)
    print("-" * 60)
