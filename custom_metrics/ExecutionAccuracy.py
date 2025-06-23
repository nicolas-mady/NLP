import sqlite3
from typing import List, Any
from deepeval.metrics import BaseMetric
from deepeval.test_case import LLMTestCase

class ExecutionAccuracy(BaseMetric):
    def __init__(self, name: str = "Execution Accuracy", base_db_dir = "./spider_dataset/database"):
        super().__init__()

        self.name = name
        # local do diretório do SQL
        self.base_db_dir = base_db_dir

    def _execute_sql(self, cursor: sqlite3.Cursor, sql_query: str) -> List[Any]:
        try:
            cursor.execute(sql_query)
            # Ordena para fazer a  comparação insensível à ordem do trabalho
            return sorted(cursor.fetchall())  
        except sqlite3.Error as e:
            return []  

    def measure(self, test_case: LLMTestCase) -> float:

        # Constrói o caminho para o banco de dados correto usando db_id
        db_path = f"{self.base_db_dir}/{test_case.input}/{test_case.input}.sqlite"
        conn = None
        try:
            conn = sqlite3.connect(db_path)
            cursor = conn.cursor()
            
            actual_results = self._execute_sql(cursor, test_case.actual_output)
            expected_results = self._execute_sql(cursor, test_case.expected_output)

            if actual_results == expected_results:
                self.success = True
                return 1.0
            else:
                self.success = False
                return 0.0

        except Exception as e:
            self.success = False
            return 0.0
        finally:
            if conn:
                conn.close()