from prometheus_client import start_http_server, Info
import logging
import time
import platform
import os


logging.basicConfig(level=logging.INFO, filename="ms_prometheus.log", format="%(asctime)s %(levelname)s %(message)s")


def check_server_type() -> tuple: # определяет где запущен микросервис на физ сервере, ВМ или контейнере 
    try:
        os_type = platform.system()
        if os_type == "Windows":                               # тк код я писал на винде
            machine_type = "Phisical server"                   # тк по ТЗ у нас микросервис запускается только на linux виртуалках
            logging.info(f"OS and host type were defined: {os_type}, {machine_type}")
            return os_type, machine_type
        
        elif os_type == "Linux":
            vm_check = os.popen('dmesg 2>/dev/null | grep -i "hypervisor detected" 2>/dev/null').read()    # если это ВМ, то в dmesg будет запись Hypervisor detected
            if vm_check != "":
                machine_type = "Virtual machine"
                logging.info(f"OS and host type were defined: {os_type}, {machine_type}")
                return os_type, machine_type
            elif os.path.isfile("/.dockerenv"):   # проверяет есть ли такой файл. Он всегда создается в контейнерах 
                machine_type = "Container"
                logging.info(f"OS and host type were defined: {os_type}, {machine_type}")
                return os_type, machine_type
            else:
                machine_type = "Phisical server"                # если ничего на linux не подолшо занчит физический сервер
                logging.info(f"OS and host type were defined: {os_type}, {machine_type}")
                return os_type, machine_type
            
        else:
            logging.info(f"Unexpected OS: {os_type}")

    except Exception as error:
        logging.info("Cound not define server type: %s", error)
        return "Not defined", "Not defined"


if __name__ == '__main__':
    host_type = Info('host_type', 'OS and host type info')
    host_type.info({'OS': check_server_type()[0], 'machine': check_server_type()[1]})

    start_http_server(8080)
    logging.info("Prometheus service started.")

    try:
        while True:
            time.sleep(1)
    except:
        logging.info("Service was stopped by user.")
