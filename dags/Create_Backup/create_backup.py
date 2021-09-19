"""
Author: Sony Shrestha
Created Date:2020-07-28
Descripion  : Dag program for Create Backup.
"""

#importing default modules
import os
import shutil
import pendulum
from datetime import timedelta, datetime
import pandas as pd

#importing airflow modules
from airflow import DAG
from airflow.utils import timezone
from airflow.utils.dates import days_ago
from airflow.operators.bash_operator import BashOperator
from airflow.operators.dummy_operator import DummyOperator
from airflow.operators.mysql_operator import MySqlOperator
from airflow.operators.python_operator import PythonOperator
from airflow.operators.email_operator import EmailOperator
from airflow.operators.python_operator import BranchPythonOperator
from airflow.operators import TriggerDagRunOperator

from airflow.operators.sensors import SqlSensor


#importing custom modules
from Create_Backup.utilities.utilities import *
from Create_Backup.utilities.variables import *

import logging

local_tz = pendulum.timezone('Asia/Kathmandu')
start_date = datetime(**START_DATE, tzinfo=local_tz)

# These args will get passed on to each operator
# You can override them on a per-task basis during operator initialization
default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'start_date': start_date,
    'email': EMAIL_LIST,
    'email_on_failure': False,
    'email_on_retry': False,
    # 'retries': 1,
    # 'retry_delay': timedelta(minutes=5),
    # 'queue': 'bash_queue',
    # 'pool': 'backfill',
    # 'priority_weight': 10,
    # 'end_date': datetime(2016, 1, 1),
    # 'wait_for_downstream': False,
    # 'dag': dag,
    # 'sla': timedelta(hours=2),
    # 'execution_timeout': timedelta(seconds=300),
    # 'on_failure_callback': some_function,
    # 'on_success_callback': some_other_function,
    # 'on_retry_callback': another_function,
    # 'sla_miss_callback': yet_another_function,
    # 'trigger_rule': 'all_success'
}

dag = DAG(
    'Create_Backup',
    default_args=default_args,
    description='Create Database Backup',
    schedule_interval=None,
    catchup=False
)




create_database_bkp = BashOperator(
    task_id='create_database_bkp',
    bash_command= os.path.join(BACKUP_SCRIPT_LOCATION,'create_bkp.sh ')+mysql_host+' '+mysql_username+' '+mysql_password+' '+backup_db_name+' '+os.path.join(BACKUP_SCRIPT_LOCATION,'Backup')+' '+os.path.join(MYCNF_LOCATION,'my.cnf'),
    # on_success_callback=notify_email_success,
    on_failure_callback=notify_email_failure,
    params={
        "email_list":EMAIL_LIST,
        "task_success_msg":"Backup of application pointing database has been successfully created in location "+BACKUP_SCRIPT_LOCATION+" Backup/",
        "task_failure_msg":"Filed to create backup of application pointing database."
    },
    trigger_rule = 'one_success',
    dag=dag
)


create_database_bkp
