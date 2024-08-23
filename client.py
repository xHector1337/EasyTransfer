import socket

port = int(input("Enter port:\n"))
ip = str(input("Enter ip:\n"))
passkey = "SKYFM"
sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

try:
    sock.connect((ip,port))
    print(f"Connected to {ip}:{port}")
    sock.send(passkey.encode())
    sock.recv(1024)
    filename = str(input(""))
    sock.send(filename.encode())
    with open(filename,"rb") as f:
        data = f.read(1024)
        while data:
            sock.send(data)
            data = f.read(1024)
    sock.send(b'')
    print("File sent.")        
    response = sock.recv(1024)
    print(f"Recieved {response.decode('utf-8')}")
except Exception as e:
    print(e)
sock.close()        
