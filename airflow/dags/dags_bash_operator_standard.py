from airflow import DAG

import datetime

dags_bash_operator_standard = DAG(
    dag_id='dags_bash_operator_standard',
    start_date=datetime.datetime(2024, 6, 1),
    tags=['homework']
)