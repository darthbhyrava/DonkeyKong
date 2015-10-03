
#Test for Fixtures, Exceptions | Create Test_Classes

"""Donkey Kong Terminal Game"""
import os, time
from random import choice, randint


def getchar():
    """Returns a single character from standard input"""
    """Function taken from http://code.activestate.com/recipes/134892/"""
    import tty, termios, sys
    fd = sys.stdin.fileno()
    old_settings = termios.tcgetattr(fd)
    try:
        tty.setraw(sys.stdin.fileno())
        ch = sys.stdin.read(1)
    finally:
        termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
    return ch

class Person:
    """Class for Player and Donkey Inheritance"""
    
    def __init__(self,x,y):
        self.__y = y
        self.__x = x

    def move(self, inp, sc):
        if(sc.old!='C'):
            sc.prplayer(self.__x, self.__y,sc.old)
        else:
            sc.prplayer(self.__x, self.__y,' ')
        if(inp=='a' or inp=='A'):
            if(sc.checkCollision(self.__x,self.__y-1) and (sc.board[self.__x+1][self.__y-1]=="*" or sc.board[self.__x+1][self.__y-1]=="H")):
                sc.old=sc.board[self.__x][self.__y-1]
                self.__y-=1
                self.__ladder_length=0;
        elif(inp=='d' or inp=='D'):
            if(sc.checkCollision(self.__x,self.__y+1) and (sc.board[self.__x+1][self.__y+1]=="*" or sc.board[self.__x+1][self.__y+1]=="H")):
                sc.old=sc.board[self.__x][self.__y+1]
                self.__y+=1
                self.__ladder_length=0;
        elif(inp=='w' or inp=='W'):
            if(sc.old=='H' and (sc.board[self.__x-1][self.__y]=='H' or self.__ladder_length>=3)):
                sc.old=sc.board[self.__x-1][self.__y]
                self.__ladder_length+=1
                self.__x-=1
        elif(inp=='s' or inp=='S'):
            if(sc.board[self.__x+1][self.__y]=='H'):
                sc.old=sc.board[self.__x+1][self.__y]
                self.__ladder_length+=1
                print self.__ladder_length
                self.__x+=1
        sc.prplayer(self.__x,self.__y,'P')

    def ljump(self,sc):
        """Creates a left jump for player"""
        if(sc.checkLjump(self.__x,self.__y)):
            self.timer=4
            while(self.timer!=0):
                os.system("clear")
                screen.prscreen()
                sc.prplayer(self.__x, self.__y, sc.oldj)                
                if(self.timer==4 or self.timer==3):
                    sc.oldj=sc.board[self.__x][self.__y]
                    self.__x=self.__x-1
                    self.__y=self.__y-1
                    sc.prplayer(self.__x,self.__y,'P')
                    time.sleep(0.1)
                    self.timer=self.timer-1
                if(self.timer==2 or self.timer==1):
                    sc.oldj=sc.board[self.__x][self.__y]
                    self.__x=self.__x+1
                    self.__y=self.__y-1
                    sc.prplayer(self.__x,self.__y,'P')
                    time.sleep(0.1)
                    self.timer=self.timer-1
    def rjump(self,sc):
        """Creates a right jump for player"""
        if(sc.checkRjump(self.__x,self.__y)):
            self.timer=4
            while(self.timer!=0):
                sc.prplayer(self.__x, self.__y, sc.oldj)
                if(self.timer==4 or self.timer==3):
                    self.__x=self.__x-1
                    self.__y=self.__y+1
                    sc.oldj=sc.board[self.__x][self.__y]
                    sc.prplayer(self.__x,self.__y,'P')
                    time.sleep(0.5)
                    self.timer=self.timer-1
                if(self.timer==2 or self.timer==1):
                    self.__x=self.__x+1
                    self.__y=self.__y+1
                    sc.oldj=sc.board[self.__x][self.__y]
                    sc.prplayer(self.__x,self.__y,'P')
                    time.sleep(0.5)
                    self.timer=self.timer-1
        

        
    



