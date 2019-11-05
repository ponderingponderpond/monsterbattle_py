#Global Variable, just to illustrate how those work, really.
#importing the specific means you can just call randint without using random.randint everytime
from random import randint 
from random import choice

#importing the module monsterbattle_monsterpool and renaming it to mbtl_mpool to work with it a little easier
import monsterbattle_monsterpool as mbtl_mpool 

#Just for learning how global variables work
damageDone = 3 

#this defines a function
def monsterBattle():  
    #Building the variable contents for the monster based on the selection in "monsterPool"
    selectedMonster = choice(mbtl_mpool.monsterPool)
    selectedMonsterName = selectedMonster.get('name')
    selectedMonsterArticle = selectedMonster.get('article')
    selectedMonsterHealth = selectedMonster.get('health')
    #Printing multiline text using ''' Stuff ''''; "playerName" is undefined, because it takes the value from the monsterbattle_main variable based on user input, as it's called.
    print(f'''
    You have encountered {selectedMonsterArticle} {selectedMonsterName}. Get ready to fight. It has {selectedMonsterHealth} health.
    Do you posess the will to fight this {selectedMonsterName}, {playerName}?
    Roll the dice and learn your fate!
    ''') #the "f" allows to use {} to call on variables instead of needing to go the long way via + [] +
    playerMoraleThrowCheck = input('(Hint: type \"roll\") ')
    #the .lower() converts any input like ROLL to roll, so the input is valid since it expects lower case "roll"
    if playerMoraleThrowCheck.lower() == 'roll': 
        playerMoraleThrow = randint(1, 6)
        if playerMoraleThrow > 1:
            print('You have the will to fight and engage the enemy!')
        else:
            print('You lack the will to fight.')
    else:
        print('All you had to do was type \"roll\"...')
    
    #call in global variable to assign new value in next step
    global damageDone 
    #local variable because it's within a defined function, overrides global variable
    damageDone = 0 
    
    while selectedMonsterHealth > 0:
        if playerMoraleThrow > 1:
            #putting the randint() in the "while" loop continually generates new numbers instead of just repeating the one that was picked outside of it (as I had it before).
            actualDamageDealt = randint(1, 5) 
            #+= does the same thing as damageDone = damageDone + standardDot, since damageDone is used both as a variable and a value. This is an "augmented assignment operator"
            damageDone += actualDamageDealt 
            selectedMonsterHealth -= actualDamageDealt
            print(f'You hit the {selectedMonsterName} for {actualDamageDealt} reducing its health to {selectedMonsterHealth}')
            if selectedMonsterHealth <= 0:
                print(f'You have dealt {damageDone} damage overall.') 
                cheers = ['Huzza!', 'Glorious!', 'Fantastic!', 'You can do better, though.', 'Honestly, it wasn\'t that hard.', 'Gee golly, aren\'t you strong...']
                print(f'You have killed the {selectedMonsterName}! {choice(cheers)}')
                break
        else:
            print(f'You are freigthened by the {selectedMonsterName}. Best you run away and save your petty hide!')
            break #stops the while loop, so it doesn't infinetely print to terminal that you are a coward.

