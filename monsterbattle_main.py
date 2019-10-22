#Import stuff to help with stuff
from random import randint #importing the specific means you can just call randint without using random.randint everytime
from random import choice

import monsterbattle_battle as mbtl_btl #Not sure if I use from if I can pass on values generated in this module to the imported one. 

#locationPool - unused so far
l_forrestPath = {'combatPlayerBonus': 1}

gameLoopCount = 1
gameRun = True

#Let's have our player create his name as global variable to be used in everything subsequent from here on out.

print('Who are you?')
playerName = input()
mbtl_btl.playerName = playerName #Here we define "PlayerName" to be the same for the module monsterbattle_battle as well, otherwise using the mbtl_btl.monsterBattle() later won't know what the player typed as their name.


def gameIntroduction():
    if len(playerName) > 3:
        print(f'{playerName}, eh? How odd. Well, {playerName}, would you like to go on an adventure?')
    elif len(playerName) <= 3:
        print(f'{playerName}? That\'s kind of short, isn\'t it? Fine. Want to have an adventure?')

def gameShortIntroduction():
    print(f'Back again for more, {playerName}?')
    print(f'Alright, fine. You really want to try again?')


while gameRun == True:
    if gameLoopCount == 1:
        gameIntroduction()
    elif gameLoopCount > 1:
        gameShortIntroduction()
    
    goForth = input('Yes or no? ')

    if goForth.lower() == 'yes':
        print('Let\'s roll the dice and see what happens, shall we?')
        playerRoll = input('(Hint: type \"roll\") ')
        if playerRoll.lower() == 'roll':
            playerDiceRoll = randint(1, 6)
            print ('You have rolled a', playerDiceRoll, '.')
            if playerDiceRoll >= 2:  
                print('You hear something suspicious. Do you wish to investigate?')
                playerChoice = input('Yes or no? ')
                if playerChoice.lower() == 'yes':           
                    mbtl_btl.monsterBattle() #this calls/executes the function from the module mbtl_btl which we shortened above from monsterbattle_battle
                    userReplayChoiceRequest = True
                else:
                    print(f'{playerName} is a little coward, eh?')
                    userReplayChoiceRequest = True
            else:
                print('Nothing happens and you have no adventures. Pity.')
                userReplayChoiceRequest = True
        else:
            print('I gave you a hint!')
            userReplayChoiceRequest = True
    else:
        print('Fine. Spoilsport.')
        userReplayChoiceRequest = True
    gameLoopCount = gameLoopCount + 1
    if userReplayChoiceRequest == True:
        userReplayChoiceInput = input (f'Want to try again, {playerName}? ')
        if userReplayChoiceInput.lower() == 'yes':
            print('...')
        else:
            print(f'God, you are no fun, are you, {playerName}?')
            print(f'You have done this {gameLoopCount} times.')
            gameRun = False

