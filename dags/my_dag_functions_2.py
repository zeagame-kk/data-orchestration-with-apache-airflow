import datetime
from airflow.sdk import DAG, task, dag


#แบบที่สอง
with DAG(
    dag_id="my_dag_functions_2",
    start_date=datetime.datetime(2025, 10, 2),
    schedule=None,
):

    @task
    def minus_20(number):
        return number - 20

    @task
    def plus_100(number):
        return number+100


    minus_20(plus_100(10))
