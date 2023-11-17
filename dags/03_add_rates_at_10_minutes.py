import requests
from datetime import datetime, timedelta, date
from airflow import DAG
from airflow.operators.bash import BashOperator
from airflow.operators.postgres_operator import PostgresOperator
from airflow.operators.python_operator import PythonOperator
from airflow.operators.empty import EmptyOperator
import modules.functions as functions

# аргументы дага по умолчанию
default_args = {
    "owner": "Oleg",
    "start_date": datetime(2023, 11, 16)
}

with DAG(dag_id="03_add_rates_at_10_minutes", 
         default_args=default_args, 
         description="bash operator example DAG",
         schedule_interval=timedelta(minutes=10),
         tags=["postgres", "api", "Oleg"], 
         catchup=False) as dag:

    start = EmptyOperator(task_id='start') 
  
    create_quotes_table = PostgresOperator(
        task_id='create_quotes_table',
        postgres_conn_id='conn1',
        sql="sql/create_quotes.sql",
        dag=dag
    )

    add_data_psql = PythonOperator(
        task_id='add_data_psql',
        python_callable=functions.add_data_psql,
        dag=dag
    )

    end = EmptyOperator(task_id='end')

start >> create_quotes_table >> add_data_psql >> end

