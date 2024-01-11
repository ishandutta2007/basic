# Last updated: 17-Oct-2012
# Udaya Maurya (udaya_cbscients@yahoo.com, telegram: https://t.me/udy11)
# Source: https://github.com/udy11, https://gitlab.com/udy11
# Rock-Paper-Scissor-Lizard-Spock Game
# Player vs. Computer

# RULES (as explained by Sheldon Cooper):
# It's very simple:
# scissor cuts paper
# paper covers rock
# rock crushes lizard
# lizard poisons Spock
# Spock smashes scissor
# scissor decapitates lizard
# lizard eats paper
# paper disproves Spock
# Spock vaporizes rock
# and as it always has
# rock crushes scissor

# In the statistics report, ties are not counted in total matches

import random
def rpslS(pch):
    while not pch in 'rSpls':
        pch=input("Enter r, p, s, l or S only: ")
    pn='rSpls'.find(pch)
    rSpls_str=["rock","Spock","paper","lizard","scissor"]
    print("You chose: ",rSpls_str[pn])
    cn=random.randrange(0,5)
    print("Comp chose:",rSpls_str[cn])
    wf=(pn-cn)%5
    if wf==0:
        print("Both Tie!")
        return 0
    elif wf<3:
        print("Player Wins!")
        return 1
    else:
        print("Computer Wins!")
        return 2

print("r -> rock, p -> paper, s -> scissor, l -> lizard, S -> Spock")
tp=0; tw=0; ty=0
while 1:
    pch=input("Enter your choice: ")
    d=rpslS(pch)
    if d>0:
        tp+=1
    if d==1:
        tw+=1
    elif d==0:
        ty+=1
    print("------- Wins: "+str(tw)+"/"+str(tp)+", Ties: "+str(ty)+" -------")
