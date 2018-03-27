import socket
import sys
import random 
import time
#import datetime
from thread import *
from hangman import *
#from hangman import hangman


HOST = ''   # Symbolic name meaning all available interfaces
PORT = 2305 # Arbitrary non-privileged port
 
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
print 'Socket created'
 
#Bind socket to local host and port
try:
    s.bind((HOST, PORT))
except socket.error , msg:
    print 'Bind failed. Error Code : ' + str(msg[0]) + ' Message ' + msg[1]
    sys.exit()
     
print 'Socket bind complete'
 
#Start listening on socket
s.listen(10)
print 'Socket now listening'

class User(object):
    def __init__(self,uname):
        self.uname=uname
       
userList = dict()
userList['klynn']=User('klynn')
users= {
    'klynn':'123',
    'test':'123'
}
curusers = dict()
curgames = dict()
hof = dict()
def menuPrompt(conn):
    prompt="""1. Login
2. Make New User
3. Hall of Fame
4. Exit\n"""
    conn.sendall(prompt)
def login(conn):
    invalidLogin=1
    while(invalidLogin):
        conn.send('Please enter your username and hit enter\n') #send only takes string
        uname=conn.recv(1024)
        uname=uname.rstrip('\r\n')
        #print 'Username: ' + uname
        conn.sendall('Please enter your password and hit enter\n')
        pwd=conn.recv(1024)
        pwd=pwd.rstrip('\r\n')
        #print 'Password: ' + pwd
        if uname in users and users[uname]==pwd:
            invalidLogin=0
            curusers[uname]=conn
            prompt="""1. Start New Game
2. Get List of Games
3. Hall of Fame
4. Exit\n"""
            conn.sendall(prompt)
            return uname
        else:
            conn.send('Invalid Username/Password Combination\n')

