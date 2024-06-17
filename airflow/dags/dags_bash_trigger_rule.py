from airflow import DAG
from airflow.decorators import task
from airflow.operators.bash import BashOperator
from airflow.exceptions import AirflowException

import pendulum

with DAG(
    dag_id='dags_bash_trigger_rule',
    start_date=pendulum.datetime(2024, 6, 1, tz="Asia/Seoul"),
    schedule=None,
    catchup=False,
    tags=["homework"]
) as dag:
    bash_t1 = BashOperator(
        task_id='bash_t1',
        bash_command='echo task_1',
    )

    bash_t2 = BashOperator(
        task_id='bash_t2',
        bash_command='echo task_2',
    )

    bash_t3 = BashOperator(
        task_id='bash_t3',
        bash_command='echo task_3',
    )

    bash_t4 = BashOperator(
        task_id='bash_t4',
        bash_command='echo task_4',
        trigger_rule='one_success'
    )

    [bash_t1, bash_t2, bash_t3] >> bash_t4