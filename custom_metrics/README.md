# Avaliação de Desempenho na Tarefa-Alvo com Métrica Customizada

Fizemos uma métrica customizada utilizando o `deepeval`. Para que possa utilizá-lo, é preciso baixar o `database` do Spider dataset para conseguir realizar as consultas SQL. Você pode encontrar o zip do Spider dataset facilmente no site, ou simplesmente pegar o zip que deixamos no nosso drive:

https://drive.google.com/drive/folders/1CADgJH4JmLiwoa6Tb053JXF71F1S7lkG?usp=sharing

Os .jsonl que geramos nos treinos possui os campos:
- db_id: O diretório das tabelas correspondentes à consulta
- response_query: Resposta dada pelo modelo
- original_query: Resposta original _ground truth_ da base
- question: Pergunta em linguagem natural

Exemplo:

```json
{
    "db_id": "concert_singer", 
    "response_query": "SELECT count(*) FROM singers;", 
    "original_query": "SELECT count(*) FROM singer", 
    "question": "How many singers do we have?"
}
```

Para executar o teste, deve-se obter o database do Spider e rodar o seguinte comando:

`python3 main.py <path do arquivo .jsonl> <path do database>`

Exemplo:

`python3 main.py respostas_fewshot.jsonl database`

Os resultados que obtemos foram:
- Modelo base com 3-shot: Score 20.0 de 200 queries
- Modelo fine tunado 1 (learning rate 2e-4): Score 28.0 de 200 queries