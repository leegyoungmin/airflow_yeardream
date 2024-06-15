from airflow import DAG

from airflow.operators.bash import BashOperator

import pendulum

dags_bash_operator_standard = DAG(
    dag_id='dags_bash_operator_standard',
    start_date=pendulum.datetime(2024, 6, 1, tz="Asia/Seoul"),
    tags=['homework'],
    schedule='0 9 * * 1,5'
)

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