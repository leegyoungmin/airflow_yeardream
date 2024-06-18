from airflow import DAG
from airflow.sensors.bash import BashSensor
from airflow.operators.bash import BashOperator

with DAG(
    dag_id='dags_bash_sensor',
    schedule_interval=None,
    start_date=None,
    catchup=False
) as dag:
    sensor_task_by_poke = BashSensor(
        task_id='sensor_task_by_poke',
        env={'FILE':'opt/airflow/files/bikeList/{{data_interval_end.in_timezone("Asia/Seoul") | ds_nodash }}/bikeList.csv'},
        bash_command=f"""
        echo $FILE &&
        if [ -f $FILE ]; then
            exit 0
        else
            exit 1
        fi
        """,
        poke_interval=30,
        timeout=60 * 2,
        mode="poke",
        soft_fail=False
    )