#Import stuff to help with stuff
from random import randint #importing the specific means you can just call randint without using random.randint everytime
from random import choice

import monsterbattle_battle as mbtl_btl #Not sure if I use from if I can pass on values generated in this module to the imported one. 

#locationPool - unused so far
l_forrestPath = {'combatPlayerBonus': 1}

print('Who are you?')
playerName = input()
mbtl_btl.playerName = playerName #Here we define "PlayerName" to be the same for the module monsterbattle_battle as well, otherwise using the mbtl_btl.monsterBattle() later won't know what the player typed as their name.
if len(playerName) > 3:
    print(f'{playerName}, eh? How odd. Well, {playerName}, would you like to go on an adventure?')
elif len(playerName) <= 3:
    print(f'{playerName}? That\'s kind of short, isn\'t it? Fine. Want to have an adventure?')

goForth = input()
if goForth.lower() == 'yes':
    print('Let\'s roll the dice and see what happens, shall we? (Hint: type \"roll\")')
    playerRoll = input()
    if playerRoll.lower() == 'roll':
        playerDiceRoll = randint(1, 6)
        print ('You have rolled a', playerDiceRoll, '.')
        if playerDiceRoll >= 2:  
            print('You hear something suspicious. Do you wish to investigate?')
            playerChoice = input()
            if playerChoice.lower() == 'yes':           
                mbtl_btl.monsterBattle() #this calls/executes the function from the module mbtl_btl which we shortened above from monsterbattle_battle
            else:
                print(f'{playerName} is a little coward, eh?')
        else:
            print('Nothing happens and you have no adventures. Pity.')
    else:
        print('I gave you a hint!')
else:
    print('Fine. Spoilsport.')


