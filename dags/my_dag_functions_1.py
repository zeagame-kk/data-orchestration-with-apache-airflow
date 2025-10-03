import datetime
from airflow.sdk import DAG, task, dag

#แบบแรก
@dag(
    dag_id="my_dag_functions_1",
    start_date=datetime.datetime(2025, 10, 2),
    schedule=None,
)
def my_dag_functions_1():

    @task
    def minus_20(number):
        return number - 20

    @task
    def plus_100(number):
        return number+100

    minus_20(plus_100(10))

dag = my_dag_functions_1()

# #แบบที่สอง
# with DAG(
#     dag_id="my_dag_name",
#     start_date=datetime.datetime(2025, 10, 1),
#     schedule=None,
# ):

#     @task
#     def minus_20(number):
#         return number - 20

#     @task
#     def plus_100(number):
#         return number+100


#     minus_20(plus_100(10))
