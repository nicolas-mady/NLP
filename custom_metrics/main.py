from ExecutionAccuracy import ExecutionAccuracy
from deepeval.test_case import LLMTestCase 
import json
import sys

def load_jsonl(file_path: str) -> list[dict]:
    """
    Carrega todos os objetos JSON de um arquivo .jsonl.

    Args:
        file_path (str): O caminho para o arquivo .jsonl.

    Returns:
        list[dict]: Uma lista de dicionários Python, onde cada dicionário
                    representa um objeto JSON do arquivo.
    """
    data = []
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            for line in f:
                # Remove espaços em branco ou quebras de linha extras
                stripped_line = line.strip()
                if stripped_line: # Garante que a linha não está vazia
                    try:
                        json_object = json.loads(stripped_line)
                        data.append(json_object)
                    except json.JSONDecodeError as e:
                        print(f"Erro ao decodificar JSON na linha: '{stripped_line}' - Erro: {e}")
                        # Opcional: Você pode optar por ignorar a linha ou levantar uma exceção
    except FileNotFoundError:
        print(f"Erro: O arquivo '{file_path}' não foi encontrado.")
    except Exception as e:
        print(f"Ocorreu um erro inesperado ao ler o arquivo: {e}")
    return data


# Example Usage (for testing purposes)
if __name__ == "__main__":

    db_path = "./spider_data/database" 

    if len(sys.argv) == 2:
        data = load_jsonl(sys.argv[1])
    else:
        print("Faltou passar o argumento do path do jsonl")
        sys.exit(1)

    execution_accuracy_metric = ExecutionAccuracy(base_db_dir = db_path)

    score=0
    cont=0
    for i in data:
        test_case = LLMTestCase(
            input= i['db_id'],
            actual_output= i['response_query'],
            expected_output= i['original_query'],
            retrieval_context=[], 
            context=[], 
        )
        score += execution_accuracy_metric.measure(test_case)
        cont+=1

    print(f"Score = {score}, Quantidade de queries: {cont}")