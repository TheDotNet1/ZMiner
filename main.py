from colorama import Fore, init
import time
import random
import os
import secrets
import requests
import pyfiglet

init(convert=True)

#VARIABILI
title = Fore.CYAN + """


___________.__           ________          __   _______          __         ___    
\__    ___/|  |__   ____ \______ \   _____/  |_ \      \   _____/  |_   /\  \  \   
  |    |   |  |  \_/ __ \ |    |  \ /  _ \   __\/   |   \_/ __ \   __\  \/   \  \  
  |    |   |   Y  \  ___/ |    `   (  <_> )  | /    |    \  ___/|  |    /\    )  ) 
  |____|   |___|  /\___  >_______  /\____/|__| \____|__  /\___  >__|    )/   /  /  
                \/     \/        \/                    \/     \/            /__/  

        GitHub: @TheDotNet1 Telegram: @ImHackerlol


                    """
ethstr = """

__________  _____  .__                       _________________________ ___  
\____    / /     \ |__| ____   ___________   \_   _____/\__    ___/   |   \ 
  /     / /  \ /  \|  |/    \_/ __ \_  __ \   |    __)_   |    | /    ~    \
 /     /_/    Y    \  |   |  \  ___/|  | \/   |        \  |    | \    Y    /
/_______ \____|__  /__|___|  /\___  >__|     /_______  /  |____|  \___|_  / 
        \/       \/        \/     \/                 \/                 \/

		 """

btcstr = """

__________  _____  .__                       ______________________________  
\____    / /     \ |__| ____   ___________   \______   \__    ___/\_   ___ \ 
  /     / /  \ /  \|  |/    \_/ __ \_  __ \   |    |  _/ |    |   /    \  \/ 
 /     /_/    Y    \  |   |  \  ___/|  | \/   |    |   \ |    |   \     \____
/_______ \____|__  /__|___|  /\___  >__|      |______  / |____|    \______  /
        \/       \/        \/     \/                 \/                   \/

		 """

mainbnr = """

__________  _____  .__                     
\____    / /     \ |__| ____   ___________ 
  /     / /  \ /  \|  |/    \_/ __ \_  __ \
 /     /_/    Y    \  |   |  \  ___/|  | \/
/_______ \____|__  /__|___|  /\___  >__|   
        \/       \/        \/     \/

		  """

licenseKey = input("license Key: ")
licenseList = ["admin", "rv2jdli99X", "P023cvB"]
randomETH = random.randrange(0, 5)
randomETHstr = str(randomETH)
randomETH1 = random.randrange(0000, 9432)
randomETH1str = str(randomETH1)
randomBTC = random.randrange(0, 2)
randomBTCstr = str(randomBTC)
randomBTC1 = random.randrange(0000, 9432)
randomBTC1str = str(randomBTC1)

#CHECKER LICENZA

if licenseKey in licenseList:
	print(Fore.GREEN + "Key is valid!")
	print(mainbnr)

else:
	print(Fore.RED + "Key not valid...")
	print("exit...")
	time.sleep(2)
	print("byeee...")
	time.sleep(1)
	exit()

crypto = input("What crypto you want mine? ETH/BTC: ")

#MINING ETH

def ETH():
	print(title)
	print(ethstr)
	print(Fore.RED + "ENTER A VALID WALLET. IF THE WALLET IS INVALID ALL WALLET YOU HIT WILL BE LOST!")

	with open("btc.txt", "r") as btcWallettxt:
		btcwallet = btcWallettxt.read()
		print(f"Your btc wallet is: {btcwallet}")

	time.sleep(1)
	print(Fore.GREEN + "Mining start! Good Luck!")

	time.sleep(3)
	for i in range(200000000, 200000000000):

		print(" | " + Fore.RED + " CHECK | 0x" + secrets.token_hex(nbytes=24) + " | " + Fore.BLUE + " 0.0000 ETH")

	print("VALID WALLET FOUND!")

	if randomETHstr == 0.5:
		print(Fore.GREEN + " VALID | 0x" + secrets.token_hex(nbytes=24) + Fore.BLUE + " | " + randomETHstr + "." + randomETH1str + " ETH")

	time.sleep(1)
	print(Fore.GREEN + " VALID | 0x" + secrets.token_hex(nbytes=24) + Fore.BLUE + " | " + randomETHstr + "." + randomETH1str + " ETH")

	time.sleep(1)
	print(Fore.BLUE + "Withdrawing... Can take 3-5 day to complete the transaction.")

	time.sleep(0.5)
	print(Fore.BLUE + "ETH Send to your main wallet! Exit...")

	time.sleep(2)
	exit()

#MINING BTC

def BTC():
	print(title)
	print(btcstr)
	print(Fore.RED + "ENTER A VALID WALLET. IF THE WALLET IS INVALID ALL WALLET YOU HIT WILL BE LOST!")

	with open("btc.txt", "r") as btcWallettxt:
		btcwallet = btcWallettxt.read()
		print(f"Your btc wallet is: {btcwallet}")

	time.sleep(1)
	print(Fore.GREEN + "Mining start! Good Luck!")
#200000000, 200000000000
	time.sleep(3)

	for i in range(200, 20000):

		print(Fore.RED + " CHECK | 1" + secrets.token_hex(nbytes=16) + " | " + Fore.BLUE + " 0.0000 BTC")
		print(Fore.RED + " CHECK | bc1" + secrets.token_hex(nbytes=16) + " | " + Fore.BLUE + " 0.0000 BTC")

	print("VALID WALLET FOUND!")
	if randomETHstr == 0.5:

		print(Fore.GREEN + " VALID | 1" + secrets.token_hex(nbytes=16) + Fore.BLUE + " | " + randomETHstr + "." + randomETH1str + " BTC")

	time.sleep(1)
	print(Fore.GREEN + " VALID | 1" + secrets.token_hex(nbytes=16) + Fore.BLUE + " | " + randomETHstr + "." + randomETH1str + " BTC")

	time.sleep(1)
	print(Fore.BLUE + "Withdrawing... Can take 3-5 day to complete the transaction.")

	time.sleep(0.5)
	print(Fore.BLUE + "BTC Send to your main wallet! Exit...")

	time.sleep(2)
	exit()

if crypto == "eth" or crypto == "ETH":
	ETH()
elif crypto == "btc" or crypto == "BTC":
	BTC()
