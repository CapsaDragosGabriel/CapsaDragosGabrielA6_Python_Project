import sys
import psutil
import os


def get_run_time():
    if len(sys.argv) == 6:
        time = int(sys.argv[5])
    else:
        time = 0
    return time


def get_mode():
    mode = 's'
    if len(sys.argv) == 5:
        if sys.argv[4] == '-f':
            mode = 'f'
        elif sys.argv[4] == '-s':
            mode = 's'
        else:
            raise Exception("invalid 4th argument: mode can be -f or -s (fancy/simple)")
    return mode


def check_if_process_runs(process_name):
    """
    verifica daca am un proces running cu numele specificat
    """
    # caut numele in lista de procese
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
