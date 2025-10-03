from airflow.sdk import DAG
from airflow.utils import timezone
from airflow.providers.standard.operators.python import PythonOperator
from airflow.providers.standard.operators.bash import BashOperator
from airflow.providers.standard.operators.empty import EmptyOperator

def _hello():
    print("Hello")

with DAG(
    dag_id="day_1_16",
    start_date=timezone.datetime(2025,10,2),
    schedule="30 17 1,16 * *", 
):
    hello = PythonOperator(
        task_id = "hello",
        python_callable = _hello,
    )

    world = BashOperator(
        task_id="world",
        bash_command="echo 'world'",
    )

hello >> world
