# RPCW2026-Normal

## Exercicio 1

### Ontologia

Criei as classes Animal com as subclasses Ave e Mamifero com as respetivas subclasses Corvo e Raposa, criei ainda a classe Caracteristica para defenir as caracteristicas descritas, as classes Localização, Objeto, Personagem e Sentimento. Os verbos e interações foram feitos como Object Properties, como por exemplo, possui, estaEm, sente, temCaracteristica, enganou, elogiou. Os valores literais ficaram definidos nas Data Properties como o nome a descrição e a corPlumagem.

### Queries

Criei as queries para a ontologia


## Exercicio 2

### Ontologia Base

Para a ontologia defini as classes Autor para definir quem são os autores dos jogos, a classe Editora, a classe Jogo, a classe Mecanica e a classe Premio. As Object Properties(OP) criadas foram a AtribuidoA para relacioanr um Premio a um Jogo, a OP criou oara relacionar o Autor ao Jogo, a OP publicou para relacionar Editora a Jogo e a OP usadaEm para relacionar a Mecanica ao Jogo. Nas DataProperties(DP) criei o ano para o ano do Premio, a categoria, descricao, maxJogadores e minJogadores e tempoJogo para o Jogo e criei a DP nome para os nomes.

### Ontologia Povoada

Depois de ter a ontologia base criada, com base nos ficheiros json fornecidos, povoei a ontologia com um script em python que carrega a estrutura base do boardgames_base.ttl, defino o slug() para ter URIs seguros. Depois o script percorre os 5 json's e cria triplos. Por fim serializa tudo no boardgames_ind.ttl.

### Sparql

Criei queries simples para a ontologia povoada, de seguida criei queries de cálculo de distribuições e depois de inferência de novo conhecimento