from airflow import DAG
import datetime
import pendulum

from airflow.operators.bash import BashOperator

with DAG(
        dag_id="dags_bash_operator",
        schedule="0 0 * * *",
        start_date=pendulum.datetime(2024, 6, 13, tz="Asia/Seoul"),
        catchup=True
) as dag:
    bash_t1 = BashOperator(
        task_id="bash_t1",
        bash_command="echo whoami"
    )

    bash_t2 = BashOperator(
        task_id="bash_t2",
        bash_command="echo $HOSTNAME"
    )

    bash_t3 = BashOperator(
        task_id="bash_t3",
        bash_command="echo Gyoungmin"
    )

    bash_t1 >> bash_t2 >> bash_t3