import nmap

sc = nmap.PortScanner()
print('Scanning...')
for i in range(25):
    ip = '192.168.100.'+ str(i)
    for j in range(75, 81):
        res = sc.scan(ip, str(j))
        try: 
            res = res['scan'][ip]['tcp'][j]['state']
            if res == 'open' :
                with open('scan1.csv','a') as file:
                    file.write(f'{ip} : {j} open\n')
        except:
            None
print('File created')