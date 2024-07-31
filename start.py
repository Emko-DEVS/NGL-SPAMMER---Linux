import os
from pystyle import Colors, Colorate
from colorama import Fore


def startup():
    os.system("cls || clear")
    print(Colorate.Vertical(Colors.red_to_yellow, """


                                                                                                                                     ,MMM8&&&.
                                                                                                                                _...MMMMM88&&&&..._
                                                                                                                             .::'''MMMMM88&&&&&&'''::.
███╗   ██╗ ██████╗ ██╗         ███████╗██████╗  █████╗ ███╗   ███╗███╗   ███╗███████╗██████╗                                ::     MMMMM88&&&&&&     ::
████╗  ██║██╔════╝ ██║         ██╔════╝██╔══██╗██╔══██╗████╗ ████║████╗ ████║██╔════╝██╔══██╗                               '::....MMMMM88&&&&&&....::'
██╔██╗ ██║██║  ███╗██║         ███████╗██████╔╝███████║██╔████╔██║██╔████╔██║█████╗  ██████╔╝                                  `''''MMMMM88&&&&''''`
██║╚██╗██║██║   ██║██║         ╚════██║██╔═══╝ ██╔══██║██║╚██╔╝██║██║╚██╔╝██║██╔══╝  ██╔══██╗                                        'MMM8&&&'
██║ ╚████║╚██████╔╝███████╗    ███████║██║     ██║  ██║██║ ╚═╝ ██║██║ ╚═╝ ██║███████╗██║  ██║
╚═╝  ╚═══╝ ╚═════╝ ╚══════╝    ╚══════╝╚═╝     ╚═╝  ╚═╝╚═╝     ╚═╝╚═╝     ╚═╝╚══════╝╚═╝  ╚═╝


- By Lopusnik + Pers0nalPr0xy (EMKO-DEVELOPERS)

    """))
    while True:
        command = input("[NGLSpammer@Root] $ ")

        if command == "help":
            print("")
            print(f"{Fore.YELLOW}NGLSpammer{Fore.RESET} commands:")
            print(f" {Fore.GREEN}start {Fore.WHITE}- {Fore.BLUE}start the program{Fore.RESET}")
            print(f" {Fore.GREEN}proxy {Fore.WHITE}- {Fore.BLUE}updates proxies list{Fore.RESET}")
            print(f" {Fore.GREEN}check {Fore.WHITE}- {Fore.BLUE}check proxies if they are alive{Fore.RESET}")
            print(f" {Fore.GREEN}help {Fore.WHITE}- {Fore.BLUE}help message{Fore.RESET}")
            print(f" {Fore.GREEN}about {Fore.WHITE}- {Fore.BLUE}about the developers{Fore.RESET}")
            print("")
        elif command == "proxy":
            os.system("cd src && python3 proxyupdate.py")
        elif command == "check":
            os.system("cd src && python3 check.py unchecked.txt --threads 1000")
        elif command == "start":
            os.system("cd src && python3 pica.py")
        elif command == "exit": 
            break
        else:
            print(f" {Fore.RED}(( ! )) {Fore.RESET}invalid command")


startup()
