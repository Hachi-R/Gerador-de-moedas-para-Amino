import amino
import json
import time
from os import path
from coingeneratorconfig import coingeneratorfunctions
from concurrent.futures import ThreadPoolExecutor
from colorama import init, Fore, Back, Style
init()

print(Fore.MAGENTA + Style.NORMAL)

print(""" SCRIPT POR: HACHI.

 OTANIX/AMINO: http://aminoapps.com/p/u9irwn 
 Chama lá, em caso de dúvidas e outras coizinhas!""")

print("""""")
print(""" COMO USAR: GITHUB.COM/REPO""")
print("""""")
print("""""")
print(" ------------------------------------------------------")
print("""""")
print("""""")

print(""" GERADOR DE MOEDAS AUTOMÁTICO VINICCIUS 13!
 CRIADO PELO HACHI PARA OS POBRES DO AMINO.""")

print("""""")

THIS_FOLDER = path.dirname(path.abspath(__file__))
emails = path.join(THIS_FOLDER, 'emails.txt')
deviceIdfile = path.join(THIS_FOLDER, "device")
emails = open(emails, "r")
print(""" (01): GERADOR DE MOEDAS.
 (02): TRANSFERIDOR DE MOEDAS.""")

print("""""")
print("""""")
theselect = input(" # Escolha uma opção: >> ")
print("""""")	

def coinsgenerator(sub_client : amino.SubClient):
	generatingcoins = {"start": int(time.time()), "end": int(time.time()) +300}
	return generatingcoins

def sendingprocces(sub_client : amino.SubClient):
	thetimer = [coinsgenerator(sub_client) for _ in range(50)]
	sub_client.send_active_obj(timers=thetimer)
	print(f" Gerando moedas em: {email}")

def coinsgeneratingproccess(client: amino.Client, email : str, password : str, comid: str):
	try:
		sendingprocces(sub_client)
	except:
		return

def lottery():
	try:
		sub_client.lottery()
		print(f" Executando script em: {email}")
		print("")
	except amino.lib.util.exceptions.AlreadyPlayedLottery:
		print("")
		print(f" Executando script em: {email}")
		print("")
		return

#coins transfer functions
def coinstransfer():
    client = amino.Client()
    password = input(" # Digite a senha das contas: >> ")
    
    print("")
    
    thebloglink = input(" # Blog de recebimento: >> ")
    
    print("")
    
    theblog = client.get_from_code(thebloglink)
    blogid = client.get_from_code(str(thebloglink.split('/')[-1])).objectId
    thecommunityid = theblog.path[1:theblog.path.index('/')]
    for line in emails:
    	email = line.strip()
    	coingeneratorfunctions.login(client = client, email = email, password = password)
    	sub_client = amino.SubClient(comId=thecommunityid, profile=client.profile)
    	try:
    	   	coins = int(client.get_wallet_info().totalCoins)
    	   	print(f" Este e-mail: \"{email}\" possui {coins} moedas!")		   
    	   	if coins != 0:
    	   	   sub_client.send_coins(coins=coins, blogId=blogid)
    	   	   print(f" As moedas desta conta: \"{email}\" foram transferidas! {coins} moedas!")
    	except amino.lib.util.exceptions.NotEnoughCoins:
    	   	print(f" Essa conta: \"{email}\" não possui moedas :(")
    	   	return
    	except amino.lib.util.exceptions.InvalidRequest:
    	   	print(" Pedido invalido.")
    	   	return
    	except amino.lib.util.exceptions.YouAreBanned:
    	   	print(f" Essa conta: \"{email}\" foi banida.")
    	   	return
    	except amino.lib.util.exceptions.InvalidSession:
    	   	print(f" {email} Invalid Session.")
    	   	return
    	except:
    		return

if theselect == "1":
    client = amino.Client()
    password = input(" # Digite a senha das contas: >> ")
    
    print("")
    
    communitylink = input(" # Link da comunidade de farm: >> ")
    
    print("")
    
    communityinfo = client.get_from_code(communitylink)
    communityid = communityinfo.path[1:communityinfo.path.index('/')]

    for line in emails:
        email = line.strip()
        device = coingeneratorfunctions.deviceIdgenerator()
        thedevicejs = {
        "device_id": f"{device}",
        "device_id_sig": "Aa0ZDPOEgjt1EhyVYyZ5FgSZSqJt",
        "user_agent": "Dalvik/2.1.0 (Linux; U; Android 5.1.1; SM-G973N Build/beyond1qlteue-user 5; com.narvii.amino.master/3.4.33562)"
        }
        deviceIdfile = open('device.json', "w")
        json.dump(thedevicejs, deviceIdfile)
        deviceIdfile.close()
        coingeneratorfunctions.login(client = client, email = email, password = password)
        sub_client = amino.SubClient(comId=communityid, profile = client.profile)
        lottery()
        for i in range(20):
            with ThreadPoolExecutor(max_workers=150) as executor:
                 _ = [executor.submit(coinsgeneratingproccess, client, email, password, communityid)]

elif theselect == "2":
	coinstransfer()