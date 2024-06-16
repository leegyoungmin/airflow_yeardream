from airflow.decorators import dag
import pendulum

from airflow.operators.bash import BashOperator

@dag(
    dag_id='dags_bash_operator_decorator',
    start_date=pendulum.datetime(2024, 5, 1, tz="Asia/Seoul"),
    schedule="0 9 * * 1,5",
    tags=['homework'],
    catchup=False
)
def generate_bash_dag():
    task_1 = BashOperator(
        task_id='bash_task_1',
        bash_command='echo task_1'
    )

    task_2 = BashOperator(
        task_id='bash_task_2',
        bash_command='echo task_2'
    )

    task_3 = BashOperator(
        task_id='bash_task_3',
        bash_command='echo task_3'
    )

    task_1 >> task_2 >> task_3

dag = generate_bash_dag()