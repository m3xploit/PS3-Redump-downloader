import requests
import os

from bs4 import BeautifulSoup
from tqdm import tqdm
from colorama import Fore, Back, Style

link = "https://myrient.erista.me/files/Redump/Sony%20-%20PlayStation%203/"
roms = {}

print("Fetching ROMs ...")

try:
    base_req = requests.get(link)
except requests.ConnectionError:
    print("Connection error! Please check your internet connection and then try again.")
    input()
    exit()
except Exception as e:
    print("CRITICAL ERROR: " + str(e))
    input()
    exit()

if base_req.status_code != 200:
    print(f"Something went wrong! HTTP Status code: {base_req.status_code}")
    input()
    exit()

soup = BeautifulSoup(base_req.text, features="lxml")

print("Parsing ROMs ...")

for a in soup.find_all("a"):
    if ".zip" in a.get("href").lower():
        roms[a.get("title")] = link + a.get("href")

while True:
    if os.name.lower() == "nt":
        os.system("cls")
    else:
        os.system("clear")

    print(r"""
 ________  ________  ________  ________  ________     
|\   __  \|\   ____\|\_____  \|\   __  \|\   ___ \    
\ \  \|\  \ \  \___|\|____|\ /\ \  \|\  \ \  \_|\ \   
 \ \   ____\ \_____  \    \|\  \ \   _  _\ \  \ \\ \  
  \ \  \___|\|____|\  \  __\_\  \ \  \\  \\ \  \_\\ \ 
   \ \__\     ____\_\  \|\_______\ \__\\ _\\ \_______\
    \|__|    |\_________\|_______|\|__|\|__|\|_______|
             \|_________|                             
                                   
       @m3xploit - https://github.com/m3xploit
""")

    print(f"{len(roms)} PS3 ROMs loaded.")

    search = input("\nSearch for PS3 Game: ")

    matches = []
    for game in roms.items():
        if search.lower() in game[0].lower():
            matches.append(game)

    if not matches:
        print("No matches!")
        input("\nPress [ENTER] to continue.")
        continue

    for idx, (title, _) in enumerate(matches, start=1):
        print(f"{Fore.LIGHTYELLOW_EX}{idx}.{Fore.RESET} {title.replace('.zip', '')}")

    try:
        num = int(input(f"\nSelect a number ({Fore.LIGHTYELLOW_EX}1-{len(matches)}{Fore.RESET}): "))
        if num < 1 or num > len(matches):
            print("Invalid choice! Please select a valid number.")
            input("\nPress [ENTER] to continue.")
            continue
    except ValueError:
        print("Please enter a number, not text!")
        input("\nPress [ENTER] to continue.")
        continue

    title, url = matches[num - 1]
    print(f"\nDownloading: {title.replace('.zip', '')}")

    response = requests.get(url, stream=True)
    total_size = int(response.headers.get('content-length', 0))
    block_size = 1024  # 1 KB

    with open(title, "wb") as file, tqdm(
        desc="Progress",
        total=total_size,
        unit="B",
        unit_scale=True,
        unit_divisor=1024,
    ) as bar:
        for data in response.iter_content(block_size):
            file.write(data)
            bar.update(len(data))

    print(f"Saved as {title}")
    input("\nPress [ENTER] to continue.")
