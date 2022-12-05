import sys
import logging
import utils


def log_header(printHeader):
    """
        pune un header  de forma
        Date+Time  Process Name  Status
    """
    try:
        logging.basicConfig(filename=sys.argv[3],
                            format='[%(asctime)s] %(proc)s %(status)s %(cpu)s',
                            filemode="a")
    except Exception as e:
        print(e)
        raise Exception("Can't write in the file.")
    if printHeader:
        logger = logging.getLogger()
        logger.setLevel(logging.INFO)
        d = {'proc': 'Process_Name', 'status': 'Status', 'cpu': 'Cpu_Usage'}
        try:
            logger.info('', extra=d)
        except Exception as e:
            print(e)
            raise Exception("logger header exception")


def log_status(name, status):
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
    if utils.get_process(name):
        d = {'proc': name,
             'status': status,
             'cpu': utils.get_process(name).cpu_percent()}
    else:
        d = {'proc': name,
             'status': status,
             'cpu': "0%"}

    try:
        if status:
            logger.info("", extra=d)
        else:
            logger.info("", extra=d)
    except Exception as e:
        print(e)
        raise Exception("logger exception")
