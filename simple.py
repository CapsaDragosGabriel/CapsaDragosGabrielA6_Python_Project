import sys
import time
import logging


def log_header(printHeader):
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
        d = {'proc': 'Process_Name', 'status': 'Status'}
        try:
            logger.info('', extra=d)
        except Exception as e:
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
    d = {'proc': name,
         'status': status}
    try:
        if status:
            logger.info("", extra=d)
        else:
            logger.info("", extra=d)
    except Exception as e:
        raise Exception("logger exception")
