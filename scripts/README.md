# Notebooks jupyter

Nesse diretório há três outros diretórios, que possuem os notebooks jupyter referentes ao modelo base e os dois fine-tuned desse mesmo modelo. 

Cada um possui um notebook de geração de um arquivo .jsonl com as consultas SQL (para testar posteriormente) e um de avaliação no MMLU. Para os modelos fine tunados, há também um notebook de treino.

Note que estamos utilizando a base spider na biblioteca `datasets`. Conferimos a base do site e da biblioteca. O split de validation do `datasets` bate com o Spider dev split, por isso optamos por utilizar a biblioteca (mais praticidade, pois todos são notebooks para rodar no google colaboratory).
