from copy import *   # import copy module
from random import * # import random module
import pyinputplus as pyip # import pyInputPlus
class TicTacToe:
    state={} # to store current state of game
    terminal_state=[[1,2,3],[1,4,7],[3,6,9],[7,8,9],[4,5,6],[2,5,8],[1,5,9],[3,5,7]] # final states when either x win or 0 win or draw
    plr,ai='O','X'
    # a is alpha, b is beta
    
    def printState(self,state):  # to print tic tac toe board
        for i in range(1,10):
            if i%3==0 : #the 3rd column
                print(state[i])
                if i<8: #printing the lines
                    print("-+-+-")
            else: #if tile is empty
                if state[i]=="" :
                    print(state[i],end=" |")
                else: #if tile isn't empty
                    print(state[i],end="|")
        print("\n")

    def legend(self): # numbering of each tile
        print("Legend of the Board\n")
        print("1|2|3")
        print("-+-+-")
        print("4|5|6")
        print("-+-+-")
        print("7|8|9")
        print("\n")

    def invalidMove(self,state,pos):  # to check whether tile is already filled or not
        return 1 if state[pos]!= "" else 0

    def terminal(self,terminal_state,state,plr='O'):  # to check whether game is finished or not
            for i in range(8):
                x= terminal_state[i] #a particular terminal state
                a = state[x[0]] 
                L = [state[x[0]],state[x[1]],state[x[2]]] #tiles in the current row

                if len(set(L))==1 and (a!=""): #if all tiles in the given row are same and are not empty
                        return -1 if a==plr else 1 # -1 if O wins else 1 if X wins
            return 0 if "" not in state.values() else 2 # 0 means draw and 2 means running

    def init(self): #initialises the state to empty
        for i in range(1,10):
            self.state.update({i:""})  # initialising state
    
    def maxVal(self,state,a,b,ai='X'): #finds the maximum utility of the child state from the given state    
        plr = 'X' if(ai=='O') else 'O'
        result=self.terminal(self.terminal_state,state,plr)
        if(result!=2): # Game draw, win or lose
            return result  # return utility and depth

        child=[]  # to store all possible moves of state
        v=-1  # to store return maximum utility, initialising with 0  
        for i in range(1,10):
            if state[i]=="": # if a tile is empty, create a copy and place X there as a potential move
                new_state=deepcopy(state)   # copy of game_state
                new_state[i]=ai    # X doing a move
                child.append(new_state)

        for i in range(len(child)):
            mx=self.minVal(child[i],a,b,plr)
            v= max(v,mx)
            if v>=b : #making sure b > a
                return v
            a=max(a,v)
        return v  # return maximum utility of all child states

    def minVal(self,state,a,b,plr='O'): #finds the minimum utility of the child state from the given state  
        result=self.terminal(self.terminal_state,state,plr)
        if(result!=2):
            return result  # return utility

        child=[]   # to store all possible moves of state
        v=1   # to store return minimum utility, initialising with 1 
        for i in range(1,10):
            if state[i]=="": # if a tile is empty, create a copy and place O there as a potential move
                new_state=deepcopy(state)   # copy of game_state
                new_state[i]=plr   # O doing a move
                child.append(new_state) 

        ai = 'X' if(plr=='O') else 'O'
        for i in range(len(child)):
            mn=self.maxVal(child[i],a,b,ai)
            v= min(v,mn)
            if v<=a : #making sure b>a
                return v
            b=min(b,v)
        return v   # return utility

    def minMax(self,ai='X'):
        child=[]  # to store all possible moves of state
        a=float("-inf") #first alpha is -infinity
        b=float("inf") #first beta is infinity

        for i in range(1,10): #first minimising for the AI player to get the initial child states
            if self.state[i]=="": # if a tile is empty, create a copy and place X there as a potential move
                new_state=deepcopy(self.state)   # copy of state
                new_state[i]=ai   # x doing a move
                child.append(new_state) 

        plr = 'X' if(ai=='O') else 'O'
        util=[]   # to store utility values of different child states
        v=-1 # to store return minimum utility, initialising with -1
        for i in range(len(child)):
            mx = self.minVal(child[i],a,b,plr)
            util.append(mx)  # appending utility

        m = max(util) #maximum utility of all child states from player's move (all moves which AI can do)
        L = [] # list of childs with maximum utility

        for i in range(len(child)):
            if(util[i]==m): #As it is possible for multiple states to have same utility values
                L.append(i)
        rand = choice(L) # selecting a random child with max utility

        return child[rand] #assigning the new state or the move of the AI

    def game(self,plr='O'):
        while(1):
            self.legend()
            print("Your turn to play , enter the position")
            pos = int(input())   # input for 0's move

            while(self.invalidMove(self.state,pos)==1):
                print("Invalid move \nEnter the position again")
                pos = int(input())

            self.state[pos]=plr
            self.printState(self.state)

            if(self.terminal(self.terminal_state,self.state,plr)==0):  # condition for game draw
                print("Game Draw")
                break

            elif(self.terminal(self.terminal_state,self.state,plr)==-1): # condition for O won
                print("Player wins")
                break

            else:
                ai = 'X' if(plr=='O') else 'O'
                self.state=self.minMax(ai) #calling minMax for decision making for AI
                # Assuming the player is playing optimally
                self.printState(self.state) #printing the current state
                if(self.terminal(self.terminal_state,self.state,plr)==1):  # condition for X won
                    print("AI wins")
                    break
    
    def startMenu(self): # start of the game
        print("Welcome to the Game of Tic Tac Toe\n")
        while(True):
            self.init() # initialises the game state (not a constructor)
            print("Press Y to continue playing or E to exit: ") 
            ex = pyip.inputMenu(["Y","E"],numbered=True) #if you want to continue playing
            if(ex=='Y'):
                print("Choose O or X") 
                plr = pyip.inputMenu(["O","X"],numbered=True) # choose your own game piece
                self.game(plr)
            else: # you entered to exit
                print("Goodbye!")
                break

game1 = TicTacToe()
game1.startMenu()