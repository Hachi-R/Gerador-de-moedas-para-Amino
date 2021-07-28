import amino
import random
import string
import base64
from hashlib import sha1

	#coingenerator functions

def deviceIdgenerator(st : int = 69):
	ran = ''.join(random.choices(string.ascii_uppercase + string.digits, k = st))
	thedevice = '01' + (MetaSpecial := sha1(ran.encode("utf-8"))).hexdigest() + sha1(bytes.fromhex('01') + MetaSpecial.digest() + base64.b64decode("6a8tf0Meh6T4x7b0XvwEt+Xw6k8=")).hexdigest()
	return thedevice

def login(client : amino.Client, email : str, password : str):
	try:
		client.login(email=email, password=password)
		print(f" Logado em: {email}\n")
		print("")
	except amino.lib.util.exceptions.YouAreBanned:
		print(f" Essa conta \"{email}\" foi banida. ")
		return
	except amino.lib.util.exceptions.VerificationRequired as e:
		print(f" Verificação necessaria para o e-mail: {email}")
		print(" Abra o link a seguir, e digite o código exibido no terminal!")
		print("")
		link = e.args[0]['url']
		print( link)
		print("")
		input(" # Digite o código de verificação aqui: >> ")
		print("")
		login(client, email, password)
	except amino.lib.util.exceptions.InvalidPassword:
		print(f" Senha incorreta: {email}")
		passx = input(" # Senha: >> ")
		login(client, email, passx)
	except amino.lib.util.exceptions.InvalidAccountOrPassword:
		print(f" senha incorreta: {email}")
		passx = input(" # Senha: >> ")
		login(client, email, passx)
	except:
		return
        
        
	#coingenerator functions