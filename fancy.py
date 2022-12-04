import sys
import time
import logging


def log_header(printHeader):
    """
    pune un header  de forma
    Date+Time | Process Name | Status
    ---------------------------------
    """
    try:
        logging.basicConfig(filename=sys.argv[3],
                            format='%(datetime)s%(spaces)s| %(proc)s%(procspaces)s | %(status)s',
                            filemode="a")
    except Exception as e:
        print(e)
        raise Exception("Can't write in the file.")
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
            print(e)
            raise Exception("logger filler line exception")


def log_status(name, status):
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
        print(e)
        raise Exception("logger status exception")
