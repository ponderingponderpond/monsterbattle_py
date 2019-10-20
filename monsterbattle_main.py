#Import stuff to help with stuff
from random import randint #importing the specific means you can just call randint without using random.randint everytime
from random import choice

#monsterPool
m_skeletonWarrior = {'health': 20, 'name': 'Skeleton Warrior', 'article': 'a'}
m_orcWarrior = {'health': 27, 'name': 'Orc Warrior', 'article': 'an'}
m_wrigglingFinger = {'health': 3, 'name': 'Wriggling Finger', 'article': 'a'}

monsterPool = [m_orcWarrior, m_skeletonWarrior, m_wrigglingFinger]

#locationPool - unused so far
l_forrestPath = {'combatPlayerBonus': 1}

#Global Variable, just to illustrate how those work, really.
damageDone = 3 

def monsterBattle():  #this defines a function
    #Building the variable contents for the monster based on the selection in "monsterPool"
    selectedMonster = choice(monsterPool)
    selectedMonsterName = selectedMonster.get('name')
    selectedMonsterArticle = selectedMonster.get('article')
    selectedMonsterHealth = selectedMonster.get('health')
    print(f'You have encountered {selectedMonsterArticle} {selectedMonsterName}. Get ready to fight. It has {selectedMonsterHealth} health.') #the "f" allows to use {} to call on variables instead of needing to go the long way via + [] +
    print(f'Do you posess the will to fight this {selectedMonsterName}, {playerName}? Roll the dice and learn your fate!')
    playerMoraleThrowCheck = input()
    if playerMoraleThrowCheck.lower() == 'roll': #the .lower() converts any input like ROLL to roll, so the input is valid since it expects lower case "roll"
        playerMoraleThrow = randint(1, 6)
        if playerMoraleThrow > 1:
            print('You have the will to fight and engage the enemy!')
        else:
            print('You lack the will to fight.')
    else:
        print('All you had to do was type \"roll\"...')
    
    actualDotDamage = randint(1, 5)

    global damageDone #overrides the global variable for both local and global scope
    damageDone = 0 #local variable because it's within a defined function
    
    while selectedMonsterHealth > 0:
        if playerMoraleThrow > 1:
            damageDone += actualDotDamage #+= does the same thing as damageDone = damageDone + standardDot, since damageDone is used both as a variable and a value. This is an "augmented assignment operator"
            selectedMonsterHealth -= actualDotDamage
            print(f'You hit the {selectedMonsterName} for {actualDotDamage} reducing its health to {selectedMonsterHealth}')
            if selectedMonsterHealth <= 0:
                print(f'You have dealt {damageDone} damage overall.') 
                cheers = ['Huzza!', 'Glorious!', 'Fantastic!', 'You can do better, though.', 'Honestly, it wasn\'t that hard.', 'Gee golly, aren\'t you strong...']
                print(f'You have killed the {selectedMonsterName}! {choice(cheers)}')
        else:
            print(f'You are freigthened by the {selectedMonsterName}. Best you run away and save your petty hide!')
            break #stops the while loop, so it doesn't infinetely print to terminal that you are a coward.


print('Who are you?')
playerName = input()
if len(playerName) > 3:
    print(f'{playerName}, eh? How odd. Well, {playerName}, would you like to go on an adventure?')
elif len(playerName) < 3:
    print(f'{playerName}? That\'s kind of short, isn\'t it? Fine. Want to have an adventure?')

goForth = input()
if goForth.lower() == 'yes':
    print('Let\'s roll the dice and see what happens, shall we? (Hint: type \"roll\")')
    playerRoll = input()
    if playerRoll.lower() == 'roll':
        playerDiceRoll = randint(1, 6)
        print ('You have rolled a', playerDiceRoll, '.')
        if playerDiceRoll >= 2:  
            print(f'You hear something suspicious. Do you wish to investigate, {playerName}?')
            playerChoice = input()
            if playerChoice.lower() == 'yes':           
                monsterBattle() #this calls/executes the function
            else:
                print(f'{playerName} is a little coward, eh?')
        else:
            print('Nothing happens and you have no adventures. Pity.')
    else:
        print('I gave you a hint!')
else:
    print('Fine. Spoilsport.')


