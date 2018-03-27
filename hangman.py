import string
import random
#from array import *
import socket 
wordlist = ['peaches','apple']
class hangman():
    
    def setup(self,diffuculty,uname):
        self.incorrect = []
        self.correct = []
        self.points = [0]
        self.currstr =[]
        self.currplayers = []
        self.current_puzzle = random.choice(wordlist) #random word
        self.gameover = False
        self.playerturn = ''
        self.playercount = 0
        self.swapturns = False
        if diffuculty == '1':
            self.max_guess = len(self.current_puzzle) * 3
        elif diffuculty == '2':
            self.max_guess = len(self.current_puzzle) * 2
        elif diffuculty =='3':
            self.max_guess = len(self.current_puzzle)
        reply = 'setup success\n'
        for letter in self.current_puzzle:
            self.currstr.append('_')
        self.currplayers.append(uname)
        self.playerturn = uname
        return reply
    def join(self,uname):
        self.currplayers.append(uname)
        self.points.append(0)
        
    def guess_letter(self,guess,uname):
        if self.turncheck(uname) == True:
            self.swapturns = True
            if guess in self.current_puzzle:
                self.correct.append(guess)
                pts = 0
                self.swapturns = False
                for x in self.current_puzzle:
                    if x == guess:
                        pts = pts + 1;
                for x in range(len(self.currplayers)):
                    if self.currplayers[x] == uname:
                        self.points[x] = self.points[x] + pts
            else:
                self.incorrect.append(guess)
        else:
            self.swapturns = False
    def guess_word(self,guess,uname):
        if guess == self.current_puzzle:
            self.gameover = True
            pts = len(self.current_puzzle)
            for x in range(len(self.currplayers)):
                if self.currplayers[x] == uname:
                    self.points[x] = self.points[x] + pts
            return True
        else:
            self.currplayers.remove(uname)
            return False
            
    def alreadyguessed(self, guess):
        if guess in self.correct or guess in self.incorrect:
            return True
        else:
            return False
    def update(self):
        for x in self.correct:
            for i in range(len(self.current_puzzle)):
                if self.current_puzzle[i] == x:
                    self.currstr[i] = x
        if self.currplayers[self.playercount] == self.playerturn and self.swapturns == True:
            self.playercount =self.playercount + 1
            self.swapturns = False
            print self.playercount
            if self.playercount > len(self.currplayers) - 1:
                self.playercount = 0
                self.playerturn= self.currplayers[self.playercount]
                print self.playerturn
            else:
                self.playerturn = self.currplayers[self.playercount]
                print self.playerturn
        
    def display(self):
        reply = ''
        for x in self.currstr:
            reply = reply + x
        reply = reply + '\n'
        for x in self.incorrect:
            reply = reply + x
        reply = reply + '\n'
        #for i in range(self.length):
            #reply = reply + self.currplayers[i] + ' ' + self.points[i] +'\n'
        return reply
        
    def dispts(self):
        #try if selfcurrplay == uname then add *
        reply = ''
        for x in range(len(self.currplayers)):
            reply = reply + self.currplayers[x] + ' ' + str(self.points[x])
            if self.currplayers[x] == self.playerturn:
                reply = reply + '*'
            reply = reply + '\n'
        return reply
    def status(self):
        if all(x in self.correct for x in self.current_puzzle):
            self.gameover = True
        elif len(self.incorrect) > self.max_guess:
            self.gameover = True
        if self.gameover == True:
            return True
        else:
            return False
    def turncheck(self,uname):
        if uname == self.playerturn:
            return True
        else:
            return False
    def returnword(self):
        reply = self.current_puzzle + '\n'
        return reply
    def test(self):
        reply = ''
        
        reply = '\n'
        return reply