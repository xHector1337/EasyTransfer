import socket
import os

if os.geteuid() != 0:
    print("Run it as root!")
    exit(1)

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

port = int(input("Enter the port to listen on:\n"))
ip = str(input("Enter the IP address to listen on:\n"))
key = "SKYFM"
directory = "/var/www/html/"
os.chdir(directory)

try:
    sock.bind((ip, port))
except Exception as e:
    print(f"Error binding socket: {e}")
    exit(1)

sock.listen()
print(f"Listening on {ip}:{port}")

while True:
    try:
        conn, addr = sock.accept()
        print("Got connection from", addr)
        passkey = conn.recv(1024).decode('utf-8')
        if passkey == key:
            filename = conn.recv(1024).decode('utf-8')
            with open(filename, "wb") as f:
                while 1:
                    data = conn.recv(1024)
                    if b"DONE" in data or data == "DONE":
                        f.write(data.decode('utf-8').replace("DONE","").encode())
                        conn.close()
                        break
        else:
            print(f"{addr} has entered the wrong key!")
            conn.send("Wrong passkey!".encode())
            conn.close()
    except Exception as e:
        print(f"An error occurred: {e}")
