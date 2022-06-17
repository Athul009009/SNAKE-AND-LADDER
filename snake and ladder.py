# from pickle import TRUE
from pickle import TRUE
import random

from numpy import True_
# from turtle import pos
ladder={ 1:38, 4:14, 9:30, 21:42, 28:76, 50:64 ,88:99 ,71:92 }
snake= { 32:10 ,34:6 ,48:26 ,63:18 ,88:24 ,97:3 ,98:79 ,75:35}
pos1=0
pos2=0

def move(pos):
    dice=random.randint(1,6)
    print(f"dice    :{dice}")
    pos=pos+dice
    if pos in ladder:
        print("BITTEN BY SNAKE!!")
        pos=ladder[pos]
        print(f"YOUR CURRENT POSITION IS    :{pos}")
    
    elif pos in snake:
            print("BITTEN BY SNAKE!!")
            pos=snake[pos]
            print(f"YOUR CURRENT POSITION IS    :{pos}")
    
    else:
        print(f" YOUR CURRENT POSITION IS   :{pos}")
        
        print("\n")
        return pos    
    
while TRUE:
    A=input("PLAYER 1 ENTER \"A\" TO THROW DICE   :")
    pos1=move(pos1)
    if pos1>=100:
            print("PLAYER 1 WINS!!")
            break
    B=input("PLAYER 2 ENTER \"B\" TO THROW DICE   :")
    pos2=move(pos2)
    if pos2>=100:
            print("PLAYER 2 WINS!!")
            break
    

     
         
    
        
        
    
