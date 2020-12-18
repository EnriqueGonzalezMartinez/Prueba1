import subprocess
import os

def hashValuer(path,file):
    cwd = os.getcwd().replace('\\','/')
    if (cwd != path):
        if file == None:
            command = f'powershell -ExecutionPolicy ByPass -File Hash_values.ps1 -path "{path}"'
            subprocess.run(command)
        else:
            command = f'powershell -ExecutionPolicy ByPass -File Hash_values.ps1 -path "{path}" -file {file}'
            subprocess.run(command)
    else:
        print('No es posible obtener el hash del mismo directorio desde el que se ejecuta el script.')
