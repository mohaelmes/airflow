from datetime import datetime
from airflow import DAG
from airflow.operators.dummy_operator import DummyOperator

default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'start_date': datetime(2023, 1, 1),
    'email_on_failure': False,
    'email_on_retry': False,
}

dag = DAG(
    'prueba_dag',
    default_args=default_args,
    description='Un DAG de prueba',
    schedule_interval=None,
)

dummy_task = DummyOperator(
    task_id='dummy_task',
    dag=dag,
)
