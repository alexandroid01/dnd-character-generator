#This is a DND character generator- with 19,890 unique character possibilities!
import random
import time

#List of 10 personality traits
personalities = ['playful', 'strong', 'laid-back', 'brilliant', 'conscientious', 'sensitive', 'punctual', 'daring', 'suave', 'tidy']

#List of 9 dnd races
races = ['dragonborn', 'dwarf', 'elf', 'tiefling', 'half-elf', 'half-orc', 'human', 'halfling', 'gnome']

#List of 13 dnd classes
classes = ['artificer', 'barbarian', 'bard', 'cleric', 'druid', 'fighter', 'monk', 'paladin', 'ranger', 'rogue', 'sorcerer', 'warlock', 'wizard']

#List of 17 dnd backgrounds
backgrounds = ['acolyte', 'charlatan', 'criminal', 'entertainer', 'folk hero', 'gladiator', 'guild merchant', 'guild artisan', 'hermit', 'knight', 'noble', 'outlander', 'pirate', 'sage', 'sailor', 'soldier', 'urchin']

def displayIntro():
    print('Introducing your new champion, a...')

def displayPersonality():
    #Prints a random personality trait from list
    print(personalities[random.randint(0,9)], end = ' ')

def displayRace():
    #Prints a random race from list
    print(races[random.randint(0,8)], end = ' ')

def displayClass():
    #Prints a random class from list
    print(classes[random.randint(0,12)], end = ' ')

def displayBackground():
    #Prints a random background from list
    backgroundRandom = backgrounds[random.randint(0,16)]

playAgain = 'yes'
while playAgain == 'yes' or playAgain == 'y':
    displayIntro()

    print()
    time.sleep(1)
    
    displayPersonality()
    displayRace()
    displayClass()
    displayBackground()

    print()
    time.sleep(1)

    #Player can choose whether they want another character generated for them
    print('Do you want another randomly-generated character? (yes or no)')
    playAgain = input()

    if playAgain == 'no' or playAgain == 'n':
        print('Good luck on your quest!')

