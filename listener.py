import socket

sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

port = int(input("Enter the port to be listened:\n"))
ip = str(input("Enter the ip address to be listened:\n"))
key = "SKYFM"
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
        if passkey.decode('utf-8') == "SKYFM":
            message = conn.recv(1024)
            print(f"Recieved {message.decode('utf-8')}")
            conn.send("Hello".encode())
            conn.close()
        else:
            print(f"{addr} has entered wrong key!")
            conn.send("Wrong passkey!".encode())
            conn.close()    
    except Exception as e:
        print(e)            
