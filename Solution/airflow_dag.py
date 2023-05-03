from airflow import DAG
from airflow.operators import BashOperator
import datetime

PATH = input("Enter the directory where all three files to run are present: ")

default_args = {
        'owner': 'airflow',
        'depends_on_past': False,
        'start_date': datetime.date(2023, 05, 01)
        'email_on_failure': False,
        'email_on_retry': False,
        'retries': 1,
        'retry_delay': timedelta(minutes=5),
        'catchup': False
      }

dag = DAG('airflow_dag', default_args=default_args)

t1 = BashOperator(
    task_id='testairflow1',
    bash_command=f'python {PATH}/problem_1.py',
    dag=dag
    )

t2 = BashOperator(
    task_id='testairflow2',
    bash_command=f'python {PATH}/problem2.py',
    dag=dag
    )

t3 = BashOperator(
    task_id='testairflow3',
    bash_command=f'python {PATH}/problem3.py',
    dag=dag
    )

t1 >> t2 >> t3