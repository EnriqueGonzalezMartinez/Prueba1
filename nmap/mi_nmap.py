# Enrique Adrian Gonzalez Martinez
# Este script hace un tipo de escaneo de ip dependiendo de la opcion elegida
# 2020/11/28 2:47 p.m.
import nmap

def scanNmap(ip,rango,scan):
  escaner.scan(ip,rango,f'-v {scan}')
  print(escaner.command_line())
  print(f'hostname: {escaner[ip].hostname()}')
  print(f'state: {escaner[ip].state()}')
  protocols = escaner[ip].all_protocols()
  print(f'protocols: {protocols}')
  for x in protocols:
    keys = escaner[ip][x].keys()
    print(f'keys: {keys}')
    for key in keys:
      if (x == 'tcp'):
        print(f'port {key} open: {escaner[ip].has_tcp(key)}')
      elif (x == 'udp'):
        print(f'port {key} open: {escaner[ip].has_udp(key)}')
      elif (x == 'sctp'):
        print(f'port {key} open: {escaner[ip].has_sctp(key)}')
      elif (x == 'ip'):
        print(f'port {key} open: {escaner[ip].has_ip(key)}')
      else:
        pass

print("[1] escaneo TCP SYN\n[2] escaneo por Conexion\n[3] escaneo ACK\n[4] escaneo Window")
print("[5] escaneo Maimon\n[6] escaneo UDP\n[7] escaneo FIN\n[8] escaneo Xmas")
print("[9] escaneo SCTP INIT\n[10] escaneo COOKIE-ECHO")
escaner = nmap.PortScanner()
opc = input('Ingrese la opcion de escaneo: ')
ip = input('Ingrese la ip: ')
rango = input('Ingrese el rango: ')
escan = ['','-sS','sT','-sA','-sW','-sM','-sS','-sF','-sX','-sY','-sZ']
try:
  scanNmap(ip,rango,escan[opc])
except:
  print('El rango, la ip es incorrecto o la opcion son incorrectos.')
