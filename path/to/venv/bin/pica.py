import os
import concurrent.futures
import requests
from colorama import Fore
from pystyle import Colors, Colorate
import time
import requests
import re
import hashlib
import sys
import platform
import getpass, os, uuid, hashlib, getmac as gma

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

    print(Colorate.Vertical(Colors.blue_to_purple, """
███    ██  ██████  ██          ██      ██ ███    ██ ██   ██     ███████ ██████   █████  ███    ███ ███    ███ ███████ ██████
████   ██ ██       ██          ██      ██ ████   ██ ██  ██      ██      ██   ██ ██   ██ ████  ████ ████  ████ ██      ██   ██
██ ██  ██ ██   ███ ██          ██      ██ ██ ██  ██ █████       ███████ ██████  ███████ ██ ████ ██ ██ ████ ██ █████   ██████
██  ██ ██ ██    ██ ██          ██      ██ ██  ██ ██ ██  ██           ██ ██      ██   ██ ██  ██  ██ ██  ██  ██ ██      ██   ██
██   ████  ██████  ███████     ███████ ██ ██   ████ ██   ██     ███████ ██      ██   ██ ██      ██ ██      ██ ███████ ██   ██

- By Lopusnik + Pers0nalPr0xy (EMKO-DEVELOPERS)

    """))

    nglusername = input(Colorate.Vertical(Colors.blue_to_purple, "NGL LINK Username: "))
    message = input(Colorate.Vertical(Colors.blue_to_purple, "NGL Message: "))
    Count = int(input(Colorate.Vertical(Colors.blue_to_purple, "MESSAGE Count: ")))
    thread_count = int(input(Colorate.Vertical(Colors.blue_to_purple, "Number of Threads: ")))

    proxy_file = "proxies.txt"

    with open(proxy_file, "r") as f:
        proxy_list = f.read().splitlines()

    print(Colorate.Vertical(Colors.green_to_blue, "**********************************************************"))

    while Count > 0:
        # Using ThreadPoolExecutor for concurrent execution of send_question
        with concurrent.futures.ThreadPoolExecutor() as executor:
            futures = [executor.submit(send_question, nglusername, message, {"http": proxy, "https": proxy}) for proxy in proxy_list]

            # Waiting for all futures to complete
            concurrent.futures.wait(futures)

        Count -= len(proxy_list)
        if Count > 0:
            pass

    print("All tasks completed.")

try:
    url = 'http://54.36.239.97:20008/api/client'

    # Load license key from file
    with open('license.key', 'r') as license_file:
        licensekey = license_file.read().strip()

    product = 'NGL-SPAMMER'
    version = '1.0'
    api_key = 'nHvX7wS8TR27Rqk4S1EyDW68DX9z9h4k4Me2dCDv9Y'
    hwid = hashlib.sha256((os.name + getpass.getuser() + gma.get_mac_address() + str(hex(uuid.getnode()))).encode()).hexdigest()

    headers = {'Authorization': api_key}
    data = {
        'licensekey': licensekey,
        'product': product,
        'version': version,
        'hwid': hwid
    }

    response = requests.post(url, json=data, headers=headers)

    res_data = response.json()

    if 'status_code' not in res_data or 'status_id' not in res_data:
        print(f" {Fore.RED}(( ! )) {Fore.RESET}Your license is invalid.")
        exit(1)

    if res_data.get('status_overview') != "success":
        print(f" {Fore.RED}(( ! )) {Fore.RESET}Your License is invalid")
        print(" ")
        print(" |- Reason: " + res_data.get('status_msg'))
        print(" |- Status Code: \x1b[31m" + str(res_data.get('status_code')) + "\x1b[0m")
        exit(1)
    else:
        ngl()

except Exception as err:
    print("Authentication failed")
    print(err)
    exit(1)




