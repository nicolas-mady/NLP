from ExecutionAccuracy import ExecutionAccuracy
from deepeval.test_case import LLMTestCase 
import json
import sys

def load_jsonl(file_path: str) -> list[dict]:
    """Função auxiliar para pegar os arquivos .jsonl """
    data = []
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            for line in f:

                # Remove espaços em branco ou quebras de linha extras
                stripped_line = line.strip()
                if stripped_line: 
                    try:
                        json_object = json.loads(stripped_line)
                        data.append(json_object)
                    except json.JSONDecodeError as e:
                        print(f"Erro ao decodificar JSON na linha: '{stripped_line}' - Erro: {e}")

    except FileNotFoundError:
        print(f"Erro: O arquivo '{file_path}' não foi encontrado.")
    except Exception as e:
        print(f"Ocorreu um erro inesperado ao ler o arquivo: {e}")
    return data


if __name__ == "__main__":

    db_path = "./database"

    if len(sys.argv) == 3:
        data = load_jsonl(sys.argv[1])
        db_path = sys.argv[2]
    else:
        print("A linha de comando deve ser `python3 main.py [arquivo.jsonl] [path_database_sql]`")
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