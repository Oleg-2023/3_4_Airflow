from datetime import datetime, timedelta, date
from airflow import DAG
from airflow.operators.bash import BashOperator
from airflow.operators.empty import EmptyOperator

# аргументы дага по умолчанию
default_args = {
    "owner": "Oleg",
    "retries": 1,
    "retry_delay": timedelta(minutes=1),
    "start_date": datetime(2023, 11, 14),
    "template_searchpath" : "/tmp"
}

with DAG(dag_id="01_bash_message", 
         default_args=default_args, 
         description="bash operator example DAG",
         schedule_interval="* * * * *",
         tags=["bash","Oleg"], 
         catchup=True) as dag:

    start = EmptyOperator(task_id='start') 
    step = EmptyOperator(task_id="step")

    bash = BashOperator(
        task_id='bash_operator_task',
        bash_command=f"echo 'Good morning my diggers!'"
    )

    end = EmptyOperator(task_id='end')

    start >> step >> bash >> end

