import socket

port = int(input("Enter port:\n"))
ip = str(input("Enter ip:\n"))
passkey = "SKYFM"
message = "Hello man!"
sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

try:
    sock.connect((ip,port))
    print(f"Connected to {ip}:{port}")
    sock.send(passkey.encode())
    sock.send(message.encode())
    response = sock.recv(1024)
    print(f"Recieved {response.decode('utf-8')}")
except Exception as e:
    print(e)
sock.close()        
