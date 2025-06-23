# Trabalho 4 de NLP: Análise Quantitativa do Trade-off entre Especialização e Generalização em LLMs via Fine-Tuning

Equipe:
- André Okimoto - 22352921
- Guilherme Louro - 22351621
- Nicolas Mady - 22352932

---

Este repositório possui:
- `scripts/`: Diretório com todos os notebooks jupyter utilizados para treinar e avaliar os modelos. Utilizamos o modelo "mistralai/Mistral-7B-Instruct-v0.2". Todos os notebooks foram rodados no ambiente do Google Colaboratory por falta de máquina própria, então tenha em mente que são notebooks pensados apenas para rodar naquele ambiente. Nele há os notebooks correspondentes ao modelo base e aos fine-tuned.
- `custom_metrics/`: Diretório que possui a métrica customizada do deepeval para avaliar as respostas dos modelos para a tarefa de Text-to-SQL. Importante mencionar que, por questões de eficiência e praticidade, nós geramos as consultas SQL dos modelos e salvamos num arquivo jsonl. Assim, evitaríamos ter que rodar cada consulta uma de cada vez, ainda mais no Google Colaboratory. Ele pode ser rodado na própria máquina.
- `requirements.txt`: Bibliotecas necessárias para rodar o custom_metrics. Não possui dependência com os notebooks jupyter, pois pensamos apenas na forma de rodar no Google Colab.

Alguns links importantes:
- Drive com os adaptadores treinados e o database do spider:
https://drive.google.com/drive/folders/1CADgJH4JmLiwoa6Tb053JXF71F1S7lkG?usp=sharing


- Link do modelo `mistralai/Mistral-7B-Instruct-v0.2` no Hugging Face:
https://huggingface.co/mistralai/Mistral-7B-Instruct-v0.2

