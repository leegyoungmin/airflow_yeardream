from airflow import DAG
from airflow.sensors.python import PythonSensor
import pendulum
from airflow.hooks.base import BaseHook

with DAG(
    dag_id='dags_python_sensor',
    start_date=pendulum.datetime(2024, 6, 16, tz="Asia/Seoul"),
    schedule='10 1 * * *',
    catchup=False
) as dag:
    def check_api_update(http_conn_id, endpoint, check_date, **kwargs):
        import requests
        import json

        connection = BaseHook.get_connection(http_conn_id)
        url = f"http://{connection.host}:{connection.port}/{endpoint}/1/5/{check_date}"
        print(f'url: {url}')
        response = requests.get(url)
        contents = json.loads(response.text)
        print(f'response : {contents}')
        code = contents.get('CODE')

        if code is not None and code == 'INFO-200':
            print('상태 코드 : INFO-200, 데이터 미갱신')
            return False
        elif code is None:
            keys = list(contents.keys())
            response_code = contents.get(keys[0]).get('RESULT').get('CODE')

            if response_code == 'INFO-000':
                print("상태코드 : INFO-000, 데이터 갱신 확인")
                return True
        else:
            print("상태코드 불분명")
            return False

    sensor_task = PythonSensor(
        task_id='sensor_task',
        python_callable=check_api_update,
        op_kwargs={
            'http_conn_id': 'openapi.seoul.go.kr',
            'endpoint': '{{var.value.apikey_openapi_seoul_go_kr}}/json/tbCycleRentUseDayInfo',
            'check_date': '{{date_interval_start.in_timezone("Asia/Seoul") | no_dash }}'
        },
        poke_interval=600,
        mode="reschedule"
    )