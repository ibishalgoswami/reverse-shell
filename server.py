import socket
s=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
ip=''
s.connect((socket.gethostname(),9879))
con=True
while con:
    msg=input('Enter your message')
    msg=bytes(msg,'utf-8')
    s.send(msg)
    msg=s.recv(1024).decode()
    print("Target Machine=>",msg)