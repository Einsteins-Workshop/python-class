health1=15
stamina1=10
attunement1=12
health2=15
stamina2=10
attunement2=12
health3=15
stamina3=10
attunement3=12
en1hp=30
en2hp=10
en3hp=10



enlist= {
    "1": "solid calcite guardian",
    "2": "👁voidwalker",
    "3": "👁other voidwalker",
}
#the player's inventory loadout at the start of the game
items=["medkit","medkit","burn cream","healing remedy","poison darts"]
scrap=100

def turn (name, cl, mg, cn):

    healths = {
        "1": health1,
        "2": health2,
        "3": health3
    }
    attunements = {
        "1": attunement1,
        "2": attunement2,
        "3": attunement3
    }
    staminas = {
        "1": stamina1,
        "2": stamina2,
        "3": stamina3
    }

    print("---",name,"---")
    print(" ")
    print(f"health [{(healths[cn])}]")
    print(" ")
    print(f"attunement [{(attunements[cn])}]")
    print(" ")
    print(f"stamina [{(staminas[cn])}]")
    print(" ")
    print("1-attack")
    print("2-abilities")
    print("3-items")
    print("4-psi")
    print("5-skip")
    actioncat=input(f"what would {name} like to do?")
    if actioncat=="1":
        print("lasered will do a basic attack.")
        action1=1
    if actioncat=="2":
        print(" \n ")
        print("---------------")

        print(" ")
        print("1-herbal brew [5]")
        print("Heals 5-7 hp from an ally of your choice.")
        print(" ")
        print("2-24 karat concoction [6]")
        print("deals 4 capitalism and 4 opalescent damage \nto an enemy of your choice.")
        print(" ")
        print("3-liquid focus elixir [4]")
        print("strengthens the psi abilities of an ally of \nyour choice for this turn.")
        print(" ")
        print("4-shade shielding aromatic [4]")
        print("boosts the DEF of an ally of your choice for \nthis turn.")
        print(" ")
        print("5-acidic spray [5]")
        print("deals 1-2 peirce damage to all enemies.")
        print(" \n ")
        action1=input(f"what ability will {name} use?")

    print(" \n ")
    print("---------------")

    print("1-⌬solid calcite guardian [",en1hp,"]")
    print("2-voidwaker [",en2hp,"]")
    print("3-other voidwaker [",en3hp,"]")
    print(" ")

    target1=input(f"who will {name} target?")

    print(name,"will target the",(enlist[target1]),".")
print (" \n \n \n \n \n \n \n \n")
print ("<|> FLOOR 1 <|> \n \n 👁They are watching. 👁They have found us. 👁They are not far behind.")
print(" \n \n ")
print ("tnh has encountered a solid calcite guardian. two voidwakers have also decided to join.")
print (" \n ")
turn("lasered","3","4","1")
print(" \n ")
print("---------------")
print(" \n ")
turn("testingjared","1","3","2")
print(" \n ")
print("---------------")
print(" \n ")
turn("other lasered","4","6","3")