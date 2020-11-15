import nmap
import re
import os

exp_ip = re.compile(r'192.168.100.\d(\d)?')
exp_port = re.compile(r';\d\d;')
exp_state = re.compile(r'open')
sc = nmap.PortScanner()
print('Scanning...')
res = sc.scan('192.168.100.0/24', '7-500')
csv = sc.csv()
with open("test.txt","w") as file:
	file.write(csv)
with open("test.txt","r") as file:
	for line in file:
		ser1 = exp_ip.search(line)
		ser2 = exp_port.search(line)
		ser3 = exp_state.search(line)
		try:
			with open("scan.csv","a") as file:
				file.write(f'{ser1.group()} : {ser2.group()[1:3]} {ser3.group()}\n')
		except:
			None

print('File created')
os.remove('test.txt')
