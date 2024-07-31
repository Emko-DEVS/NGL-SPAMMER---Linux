import os
import concurrent.futures
import requests
from colorama import Fore
from pystyle import Colors, Colorate
import time
import requests
import random
import re
import hashlib
import sys
import platform
import getpass, os, uuid, hashlib, getmac as gma
from itertools import cycle


def send_question(nglusername, message, proxy):
    R = '\033[31m'
    G = '\033[32m'
    W = '\033[0m'

    headers = {
        'Host': 'ngl.link',
        'sec-ch-ua': '"Google Chrome";v="113", "Chromium";v="113", "Not-A.Brand";v="24"',
        'accept': '*/*',
        'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
        'x-requested-with': 'XMLHttpRequest',
        'sec-ch-ua-mobile': '?0',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36',
        'sec-ch-ua-platform': '"Windows"',
        'origin': 'https://ngl.link',
        'sec-fetch-site': 'same-origin',
        'sec-fetch-mode': 'cors',
        'sec-fetch-dest': 'empty',
        'referer': f'https://ngl.link/{nglusername}',
        'accept-language': 'tr-TR,tr;q=0.9,en-US;q=0.8,en;q=0.7',
    }

    data = {
        'username': f'{nglusername}',
        'question': f'{message}',
        'deviceId': '0',
        'gameSlug': '',
        'referrer': '',
    }


    try:
        response = requests.post('https://ngl.link/api/submit', headers=headers, data=data, proxies=proxy, timeout=10)
        if response.status_code == 200:
            print(G + "(( + ))" + W + " Send =>" + G + "{}".format(nglusername) + W)
        else:
            print(R + "(( ! ))" + W + " Not Send")
    except Exception as e:
        pass

def ngl():
    os.system('cls' if os.name == 'nt' else 'clear')

    print(Colorate.Vertical(Colors.red_to_yellow, """
███    ██  ██████  ██          ██      ██ ███    ██ ██   ██     ███████ ██████   █████  ███    ███ ███    ███ ███████ ██████
████   ██ ██       ██          ██      ██ ████   ██ ██  ██      ██      ██   ██ ██   ██ ████  ████ ████  ████ ██      ██   ██
██ ██  ██ ██   ███ ██          ██      ██ ██ ██  ██ █████       ███████ ██████  ███████ ██ ████ ██ ██ ████ ██ █████   ██████
██  ██ ██ ██    ██ ██          ██      ██ ██  ██ ██ ██  ██           ██ ██      ██   ██ ██  ██  ██ ██  ██  ██ ██      ██   ██
██   ████  ██████  ███████     ███████ ██ ██   ████ ██   ██     ███████ ██      ██   ██ ██      ██ ██      ██ ███████ ██   ██

- By Lopusnik + Pers0nalPr0xy (EMKO-DEVELOPERS) ccccccccc

    """))

    nglusername = input(f"NGL Username: {Fore.GREEN}")
    message_input = input(f"{Fore.RESET}NGL Message (leave blank to use messages from messages.txt): {Fore.GREEN}")
    Count = int(input(f"{Fore.RESET}MESSAGE Count: {Fore.GREEN}"))
    thread_count = int(input(f"{Fore.RESET}Number of Threads: {Fore.GREEN}"))

    proxy_file = "proxies.txt"

    with open(proxy_file, "r") as f:
        proxy_list = f.read().splitlines()

    with open("messages.txt", "r") as messages_file:
        messages = messages_file.read().splitlines()

    print(f"{Fore.RESET}")

    while Count > 0:
        with concurrent.futures.ThreadPoolExecutor(max_workers=thread_count) as executor:
            for proxy in proxy_list:
                if message_input:
                    current_message = message_input
                else:
                    current_message = random.choice(messages)

                executor.submit(send_question, nglusername, current_message, {"http": proxy, "https": proxy})
                Count -= 1
                if Count <= 0:
                    break

    print("All tasks completed.")
    os.system("cd .. && python3 start.py")


ngl()