class Player(Person):
    """Player Class"""
  
    def __init__(self,x,y):
        Person.__init__(self,x,y)

    def move(self,inp,sc):
        Person.move(self, inp, sc)

    def getx(self):
        return (self._Person__x)

    def gety(self):
        return (self._Person__y)
    


class Donkey(Person):
    """Donkey Class"""

    def __init__(self,x,y):
        self.__x = x
        self.__y = y 

    def move(self, sc):
        self.__rd=randint(1,10)
        sc.prplayer(self.__x, self.__y,' ')
        if(self.__rd%2==0):
            if(sc.checkCollision(8,self.__y-1) and (sc.board[self.__x+1][self.__y-1]=="*" or sc.board[self.__x+1][self.__y-1]=="H")):
                self.__y-=1
            else:
                self.__y+=1
        else:
            if(sc.checkCollision(8,self.__y+1) and (sc.board[self.__x+1][self.__y+1]=="*" or sc.board[self.__x+1][self.__y+1]=="H")):
                self.__y+=1
            else:
                self.__y-=1
        sc.prplayer(self.__x, self.__y, "D")
        if(self.__y!=18):
            sc.prplayer(8,18,'H')

    def getx(self):
        self.xv=self.__x
        return (self.xv)

    def gety(self):
        self.yv=self.__y
        return (self.yv)

class Fireball(Person):
    """defines the methods and attributes of fireball"""

    def __init__(self,x,y):
        self.x=x
        self.y=y
        self.mv='d'

    def move(self, sc):
        self._rd=randint(1,10)
        sc.prplayer(self.x, self.y,sc.oldk)
        if(self.mv=='d'):
            if(sc.checkCollision(self.x,self.y+1)==False):
                sc.oldk=sc.board[self.x][self.y-1]
                self.y=self.y-1
                self.mv='a'
            else:
                if(sc.board[self.x+1][self.y+1]=='*'):
                    self.mv='d'
                elif(sc.board[self.x+1][self.y+1]=='H'):
                    if(self._rd%2==0):
                        self.mv='s'
                    else:
                        self.mv='d'
                elif(sc.board[self.x+1][self.y+1]==' '):
                    self.mv='s'
                sc.oldk=sc.board[self.x][self.y+1]
                self.y=self.y+1
        elif(self.mv=='a'):
            if(sc.checkCollision(self.x,self.y-1)==False):
                sc.oldk=sc.board[self.x][self.y+1]
                self.y=self.y+1
                self.mv='d'
            else:
                if(sc.board[self.x+1][self.y-1]=='*'):
                    self.mv='a'
                elif(sc.board[self.x+1][self.y-1]=='H'):
                    if(self._rd%2==0):
                        self.mv='s'
                    else:
                        self.mv='a'
                elif(sc.board[self.x+1][self.y-1]==' '):
                    self.mv='s'
                sc.oldk=sc.board[self.x][self.y-1]
                self.y=self.y-1
        elif(self.mv=='s'):
            if(sc.board[self.x+1][self.y]=='H' or sc.board[self.x+1][self.y]==' '):
                sc.oldk=sc.board[self.x+1][self.y]
                self.x=self.x+1
                self.mv='s'
            elif(sc.board[self.x+1][self.y]=='*'):
                if(self._rd%2==0):
                    self.mv='a'
                else:
                    self.mv='d'
        sc.prplayer(self.x,self.y,'O')

    def getx(self):
        return (self.x)

    def gety(self):
        return (self.y) 



