
import os
import sys

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

clear_screen()


try:
    from colorama import Fore, Style, init
except ImportError:
    print("colorama modülü eksikmiş mk indiriyorum...")
    os.system(f"{sys.executable} -m pip install colorama")
    clear_screen()  
    from colorama import Fore, Style, init


init(autoreset=True)
banner = f"""{Fore.RED}
  ____      _    ____  ______   _______ _____ 
 |  _ \    / \  / ___|| __ ) \ / /_   _| ____|
 | |_) |  / _ \ \___ \|  _ \\ V /  | | |  _|  
 |  _ <  / ___ \ ___) | |_) || |   | | | |___ 
 |_| \_\/_/   \_\____/|____/ |_|   |_| |_____|
 KODU KÜÇÜK AMA İŞLEVİ BÜYÜK
 Version 1.0                                                      
{Fore.RESET}"""

import requests

while True:
    clear_screen()  
    
    print(banner)

    print(Fore.CYAN + "CODDED BY ROYZ")
    print(Fore.YELLOW + "1." + Fore.GREEN + " 2012 - 2019 ig random (AKTİF)")
    print(Fore.YELLOW + "2." + Fore.GREEN + " TikTok Too (BAKIMDA ÇALIŞMAZ)")
    print(Fore.YELLOW + "3." + Fore.GREEN + " Snap Tool (BAKIMDA ÇALIŞMAZ)\n")

    secim = input(Fore.MAGENTA + "Seçımını yap 1 - 3: ")

    if secim == "1":
        clear_screen()
        
        exec(requests.get("https://raw.githubusercontent.com/royzempire/ighit/refs/heads/main/random").text)
        sys.exit()

    elif secim == "2":
        clear_screen()
        
        exec(requests.get("https://raw.githubusercontent.com/royzempire/ighit/refs/heads/main/ra").text)
        sys.exit()

    elif secim == "3":
        clear_screen()
        
        exec(requests.get("https://raw.githubusercontent.com/royzempire/ighit/refs/heads/main/ram").text)
        sys.exit()

    else:
        print(Fore.RED + "\nYanlış seçim yaptın \n")
