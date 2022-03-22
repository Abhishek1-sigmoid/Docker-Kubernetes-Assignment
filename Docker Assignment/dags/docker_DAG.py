from airflow import DAG
from airflow.operators.python_operator import PythonOperator
from datetime import datetime, timedelta
from insert_entry import insert_entry_to_table

default_args = {
    "owner": "Abhishek",
    "depends_on_past": False,
    "start_date": datetime(2022, 3, 22),
    "email": ["airflow@airflow.com"],
    "email_on_failure": False,
    "email_on_retry": False,
    "retries": 1,
    "retry_delay": timedelta(minutes=2)
}

dag = DAG("Docker_DAG", default_args=default_args, schedule_interval="0 6 * * *")

t1 = PythonOperator(task_id='Insert_data_to_execution_table', python_callable=insert_entry_to_table, dag=dag)

t1
