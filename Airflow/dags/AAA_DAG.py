import logging
from datetime import timedelta

from airflow import DAG
from airflow.operators.python import PythonOperator
from airflow.utils.dates import days_ago

default_args = {
    'owner':'airflow',
    'depends_on_past':False,
    'email':['airflow@example.com'],
    'email_on_failure':False,
    'email_on_retry':False,
    'retries':1,
    'retry_delay':timedelta(minutes=5),
}

# tasks
def init_dag():
    logging.info("performing init_dat")

def process():
    logging.info("performing processing")

def save():
    logging.info("performing saving")

def log():
    logging.info("performing log")

# Definir nuestro grafo aciclico dirigido
with DAG(
    'AAA_DAG',
    default_args= default_args,
    description='Test DAG',
    schedule_interval=timedelta(days=1),
    start_date=days_ago(2),
    tags=['example'],
) as dag:
    
    # definicion de las tareas
    init_dat_task = PythonOperator(task_id="init_dat", python_callable=init_dag)
    process_task = PythonOperator(task_id="process", python_callable=process)
    save_task = PythonOperator(task_id="save", python_callable=save)
    log_task = PythonOperator(task_id="log", python_callable=log)

    # Definir las dependencias entre nuestras tareas, orden
    init_dat_task >> process_task >> save_task >> log_task