"""
Created on 28-Feb-2022
@author: nimish.jain@airlinq.com

Script to change the state of IMSI to terminate if the number of days of IMSI in Deactivated state is equal to or
greater then defined number of days
"""


import mysql.connector
from mysql.connector import Error as SQL_ERR
from config import meta_db_configs,no_of_days
from api_initiator import api_call
from logger import get_logger

from os.path import dirname, abspath

dir_path = dirname(abspath(__file__))
log_file_name = "amx_imsi_deactivate_state.txt"

no_of_days = no_of_days

logger = get_logger(dir_path, log_file_name)

jdbcMetaDatabase = meta_db_configs["DATABASE"]
host =  meta_db_configs["HOST"]
username = meta_db_configs["USER"]
password = meta_db_configs["PASSWORD"]
jdbcPort = meta_db_configs["PORT"]

def mysql_connection():
        try:
            mysql_conn = mysql.connector.connect(host=host, user=username,
             database=jdbcMetaDatabase, password=password, port=jdbcPort)
            logger.info("my sql connection established")
        except Exception:
                logger.error("my sql connection error")
        return mysql_conn

db = mysql_connection()
cursor = db.cursor()

q = "SELECT IMSI FROM assets WHERE DATE(STATE_MODIFIED_DATE)<= DATE_SUB(DATE(NOW()),INTERVAL %s DAY) AND STATE='Deactivated';"%(no_of_days)

try:
    cursor.execute(q)
    data = cursor.fetchall()
    logger.info("Number of imsi : {} deactivated for past {} days".format(len(data), no_of_days))
    print(data)
except:
    logger.error("error while fetching deactivated IMSI data from sql querry for {} days".format(no_of_days))

cursor.close()
db.close()

Imsi_state_change = api_call()
try:
    token = Imsi_state_change.auth()
except:
    logger.error("API authorization error")

for deactivated_imsi in data:
    deactivated_imsi_data = {
     "imsi" : [deactivated_imsi[0]],
      "newState" : "Terminate"
        }
    try:
       status =  None
       content = None
       status, content = Imsi_state_change.sim_state_change(deactivated_imsi_data,token)

       logger.info("deactivated imsi: {} terminated request status {}".format(deactivated_imsi[0], status))
       logger.info("deactivated imsi: {} terminated response data {}".format(deactivated_imsi[0], content))
    except Exception as e:
       logger.error("deactivated imsi: {} terminated request status {}".format(deactivated_imsi[0], status))
       logger.error("deactivated imsi: {} terminated response data {}".format(deactivated_imsi[0], content))
       print(e)


