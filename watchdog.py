import os
import sys
import time
import utils
import fancy
import simple

if __name__ == '__main__':
    if len(sys.argv)==1:
        print("Programul trebuie apelat sub forma: python3 watchdog.py cale_executabil interval fisier_log (mod) (timp total)")
    if len(sys.argv) < 4 or len(sys.argv) > 6:
        raise Exception("invalid number of arguments")
    file_exists = True
    if not os.path.isfile(sys.argv[3]):
        file_exists = False

    path = sys.argv[1]
    process_name = utils.get_name(path)
    # aleg ce fel de formatare vreau sa aiba fisierul
    mode = utils.get_mode()
    # specific cat timp vreau sa ruleze watchdog
    run_time = utils.get_run_time()
    if mode == 'f':
        fancy.log_header(not file_exists)
    else:
        simple.log_header(not file_exists)

    print(process_name)
    print(mode)
    current_run_time = 0
    while True:
        if not utils.check_if_process_runs(process_name):
            print("dead")
            if mode == 'f':
                fancy.log_status(process_name, status=utils.check_if_process_runs(process_name))
            else:
                simple.log_status(process_name, status=utils.check_if_process_runs(process_name))
            try:
                os.startfile(sys.argv[1])
            except Exception as e:
                print(e)  # daca nu poate sa porneasca executabilul il voi lasa oricum sa faca logging
        else:
            if mode == 'f':
                fancy.log_status(process_name, status=utils.check_if_process_runs(process_name))
            else:
                simple.log_status(process_name, status=utils.check_if_process_runs(process_name))
            print("alive")
        current_run_time += int(sys.argv[2])
        if run_time != 0:
            if current_run_time > run_time:
                break
        time.sleep(int(sys.argv[2]))
