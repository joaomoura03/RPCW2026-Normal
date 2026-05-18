import json
import re
from rdflib import Graph, Namespace, URIRef, RDF, Literal, XSD
from rdflib.namespace import OWL

# --------------------------------------------------------------------
# 1. Configuracao
# --------------------------------------------------------------------
N = Namespace("http://www.di.uminho.pt/rpcw2026/pg60273#")

g = Graph()
g.parse("boardgames_base.ttl", format="turtle")   # carrega a estrutura base
g.bind("", N)

def slug(prefixo, texto):
    """Cria um nome local valido e previsivel: catan -> jogo_catan,
       7-wonders -> jogo_7_wonders, ticket-to-ride -> jogo_ticket_to_ride"""
    s = re.sub(r'[^0-9a-zA-Z]+', '_', texto).strip('_').lower()
    return URIRef(f"{N}{prefixo}_{s}")

def carregar(ficheiro):
    with open(ficheiro, encoding="utf-8") as f:
        return json.load(f)

# --------------------------------------------------------------------
# 2. Jogos  (jogos.json)
# --------------------------------------------------------------------
for j in carregar("jogos.json"):
    jURI = slug("jogo", j["id"])
    g.add((jURI, RDF.type, OWL.NamedIndividual))
    g.add((jURI, RDF.type, N.Jogo))
    g.add((jURI, N.id, Literal(j["id"])))
    g.add((jURI, N.nome, Literal(j["name"])))
    g.add((jURI, N.categoria, Literal(j["category"])))
    g.add((jURI, N.minJogadores, Literal(int(j["minPlayers"]), datatype=XSD.integer)))
    g.add((jURI, N.maxJogadores, Literal(int(j["maxPlayers"]), datatype=XSD.integer)))
    g.add((jURI, N.tempoJogo, Literal(int(j["playingTimeMinutes"]), datatype=XSD.integer)))
    g.add((jURI, N.descricao, Literal(j["descriptionEN"])))

# --------------------------------------------------------------------
# 3. Autores  (autores.json)  ->  Autor criou Jogo
# --------------------------------------------------------------------
for a in carregar("autores.json"):
    aURI = slug("autor", a["id"])
    g.add((aURI, RDF.type, OWL.NamedIndividual))
    g.add((aURI, RDF.type, N.Autor))
    g.add((aURI, N.id, Literal(a["id"])))
    g.add((aURI, N.nome, Literal(a["name"])))
    for jogo in a["designedGames"]:
        g.add((aURI, N.criou, slug("jogo", jogo)))

# --------------------------------------------------------------------
# 4. Editoras  (editoras.json)  ->  Editora publicou Jogo
# --------------------------------------------------------------------
for e in carregar("editoras.json"):
    eURI = slug("editora", e["id"])
    g.add((eURI, RDF.type, OWL.NamedIndividual))
    g.add((eURI, RDF.type, N.Editora))
    g.add((eURI, N.id, Literal(e["id"])))
    g.add((eURI, N.nome, Literal(e["name"])))
    g.add((eURI, N.pais, Literal(e["country"])))
    for jogo in e["publishedGames"]:
        g.add((eURI, N.publicou, slug("jogo", jogo)))

# --------------------------------------------------------------------
# 5. Mecanicas  (mecanicas.json)  ->  Mecanica usadaEm Jogo
# --------------------------------------------------------------------
for m in carregar("mecanicas.json"):
    mURI = slug("mecanica", m["id"])
    g.add((mURI, RDF.type, OWL.NamedIndividual))
    g.add((mURI, RDF.type, N.Mecanica))
    g.add((mURI, N.id, Literal(m["id"])))
    g.add((mURI, N.nome, Literal(m["name"])))
    for jogo in m["usedInGames"]:
        g.add((mURI, N.usadaEm, slug("jogo", jogo)))

# --------------------------------------------------------------------
# 6. Premios  (premios.json)  ->  Premio atribuidoA Jogo
# --------------------------------------------------------------------
for p in carregar("premios.json"):
    pURI = slug("premio", p["id"])
    g.add((pURI, RDF.type, OWL.NamedIndividual))
    g.add((pURI, RDF.type, N.Premio))
    g.add((pURI, N.id, Literal(p["id"])))
    g.add((pURI, N.nome, Literal(p["name"])))
    g.add((pURI, N.ano, Literal(int(p["year"]), datatype=XSD.integer)))
    g.add((pURI, N.atribuidoA, slug("jogo", p["wonByGame"])))

# --------------------------------------------------------------------
# 7. Serializar
# --------------------------------------------------------------------
g.serialize(destination="boardgames_ind.ttl", format="turtle")
print(f"OK - boardgames_ind.ttl gerado com {len(g)} triplos.")