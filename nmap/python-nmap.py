import nmap

escaner = nmap.PortScanner()
print(escaner.scan('127.0.0.1','1-1024','-v -sV'))
print(escaner.scaninfo())
print(escaner.all_hosts())
print(escaner['127.0.0.1'].hostname())
print(escaner['127.0.0.1'].state())
print(escaner['127.0.0.1'].all_protocols())
print(escaner['127.0.0.1']['tcp'].keys())
print(escaner['127.0.0.1'].has_tcp(135))
print(escaner['127.0.0.1']['tcp'][135])
print(escaner['127.0.0.1']['tcp'][135]['product'])
