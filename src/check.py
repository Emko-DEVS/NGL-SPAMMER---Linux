import requests
import threading
import argparse
import os
from colorama import Fore
import time

def test_proxy(proxy, working_proxies_file):
    try:
        response = requests.get("http://google.com", proxies={"http": proxy, "https": proxy}, timeout=5)
        if response.status_code == 200:
            print(f"{Fore.GREEN}(( + )) {Fore.RESET}Working proxy: {Fore.GREEN}{proxy}")
            with open(working_proxies_file, "a") as wp_file:
                wp_file.write(proxy + '\n')
        if response.status_code == 408:
            print(f"{FORE.RED} (( - ))) {Fore.RESET}NotWorking proxy: {Fore.RED}{proxy}")
    except requests.RequestException:
        pass

def main():
    parser = argparse.ArgumentParser(description="HTTP Proxy Checker")
    parser.add_argument("proxy_list", help="Path to a file containing proxy addresses, one per line")
    parser.add_argument("--threads", type=int, default=10, help="Number of threads to use for checking proxies")
    args = parser.parse_args()

    with open(args.proxy_list, "r") as file:
        proxy_list = file.read().splitlines()

    working_proxies_file = "proxies.txt"

    threads = []
    for proxy in proxy_list:
        thread = threading.Thread(target=test_proxy, args=(proxy, working_proxies_file))
        thread.start()
        threads.append(thread)

        if len(threads) >= args.threads:
            for t in threads:
                t.join()
            threads = []

    for t in threads:
        t.join()

if __name__ == "__main__":
    main()

time.sleep(2)
os.system("cd .. && python3 start.py")