def clientthread(conn):
    menuPrompt(conn)
    msg = conn.recv(1024)
    msg = msg.rstrip('\r\n')
    while (msg != '4'):
        if(msg =='1'):
            uname = login(conn)
            msg = conn.recv(1024)
            msg = msg.rstrip('\r\n')
            while(msg != '4'):
                prompt="""1. Start New Game
2. Get List of Games
3. Hall of Fame
4. Exit\n"""
                #conn.sendall(prompt)
                #msg = conn.recv(1024)
                #msg = msg.rstrip('\r\n')
                if (msg == '1'):
                    prompt2 = """choose diffuculty:
1. Easy
2. Medium
3. Hard\n"""
                    conn.sendall(prompt2)
                    msg = conn.recv(1024)
                    msg = msg.rstrip('\r\n')
                    if(msg == '1'):
                        game = hangman()
                        curgames[game] = 'game by ' + uname
                        reply = game.setup(msg,uname)
                        conn.sendall(reply)
                        reply = game.display()
                        conn.sendall(reply)
                        reply = game.dispts()
                        conn.sendall(reply)
                        #reply = game.test()
                        #conn.sendall(reply)
                        gameover = False
                        while not (gameover):
                            conn.sendall('enter guess:\n')
                            msg = conn.recv(1024).lower()
                            if msg.isalpha():
                                if len(msg) > 1:
                                    check = game.guess_word(msg,uname)
                                    gameover = game.status()
                                    if not(gameover):
                                        lose = True
                                        break
                                    game.update()
                                    reply = game.display()
                                    conn.sendall(reply)
                                    reply = game.dispts()
                                    conn.sendall(reply)
                                    if(gameover):
                                        lose = False
                                        break
                                else:
                                    guessed = game.alreadyguessed(msg)
                                    if guessed:
                                        conn.sendall('alreadyguessed\n')
                                    else:
                                        game.guess_letter(msg,uname)
                                        gameover = game.status()
                                        game.update()
                                        reply = game.display()
                                        conn.sendall(reply)
                                        reply = game.dispts()
                                        conn.sendall(reply)
                                        
                            else:
                                conn.sendall('invaild\n')
                        if lose:
                            conn.sendall(prompt)
                            msg = conn.recv(1024)
                        else:
                            reply = 'word was ' + game.returnword()
                            conn.sendall(reply)
                            curgames.pop(game,None)
                            conn.sendall(prompt)
                            msg = conn.recv(1024)
                    elif(msg == '2'):
                        game = hangman()
                        curgames[game] = 'game by ' + uname
                        reply = game.setup(msg,uname)
                        conn.sendall(reply)
                        reply = game.display()
                        conn.sendall(reply)
                        reply = game.dispts()
                        conn.sendall(reply)
                        #reply = game.test()
                        #conn.sendall(reply)
                        gameover = False
                        while not (gameover):
                            conn.sendall('enter guess:\n')
                            msg = conn.recv(1024).lower()
                            if msg.isalpha():
                                if len(msg) > 1:
                                    check = game.guess_word(msg,uname)
                                    gameover = game.status()
                                    if not(gameover):
                                        lose = True
                                        break
                                    game.update()
                                    reply = game.display()
                                    conn.sendall(reply)
                                    reply = game.dispts()
                                    conn.sendall(reply)
                                    if(gameover):
                                        lose = False
                                        break
                                else:
                                    guessed = game.alreadyguessed(msg)
                                    if guessed:
                                        conn.sendall('alreadyguessed\n')
                                    else:
                                        game.guess_letter(msg,uname)
                                        gameover = game.status()
                                        game.update()
                                        reply = game.display()
                                        conn.sendall(reply)
                                        reply = game.dispts()
                                        conn.sendall(reply)
                                        
                            else:
                                conn.sendall('invalid\n')
                        if lose:
                            conn.sendall(prompt)
                            msg = conn.recv(1024)
                        else:
                            reply = 'word was ' + game.returnword()
                            conn.sendall(reply)
                            curgames.pop(game,None)
                            conn.sendall(prompt)
                            msg = conn.recv(1024)
                    elif(msg == '3'):
                        game = hangman()
                        curgames[game] = 'game by ' + uname
                        reply = game.setup(msg,uname)
                        conn.sendall(reply)
                        reply = game.display()
                        conn.sendall(reply)
                        reply = game.dispts()
                        conn.sendall(reply)
                        #reply = game.test()
                        #conn.sendall(reply)
                        gameover = False
                        while not (gameover):
                            conn.sendall('enter guess:')
                            msg = conn.recv(1024).lower()
                            if msg.isalpha():
                                if len(msg) > 1:
                                    check = game.guess_word(msg,uname)
                                    gameover = game.status()
                                    if not(gameover):
                                        lose = True
                                        break
                                    game.update()
                                    reply = game.display()
                                    conn.sendall(reply)
                                    reply = game.dispts()
                                    conn.sendall(reply)
                                    if(gameover):
                                        lose = False
                                        break
                                else:
                                    guessed = game.alreadyguessed(msg)
                                    if guessed:
                                        conn.sendall('alreadyguessed\n')
                                    else:
                                        game.guess_letter(msg,uname)
                                        gameover = game.status()
                                        game.update()
                                        reply = game.display()
                                        conn.sendall(reply)
                                        reply = game.dispts()
                                        conn.sendall(reply)
                                        
                            else:
                                conn.sendall('invalid\n')
                        if lose:
                            conn.sendall(prompt)
                            msg = conn.recv(1024)
                        else:
                            reply = 'word was ' + game.returnword()
                            conn.sendall(reply)
                            curgames.pop(game,None)
                            conn.sendall(prompt)
                            msg = conn.recv(1024)
                    else:
                        conn.sendall(prompt2)
                        msg = conn.recv(1024)
                        msg = msg.rstrip('\r\n')
                    
                    
                elif(msg == '2'):
                    reply = ''
                    i = 1
                    for keys,values in curgames.items():
                        reply = str(i) + '. ' + str(values)
                        i = i + 1
                    conn.sendall(reply)
                    conn.sendall('\n choose one to join / q to quit')
                    msg = conn.recv(1024)
                    msg = msg.rstrip('\r\n')
                    if(msg == 'q'):
                        conn.sendall(prompt)
                        msg = conn.recv(1024)
                        msg = msg.rstrip('\r\n')
                    else:
                        num = int(msg) - 1
                        game = curgames.keys()[num]
                        game.join(uname)
                        reply = game.display()
                        conn.sendall(reply)
                        reply = game.dispts()
                        conn.sendall(reply)
                        gameover = False
                        while not(gameover):
                            conn.sendall('enter guess:')
                            msg = conn.recv(1024).lower()
                            if msg.isalpha():
                                if len(msg) > 1:
                                    check = game.guess_word(msg,uname)
                                    gameover = game.status()
                                    if not(gameover):
                                        lose = True
                                        break
                                    game.update()
                                    reply = game.display()
                                    conn.sendall(reply)
                                    reply = game.dispts()
                                    conn.sendall(reply)
                                    if(gameover):
                                        lose = False
                                        break
                                else:
                                    guessed = game.alreadyguessed(msg)
                                    if guessed:
                                        conn.sendall('alreadyguessed\n')
                                    else:
                                        game.guess_letter(msg,uname)
                                        gameover = game.status()
                                        game.update()
                                        reply = game.display()
                                        conn.sendall(reply)
                                        reply = game.dispts()
                                        conn.sendall(reply)
                                        
                            else:
                                conn.sendall('invalid\n')
                        if lose:
                            conn.sendall(prompt)
                            msg = conn.recv(1024)
                        else:
                            reply = 'word was ' + game.returnword()
                            conn.sendall(reply)
                            curgames.pop(game,None)
                            conn.sendall(prompt)
                            msg = conn.recv(1024)
                    
                elif(msg == '3'):
                    conn.sendall('wip\n')
                    msg = conn.recv(1024)
                    msg = msg.rstrip('\r\n')
                else:
                    conn.sendall(prompt)
                    msg = conn.recv(1024)
                    msg = msg.rstrip('\r\n')
        elif(msg == '2'):
            
            conn.sendall('What is your username\n')
            uname = conn.recv(1024)
            #print uname
            if uname in users:
                invalidname = 1
                
                while(invalidname):
                    conn.sendall('What is your username\n')
                    uname = conn.recv(1024)
                   # uname = msg.rstrip('\r\n')
                    if uname in users:
                        invalidname = 1
                    else:
                        invalidname = 0
            conn.sendall('What is your password\n')
            #print uname
            pwd = conn.recv(1024)
            pwd = pwd.rstrip('\r\n')
            #print pwd
            #print uname + '\n'
            users.update({uname:pwd})
            #for keys,values in users.items():
                #print(keys)
                #print(values)
            menuPrompt(conn)
            msg = conn.recv(1024)
            msg = msg.rstrip('\r\n')
        elif(msg == '3'):
            conn.sendall('wip\n')
            msg = conn.recv(1024)
            msg = msg.rstrip('\r\n')
        else:
            menuPrompt(conn)
            msg = conn.recv(1024)
            msg = msg.rstrip('\r\n')
    conn.sendall('goodbye\n')
    conn.close()
def serverthread():
    while 1:
        print """1. Current list of users
2. Current list of words
3. Add new word to list\n"""
        act =raw_input()
        if act == '1':
            for i in curusers:
                print i 
        elif act == '2':
            for i in wordlist:
                print i
        elif act == '3':
            print 'what is your word'
            nwd = raw_input()
            wordlist.append(nwd)
            print 'word added'
        #elif act == '4':
            #asdf = curgames.keys()[0]
            #print asdf
start_new_thread(serverthread,())
while 1:
    #wait to accept a connection - blocking call
    conn, addr = s.accept()
    print 'Connected with ' + addr[0] + ':' + str(addr[1])
     
    #start new thread takes 1st argument as a function name to be run, second is the tuple of arguments to the function.
    start_new_thread(clientthread ,(conn,))
 
s.close()