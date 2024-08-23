import socket
import os
port = int(input("Enter port:\n"))
ip = str(input("Enter ip:\n"))
passkey = "SKYFM"
sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
mode = str(input("Enter uploading mode:(file or directory)\n"))

def directoryUpload(path):
    try:    
        sock.connect((ip,port))
        sock.send(passkey.encode())
        os.chdir(path)
        for i in os.listdir():
            sock.send(i.encode())
            with open(i,"rb") as f:
                sock.sendfile(f)
            sock.send(b"DONE")
        print("All files are uploaded.")
        exit(0)
    except Exception as e:
        print(e)
        exit(1)    
if mode == "directory":
    path = str(input("Enter path of the directory you want to upload.\n"))
    directoryUpload(path)                         
try:
    sock.connect((ip,port))
    print(f"Connected to {ip}:{port}")
    sock.send(passkey.encode())
    filename = str(input("Enter the filename you want to upload:\n"))
    sock.send(filename.encode())
    with open(filename,"rb") as f:
        sock.sendfile(f)
    sock.send(b'DONE')
    print("File sent.")        
    response = sock.recv(1024)
    print(f"Recieved {response.decode('utf-8')}")
except Exception as e:
    print(e)
sock.close()        