class Screen:
    """Creating the Donkey Kong Board and Functions"""

    def __init__(self):
        """Defining the board and score"""
        self.score=0
        self.old=' '
        self.oldj=' '
        self.oldk=' '
        self.board=[['*','*','*','*','*','*','*','*','*','*','*','*','*','*','*','*','*','*','*','*','*','*','*','*','*','*','*','*','*','*','*','*','*','*','*','*','*','*','*','*','*','*','*','*','*','*','*','*','*','*','*','*','*','*','*','*','*','*','*','*','*','*','*','*','*','*','*','*','*','*','*','*','*','*','*','*','*','*','*','*'],
                    ['*',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ','*'],
                    ['*',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ','*'],
                    ['*',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ','*'],
                    ['*',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ','*',' ',' ','Q',' ',' ',' ',' ',' ','*',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ','*'],
                    ['*',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ','*','*','*','*','*','*','*','H','*','*',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ','*'],
                    ['*',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ','H',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ','*'],
                    ['*',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ','H',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ','*'],
                    ['*',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ','H',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ','*'],
                    ['*','*','*','*','*','*','*','*','*','*','*','*','*','*','*','*','*','*','*','*','*','*','*','*','*','*','*','*','H','*','*','*','*','*','*','*','*','*','*','*','*','*','*','*','*','*','*','*','*','*','*','*','*','*','*','*','*','*','*','*',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ','*'],
                    ['*',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ','H',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ','*'],
                    ['*',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ','H',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ','*'],
                    ['*',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ','H',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ','*'],
                    ['*',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ','*','*','*','*','*','*','*','*','*','*','*','*','*','*','*','*','*','*','*','*','*','*','*','H','*','*','*','*','*','*','*','*','*','*','*','*','*','*','*','*','*','*','*','*','*','*','*','*','*','*','*','*','*','*','*','*','*','*','*','*'],
                    ['*',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ','H',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ','*'],
                    ['*',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ','H',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ','*'],
                    ['*',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ','H',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ','*'],
                    ['*','*','*','*','*','*','*','*','*','*','*','*','*','*','*','*','*','*','*','*','*','*','*','*','*','*','*','*','*','*','*','*','*','*','*','*','*','*','*','*','*','*','*','*','*','*','*','*','*','*','*','*','*','*','*','*','*','*','H','*',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ','*'],
                    ['*',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ','H',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ','*'],
                    ['*',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ','H',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ','*'],
                    ['*',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ','H',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ','*'],
                    ['*',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ','*','*','*','*','H','*','*','*','*','*','*','*','*','*','*','*','*','*','*','*','*','*','*','*','*','*','*','*','*','*','*','*','*','*','*','*','*','*','*','*','*','*','*','*','*','*','*','*','*','*','*','*','*','*','*','*','*','*','*','*'],
                    ['*',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ','H',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ','*'],
                    ['*',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ','H',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ','*'],
                    ['*',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ','H',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ','*'],
                    ['*','*','*','*','*','*','*','*','*','*','*','*','*','*','*','*','*','*','*','*','*','*','*','*','*','*','*','*','*','*','*','*','*','*','*','*','*','*','*','*','*','*','*','*','H','*','*','*','*','*','*','*','*','*','*','*','*','*','*','*',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ','*'],
                    ['*',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ','H',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ','*'],
                    ['*',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ','H',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ','*'],
                    ['*',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ','H',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ','*'],
                    ['*','*','*','*','*','*','*','*','*','*','*','*','*','*','*','*','*','*','*','*','*','*','*','*','*','*','*','*','*','*','*','*','*','*','*','*','*','*','*','*','*','*','*','*','*','*','*','*','*','*','*','*','*','*','*','*','*','*','*','*','*','*','*','*','*','*','*','*','*','*','*','*','*','*','*','*','*','*','*','*']]

    def prscreen(self):
        """Printing Board after each Move"""
        PURPLE = '\033[95m'
        CYAN = '\033[96m'
        DARKCYAN = '\033[36m'
        BLUE = '\033[94m'
        GREEN = '\033[92m'
        YELLOW = '\033[93m'
        RED = '\033[91m'
        BOLD = '\033[1m'
        UNDERLINE = '\033[4m'
        END = '\033[0m'
        for i in range(0,30):
            for j in range(0,80):                
                if(self.board[i][j]=='*'):
                    print ( BOLD + PURPLE + '*'+ END),
                elif(self.board[i][j]=='H'):
                    print (UNDERLINE + "H" + END),
                elif(self.board[i][j]=='P'):
                    print ( BOLD + GREEN + "P" + END),
                elif(self.board[i][j]=='D'):
                    print ( BOLD + DARKCYAN + "D" + END),
                elif(self.board[i][j]=='Q'):
                    print (BLUE + "Q" + END),
                elif(self.board[i][j]=='O'):
                    print ( BOLD + RED + "O" + END),
                elif(self.board[i][j]=='C'):
                    print (YELLOW + "C" + END),                
                else:
                    print self.board[i][j],
            print ""
    def prplayer(self,x,y,inp):
        """Prints Position of Player Each Move"""
        if(inp=='P'):
            if(self.board[x][y]=='C'):
        	   self.CoinCheck()
        self.board[x][y]=inp

    def checkCollision(self,x,y):
        """Checks if the move made by Player causes Collision with walls"""
        if(self.board[x][y]=='*'):
            return False
        else:
            return True

    def genCoins(self):
    	"""Generates the Coins on the Board"""
        self.l=[12,16,20,24,28]
    	self.count=20
        self.i=0
        self.j=0
        while(self.count!=0):
            while(self.board[self.i][self.j]!=' '):
                self.i=choice(self.l)
                self.j=randint(20,60)
            self.board[self.i][self.j]='C'
            self.count=self.count-1

    def CoinCheck(self):
    	"""Checks and Acts upon Player collecting a coin"""
    	self.score+=5
    	if(self.score!=0 and (self.score%100)==0):
    		self.genCoins()

   	def getScore(self):
   		"""Return current score"""
   		return (self.score)

    def checkLjump(self,x,y):
        """Checks if jump to left is possible"""
        self.tx=x
        self.ty=y
        self.i=0
        for i in range(4):
            if(self.board[self.tx][self.ty-i-1]=="*"):
                return False
            else:
                return True

    def checkRjump(self,x,y):
        """Checks if jump to right is possible"""
        self.tx=x
        self.ty=y
        self.i=0
        for i in range(4):
            if(self.board[self.tx][self.ty+i+1]=="*"):
                return False
            else:
                return True

    def checkSave(self,pl):
        x=pl.getx()
        y=pl.gety()
        if(x==4 and y==14):
            return 1

    def checkBust(self,pl,dk):
        x1=pl.getx()
        y1=pl.gety()
        x2=dk.getx()
        y2=dk.gety()
        if(x1==x2 and y1==y2):
            return -1


    def checkBoom(self,pl,fb):
        x1=pl.getx()
        y1=pl.gety()
        x2=fb.getx()
        y2=fb.gety()
        if(x1==x2 and y1==y2):
            return -1
        

"""Main Function"""
def main():
    screen=Screen()
    player=Player(28,2)
    donkey=Donkey(8,2)
    fireball=Fireball(8,5)
    screen.prplayer(28,2,'P')
    screen.genCoins()
    os.system("clear")
    screen.prscreen()
    while(True):
        inp=getchar()
        if(inp==' '):
            jumpdir=getchar()
            if(jumpdir=='a' or jumpdir=='A'):
                player.ljump(screen)
            elif(jumpdir=='d' or jumpdir=='D'):
                player.rjump(screen)
            elif(jumpdir=='q' or jumpdir=='Q'):
                break
        elif(inp=="q" or inp=="Q"):
            break
        else:
            player.move(inp,screen)
        donkey.move(screen)
        fireball.move(screen)
        if(screen.checkSave(player)==1):
            print("Congratulations! You won!")
            print("Score: "),
            print screen.score+50
            break
        if(screen.checkBust(player,donkey)==-1):
            break
        if(screen.checkBoom(player,fireball)==-1):
            break
        os.system("clear")
        screen.prscreen()
        print "Score: ",
        print screen.score
        print "Use 'w'/'a'/'s'/'d' to Move | Space followed by 'a' or 'd' to Jump | 'q' to Quit:"
	

if __name__=="__main__":
    main()


    
                                            
                        

            

