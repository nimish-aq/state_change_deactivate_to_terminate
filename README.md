##### Project : changes the status of IMSI, Deactivated for defined number of days to Terminate state

###### INSTALLATION
* RUN  ``pip install -r requirements.txt``

* run ``python3 device_to_terminate_state.py ``

##### Database config in config.py file:

meta_db_configs = {
    "HOST": "192.168.1.114",
    "USER": "root",
    "DATABASE": "iotsmp_dev",
    "PASSWORD": "Admin@123",
    "PORT": "3306"
}

##### Number of days for which IMSI's are deactivated and needs to be terminated: config.py

no_of_days = __

If the number of days is equal to or greater than this period....device will move to a Terminate state

##### API authorization configuration in config.py:

auth_api_config = {
"authentication_api_url": "https://i.airlinq.com:8019/gcapi/auth",
"username": "gtadmin",
"password": "Admin@123"
}

##### IMSI state change API URL in config.py:

action_api_config = {
"sim_state_change_url" : "https://i.airlinq.com:8019/gcapi/device/changeState",

}

