import os
import sys
import time
import utils
import fancy
import simple


if __name__ == '__main__':
    file_exists = True
    if not os.path.isfile(sys.argv[3]):
        file_exists = False
    path = sys.argv[1]
    process_name = utils.get_name(path)
    # aleg ce fel de formatare vreau sa aiba fisierul
    fancy.log_header(not file_exists)
    # simple.log_header(not file_exists)

    print(process_name)

    while True:
        if not utils.check_if_process_runs(process_name):
            print("dead")
            fancy.log_status(process_name, status=utils.check_if_process_runs(process_name))
            # simple.log_status(processName, status=check_if_process_runs(processName))
            os.startfile(sys.argv[1])
        else:
            fancy.log_status(process_name, status=utils.check_if_process_runs(process_name))
            # simple.log_status(processName, status=check_if_process_runs(processName))
            print("alive")
        time.sleep(int(sys.argv[2]))
