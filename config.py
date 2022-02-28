
"""
Created on 28-Feb-2022
@author: Nimish.jain@airlinq.com

Config file to store  DB, no_of_days, authorization api config and sim state change url
"""



no_of_days = 12

# dev
meta_db_configs = {
    "HOST": "192.168.1.114",
    "USER": "root",
    "DATABASE": "iotsmp_dev",
    "PASSWORD": "Admin@123",
    "PORT": "3306"
}

# dev
auth_api_config = {
"authentication_api_url": "https://i.airlinq.com:8019/gcapi/auth",
"username": "gtadmin",
"password": "Admin@123"
}

# dev
action_api_config = {
"sim_state_change_url" : "https://i.airlinq.com:8019/gcapi/device/changeState",

}



