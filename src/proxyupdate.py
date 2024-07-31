import requests
import os
from pystyle import Colors, Colorate
from colorama import Fore
import time


os.system("cls || clear")
print(Colorate.Vertical(Colors.red_to_yellow, """
███    ██  ██████  ██          ██      ██ ███    ██ ██   ██     ███████ ██████   █████  ███    ███ ███    ███ ███████ ██████
████   ██ ██       ██          ██      ██ ████   ██ ██  ██      ██      ██   ██ ██   ██ ████  ████ ████  ████ ██      ██   ██
██ ██  ██ ██   ███ ██          ██      ██ ██ ██  ██ █████       ███████ ██████  ███████ ██ ████ ██ ██ ████ ██ █████   ██████
██  ██ ██ ██    ██ ██          ██      ██ ██  ██ ██ ██  ██           ██ ██      ██   ██ ██  ██  ██ ██  ██  ██ ██      ██   ██
██   ████  ██████  ███████     ███████ ██ ██   ████ ██   ██     ███████ ██      ██   ██ ██      ██ ██      ██ ███████ ██   ██

- By Lopusnik + Pers0nalPr0xy (EMKO-DEVELOPERS)

    """))
print("")
print(f"{Fore.YELLOW}(( ? )) {Fore.RESET}UPDATING PROXIES...")


url = "https://api.proxyscrape.com/v2/?request=displayproxies&protocol=http&timeout=1000000000&country=all&ssl=all&anonymity=all"

response = requests.get(url)
proxy_list = response.text.strip().split('\n')

with open('http.txt', 'w') as f:
    for proxy in proxy_list:
        f.write(proxy + '\n')


os.rename('http.txt', 'unchecked.txt')
time.sleep(4)
os.system("cd .. && python3 start.py")
