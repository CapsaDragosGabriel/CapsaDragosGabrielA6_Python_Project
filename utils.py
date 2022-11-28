from datetime import datetime
import psutil
import os
import time
import sys
import random
import time
import logging
import fancy
import simple


def get_time():
    """
    :return:
    data+ora curenta in format string
    """
    now = datetime.now()
    current_time = now.strftime("%H:%M:%S")
    return current_time


def check_if_process_runs(process_name):
    """
    verifica daca am un proces running cu numele specificat
    """
    # caut numele in list de procese
    for proc in psutil.process_iter():
        try:
            # daca l-am gasit
            if process_name.lower() in proc.name().lower() and len(process_name) == len(proc.name()):
                return True
        except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
            pass
    return False


def get_name(path):
    """
    obtine numele procesului din calea executabilului
    """
    nume_proces = os.path.basename(path)
    return nume_proces
