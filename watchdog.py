import psutil
import os
import sys
import random
import time
import logging

from datetime import datetime


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


def log_header(printHeader):
    """
    pune un header  de forma
    Date+Time | Process Name | Status
    ---------------------------------
    """
    logging.basicConfig(filename=sys.argv[3],
                        format='%(datetime)s%(spaces)s| %(proc)s%(procspaces)s | %(status)s',
                        filemode="a")
    if printHeader:
        logger = logging.getLogger()
        logger.setLevel(logging.INFO)
        d = {'datetime': 'Date+Time', 'spaces': ' ' * (len(time.asctime()) - 8), 'proc': 'Process_Name',
             'procspaces': ' ' * 15, 'status': 'Status'}
        try:
            logger.info('', extra=d)
        except Exception as e:
            raise Exception("logger header exception")

        d = {'datetime': '-' * len("Date+Time"), 'spaces': '-' * (len(time.asctime()) - 8),
             'proc': '-' * len("Process Name"), 'procspaces': "-" * 15, 'status': '------'}
        try:
            logger.info('', extra=d)
        except Exception as e:
            raise Exception("logger filler line exception")


def log_header_simple(printHeader):
    """
        pune un header  de forma
        Date+Time  Process Name  Status
    """
    logging.basicConfig(filename=sys.argv[3],
                        format='[%(asctime)s] %(proc)s %(status)s',
                        filemode="a")
    if printHeader:
        logger = logging.getLogger()
        logger.setLevel(logging.INFO)
        d = {'datetime': 'Date+Time', 'proc': 'Process_Name', 'status': 'Status'}
        try:
            logger.info('', extra=d)
        except Exception as e:
            raise Exception("logger header exception")


def log_status_simple(name, status):
    """
    pune linii de tipul:
    Date+Time ProcessName Status
    """
    logger = logging.getLogger()
    logger.setLevel(logging.INFO)
    if status:
        status = "Alive"
    else:
        status = "Dead"
    d = {'datetime': time.asctime(), 'spaces': ' ', 'proc': name,
         'procspaces': ' ' * (15 + len("Process_Name") - len(name)), 'status': status}
    try:
        if status:
            logger.info("", extra=d)
        else:
            logger.info("", extra=d)
    except Exception as e:
        raise Exception("logger exception")


def logStatus(name, status):
    """
        pune linii de tipul:
        Date+Time |  ProcessName |  Status
    """
    logger = logging.getLogger()
    logger.setLevel(logging.INFO)
    if status:
        status = "Alive"
    else:
        status = "Dead"
    d = {'datetime': time.asctime(), 'spaces': ' ', 'proc': name,
         'procspaces': ' ' * (15 + len("Process_Name") - len(name)), 'status': status}
    try:
        if status:
            logger.info("", extra=d)
        else:
            logger.info("", extra=d)
    except Exception as e:
        raise Exception("logger exception")


def getName(path):
    """
    obtine numele procesului din calea executabilului
    """
    i = 1
    ok = False
    while path[-i] != "\\" and i < len(path):
        i += 1
        if path[-i] == "\\":
            ok = True
    if ok:
        poz = len(path) - i + 1
        numeProces = path[poz:]
        # print("NUME PROCES",numeProces[:len(numeProces)-4])
    else:
        numeProces = path
    return numeProces


if __name__ == '__main__':
    file_exists = True
    if not os.path.isfile(sys.argv[3]):
        file_exists = False

    path = sys.argv[1]

    processName = getName(path)

    # aleg ce fel de formatare vreau sa aiba fisierul

    # logHeader(not file_exists)
    log_header_simple(not file_exists)

    print(processName)

    while True:
        if not check_if_process_runs(processName):
            print("nu-i pornit")
            # logStatus(processName, status=checkIfProcessRunning(processName))
            log_status_simple(processName, status=check_if_process_runs(processName))
            r = random.randint(1, 10)
            os.startfile(sys.argv[1])
        else:
            # logStatus(processName, status=checkIfProcessRunning(processName))
            log_status_simple(processName, status=check_if_process_runs(processName))
            print("e pornit ")
        time.sleep(int(sys.argv[2]))
