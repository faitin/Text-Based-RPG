#prototype for first project: Text based RPG!
#
#Michael Donnelly
#v1.1
#9-20-2016

#Class Selection:
myClass="unchosen"
print("Welcome! To begin please select one of the following classes:")
while myClass != "fighter" or myClass !="wizard" or myClass !="archer":
    print("Fighter, Wizard, Archer")
    myClass=str.lower(str(input()))
    if myClass == "fighter" or myClass=="wizard"or myClass=="archer":
        print("You have chosen",myClass)
        if myClass =="fighter":
            print("Fighters are specialists at melee combat.\nThey are incredible strong and can take quite a few hits")
        elif myClass =="wizard":
            print("Wizards are users of arcane magic.\nThey can use this to deal massive amounts of damage or to preform special tasks.\n Wizards typically are not very strong and die easily when hit.")
        elif myClass =="archer":
            print("Archers are experts of ranged combat.\nThey can attack oponnents from far away and have a decent amount of health.")
        else:
            print("There is an error")
        print("Are you happy with your class? yes or no")
        classConfirmation=str.lower(str(input()))
        if classConfirmation=="yes":
            print("Great! let us begin the story")
            break
        else:
            print("choose a different class:")
    elif myClass != "fighter" or myClass != "wizard" or myClass != "archer":
        print("I am sorry but that is not an available class.\nplease select one of the following:")
    else:
        print("There is an error")

#Character Statistics:
import random
if myClass=="fighter":
    level=1
    maxHP=14
    hitDie=random.randint(1,10)+4
    currentHP=maxHP
    attackModifier=5
    attackDamage=6
    attackDie=random.randint(1,6)+random.ranint(1,6)
    attackDieDisplay="2d6"
    weapon="greatSword"
    AC=19
    will=0
elif myClass=="wizard":
    level=1
    maxHP=8
    hitDie=random.randint(1,6)+2
    currentHP=maxHP
    attackModifier=0
    attackDamage=1
    attackDie=random.randint(1,4)
    attackDieDisplay="1d4"
    weapon="dagger"
    AC=13
    will=2
elif myClass=="archer":
    level=1
    maxHP=13
    hitDie=random.randint(1,10)+3
    currentHP=maxHP
    attackModifier=4
    attackDamage=5
    attackDie=random.randint(1,8)
    attackDieDisplay="1d8"
    weapon="composite longbow"
    AC=18
    will=0
else:
    print("There is an error")

#spells:
def spellList():
    spellsKnown=3+2(level-1)
    if spellsKnown <= 3:
        print("Spells Knwon="spellsKnown)
        print("""   SpellList:
    Magic Missile:Shoots 1 missile for every 2 levels. each missile deals 1d4+1
    Mage Armor: Creates magical armor that adds 4 to your AC. Lasts for 10 commands per level
    """)
    

def stats():
    print("Here are your current stats:")
    print("\tLevel="level)
    print("\tHP="currentHP)
    print("\tAttack Modifier="attackModifier)
    print("\tAttack Damage="attackDamage)
    print("\tAttack Die="attackDieDisplay)

#Tutorial:
