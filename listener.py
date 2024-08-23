import socket
import os

sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

port = int(input("Enter the port to be listened:\n"))
ip = str(input("Enter the ip address to be listened:\n"))
key = "SKYFM"
directory = "/var/www/html/"
os.chdir(directory)
try: 
    sock.bind((ip,port))
except Exception as e:
    print(e)
    exit(1)
sock.listen()
print(f"Listening on {ip}:{port}")
while 1:
    try:
        conn, addr = sock.accept()
        print("Got connection from",addr)
        passkey = conn.recv(1024)
        if passkey.decode('utf-8') == key:
            conn.send("Welcome back! Please enter new file name:".encode())
            filename = conn.recv(1024)
            with open(filename.decode('utf-8'),"wb") as f:
                while 1:
                    data = conn.recv(1024)
                    if not data:
                        break
                    f.write(data)
                f.close()
            conn.send("Your file has been transfered!".encode())            
            conn.close()
        else:
            print(f"{addr} has entered wrong key!")
            conn.send("Wrong passkey!".encode())
            conn.close()    
    except Exception as e:
        print(e)            
