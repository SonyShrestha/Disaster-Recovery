import os
from sqlalchemy import create_engine
from datetime import datetime
from Create_Backup.utilities.db_con import *
file_path = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))

def initialize_json_config():
    import json
    global CLIENT

    global BACKUP_SCRIPT_LOCATION
    global MYCNF_LOCATION  
    global EMAIL_LIST
    global CRON_EXPRESSION_CREATE_BACKUP

    global START_DATE
    
    global mysql_url
    global mysql_config
    global mysql_driver
    global mysql_host
    global mysql_username
    global mysql_password

    global backup_db_name

    with open(os.path.abspath(file_path + '/config/config.json'), 'r') as js:
        js_conf = json.load(js)


    CLIENT=js_conf['CLIENT']

    BACKUP_SCRIPT_LOCATION = js_conf['BACKUP_SCRIPT_LOCATION']
    MYCNF_LOCATION=js_conf['MYCNF_LOCATION']

    EMAIL_LIST=js_conf['EMAIL_LIST']

    CRON_EXPRESSION_CREATE_BACKUP = js_conf['CRON_EXPRESSION_CREATE_BACKUP']

    START_DATE = js_conf['START_DATE']  


    mysql_config=js_conf['connection']['mysql']
    mysql_host=js_conf['connection']['mysql']['host']
    mysql_driver=js_conf['connection']['mysql']['drivername']
    mysql_username=js_conf['connection']['mysql']['username']
    mysql_password=js_conf['connection']['mysql']['password']

    mysql_url=get_con_url(**js_conf['connection']["mysql"])

    backup_db_name=js_conf['backup_db_name']



def get_con_url(**conf):
    return conf["drivername"]+"://"+conf["username"]+":"+conf["password"]+"@"+conf["host"]


initialize_json_config()


