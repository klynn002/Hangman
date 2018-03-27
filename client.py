import getpass 
import socket   #for sockets
import sys  #for exit
import time
 
#create an INET, STREAMing socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
print 'Socket Created'
#change IP to servers when you run topology
#localhost for testing without running topology
host = 'localhost';
port = 2305;

askpass = "What is your password\n"
askpass2 = "Please enter your password and hit enter\n"
#Connect to remote server
s.connect((host , port))
print 'Socket Connected to ' + host

while 1:
    reply = s.recv(4096)
    print reply
    if(reply == askpass or reply == askpass2):
        pwd = getpass.getpass()
        s.sendall(pwd)
    elif(reply == "goodbye\n"):
        sys.exit()
    else:
        msg =raw_input()
        s.sendall(msg)
        time.sleep(.3)