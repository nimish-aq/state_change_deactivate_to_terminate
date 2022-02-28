"""
Created on 28-Feb-2022
@author: Nimish.jain@airlinq.com

script for basic configuration of logger module
"""

import logging

from os.path import join

def get_logger(dir_path, log_file_name):
    file_path = join(dir_path, log_file_name)

    # print(log_file_base_path + log_file_name)

    aq_logger = logging.getLogger(f'log_file_name')
    logging.basicConfig(filename=file_path,
                        format='%(asctime)s - %(levelname)s : %(message)s',
                        filemode='a')

    # Setting the threshold of aq_logger to DEBUG
    aq_logger.setLevel(logging.DEBUG)
    return aq_logger
