#Import stuff to help with stuff
from random import randint #importing the specific means you can just call randint without using random.randint everytime
from random import choice

#monsterPool
m_skeletonWarrior = {'health': 20, 'name': 'Skeleton Warrior', 'article': 'a'}
m_orcWarrior = {'health': 27, 'name': 'Orc Warrior', 'article': 'an'}
m_wrigglingFinger = {'health': 3, 'name': 'Wriggling Finger', 'article': 'a'}

monsterPool = [m_orcWarrior, m_skeletonWarrior, m_wrigglingFinger]

#locationPool
l_forrestPath = {'combatPlayerBonus': 1}

damageDone = 3 #global variable

def monsterBattle():  #this defines a function
    #Building the variable contents for the monster based on the selection in "monsterPool"
    selectedMonster = choice(monsterPool)
    selectedMonsterName = selectedMonster.get('name')
    selectedMonsterArticle = selectedMonster.get('article')
    selectedMonsterHealth = selectedMonster.get('health')

    monsterEncounteredMsg = f'You have encountered {selectedMonsterArticle} {selectedMonsterName}. Get ready to fight. It has {selectedMonsterHealth} health.' #the "f" allows to use {} to call on variables instead of needing to go the long way via + [] +
    print(monsterEncounteredMsg)
    
    playerMoraleCheckMsg = f'Do you posess the will to fight this {selectedMonsterName}, {playerName}? Roll the dice and learn your fate!'
    print(playerMoraleCheckMsg)
    playerMoraleThrowCheck = input()
    if playerMoraleThrowCheck == 'roll':
        playerMoraleThrow = randint(1, 6)
        if playerMoraleThrow > 1:
            print('You have the will to fight and engage the enemy!')
        else:
            print('You lack the will to fight and flee in terror.')
    else:
        print('All you had to do was type \"roll\"...')
    
    actualDotDamage = randint(1, 5)

    global damageDone #overrides the global variable for both local and global scope
    damageDone = 0 #local variable because it's within a defined function
    
    while selectedMonsterHealth > 0:
        if playerMoraleThrow > 1:
            damageDone += actualDotDamage #+= does the same thing as damageDone = damageDone + standardDot, since damageDone is used both as a variable and a value. This is an "augmented assignment operator"
            selectedMonsterHealth -= actualDotDamage
            dmgOutputMsg = f'You hit the {selectedMonsterName} for {actualDotDamage} reducing its health to {selectedMonsterHealth}'
            print(dmgOutputMsg)
            if selectedMonsterHealth <= 0:
                dmgDoneMsg = f'You have dealt {damageDone} damage overall.'
                print(dmgDoneMsg) 
                cheers = ['Huzza!', 'Glorious!', 'Fantastic!', 'You can do better, though.', 'Honestly, it wasn\'t that hard.', 'Gee golly, aren\'t you strong...']
                cheersMsg = f'You have killed the {selectedMonsterName}! {choice(cheers)}'
                print(cheersMsg)
        else:
            fleeingMsg = f'You are freigthened by the {selectedMonsterName} and will deal {actualDotDamage} damage. Best you run away and save your petty hide!'
            print(fleeingMsg)
            break #stops the while loop, so it doesn't infinetely print to terminal that you are a coward.


print('Who are you?')
playerName = input()
lightlyInsultingIntro = f'{playerName}, eh? How odd. Well, {playerName}, would you like to go on an adventure?'
print(lightlyInsultingIntro)

goForth = input()
if goForth == 'yes':
    print('Let\'s roll the dice and see what happens, shall we? (Hint: type \"roll\")')
    playerRoll = input()
    if playerRoll == 'roll':
        playerDiceRoll = randint(1, 6)
        print ('You have rolled a', playerDiceRoll, '.')
        if playerDiceRoll >= 2:  
            playerHearsSomethingMsg = f'You hear something suspicious. Do you wish to investigate, {playerName}?'
            print(playerHearsSomethingMsg)
            playerChoice = input()
            if playerChoice == 'yes':           
                monsterBattle() #this calls/executes the function
            else:
                playerCowardMsg = f'{playerName} is a little coward, eh?'
                print(playerCowardMsg)
        else:
            print('Nothing happens and you have no adventures. Pity.')
    else:
        print('I gave you a hint!')
else:
    print('Fine. Spoilsport.')


