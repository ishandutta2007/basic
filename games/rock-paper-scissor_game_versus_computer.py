# Last updated: 17-Oct-2012
# Udaya Maurya (udaya_cbscients@yahoo.com, telegram: https://t.me/udy11)
# Source: https://github.com/udy11, https://gitlab.com/udy11
# Rock-Paper-Scissor Game
# Player vs. Computer

# RULES:
# Rock crushes Scissor
# Paper covers Rock
# Scissors cut Paper

# In the statistics report, ties are not counted in total matches

import random
def rps(pch):
    while not pch in 'rps':
        pch=input("Enter r, p or s only: ")
    pn='rps'.find(pch)
    rps_str=["rock","paper","scissor"]
    print("You chose: ",rps_str[pn])
    cn=random.randrange(0,3)
    print("Comp chose:",rps_str[cn])
    wf=pn-cn
    if wf==1 or wf==-2:
        print("Player Wins!")
        return 1
    elif wf==0:
        print("Both Tie!")
        return 0
    else:
        print("Computer Wins!")
        return 2
    
print("r -> rock, p -> paper, s -> scissor")
tp=0; tw=0; ty=0
while 1:
    pch=input("Enter your choice: ")
    d=rps(pch)
    if d>0:
        tp+=1
    if d==1:
        tw+=1
    elif d==0:
        ty+=1
    print("------- Wins: "+str(tw)+"/"+str(tp)+", Ties: "+str(ty)+" -------")
