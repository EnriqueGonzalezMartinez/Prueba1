import os
import time

def cambio(cadena,indice,carac):
    nueva = ''
    for c in range(len(cadena)):
        if c == indice:
            nueva += carac
        else:
            nueva += cadena[c]
    return nueva

def cinta(cadena,cinta):
    global flag
    for carac in cadena:
        print(f'[{carac}]', end='')
        if flag == True:
            for carac in cadena:
                if carac != ' ' and flag == True:
                    flag = [cadena.find(carac), cadena.find(carac)]

    print('')
    apuntador = (' '*3)*flag[cinta] +' ↑' 
    print(apuntador)


def machine(estado1,sim1,sim2,estado2,sim11,sim12,mov,mov2):
    global estado
    global cinta1
    global cinta2
    global cont
    os.system('cls')
    if (estado == estado1 and cinta1[flag[0]] == sim1 and cinta2[flag[1]] == sim2):
        estado = estado2
        cinta1 = cambio(cinta1, flag[0], sim11)
        cinta2 = cambio(cinta2, flag[1], sim12)
        flag[0] += mov
        flag[1] += mov2
        cinta(cinta1,0)
        cinta(cinta2,1)
        time.sleep(1)
        cont = True
    else:
        cont = False


cinta1 = input('Ingrese la cadena: ')
bs = ' ' * (cinta1.count('b') + 1)
cinta1 = bs + cinta1 + bs
cinta2 = ' ' * len(cinta1)
flag = True
estado = 'q0'
cont = False
print(f'Estado: {estado}')
cinta(cinta1,0)
cinta(cinta2,1)
time.sleep(1)

while(estado != 'q5'):
        machine('q0','a',' ','q1','a','a',1,1)
        if cont == True:
            continue
        machine('q1','a',' ','q1','a','a',1,1)
        if cont == True:
            continue
        machine('q1','b',' ','q2','b',' ',0,-1)
        if cont == True:
            continue
        machine('q2','b','a','q2','b','b',1,-1)
        if cont == True:
            continue
        machine('q2','b',' ','q3','b','b',1,-1)
        if cont == True:
            continue
        machine('q2','c','a','q3','c',' ',0,0)
        if cont == True:
            continue
        machine('q3','b',' ','q3','b','b',1,-1)
        if cont == True:
            continue
        machine('q3','c',' ','q4','c',' ',0,1)
        if cont == True:
            continue
        machine('q4','c','b','q4','c','b',1,1)
        if cont == True:
            continue
        machine('q4','c',' ','q5','c',' ',1,1)
        if cont == True:
            continue
        machine('q4',' ','b','q5',' ','b',0,0)
        if cont == True:
            continue
        machine('q4',' ',' ','q5',' ',' ',0,0)
        if cont == True:
            continue
        print('No se acepta la cadena.')
        exit()

print('Cadena aceptada.')
