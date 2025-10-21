from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime, timedelta
import sys
import os
from airflow.operators.bash import BashOperator
sys.path.append(os.path.dirname(__file__))
from store_pipeline.data_loader import load_data
import yagmail

SENDER_EMAIL = 'sender@gmail.com'
SENDER_PASSWORD = ''
RECIPIENTS = ['recipient@gmail.com']

def send_email(**context):
    try:
        yag = yagmail.SMTP(SENDER_EMAIL, SENDER_PASSWORD)
        subject = "Airflow Notification - EcommerceProject"
        body = "Hello,\n\nYour Store Pipeline has completed successfully.\n\nRegards,\nAirflow"
        yag.send(
            to=RECIPIENTS,
            subject=subject,
            contents=body
        )
        print("✅ Email sent successfully")
    except Exception as e:
        print(f"❌ Error sending email: {str(e)}")

with DAG(
    dag_id='store_pipeline_dag',
    description='A DAG for the Store Pipeline',
    schedule = '@daily',
    start_date=datetime(2025, 10, 21),
    catchup=False,
    tags=['email'],
    default_args={
        'owner': 'airflow',
        'retries': 1,
        'retry_delay': timedelta(minutes=1),
    }
) as dag:
    Load_data_task = PythonOperator(
        task_id='load_data_task',
        python_callable=load_data
    )
    dbt_run_task = BashOperator(
        task_id="dbt_run_task",
        cwd="/root/airflow/dags/store_pipeline",
        bash_command="/root/venvs/airflow_3.1.0/bin/dbt run"
    )
    send_email_task = PythonOperator(
        task_id='send_email_task',
        python_callable=send_email
    )
Load_data_task >> dbt_run_task >> send_email_task