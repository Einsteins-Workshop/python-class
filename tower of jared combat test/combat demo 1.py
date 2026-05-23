italics = '\033[3m'
end = '\033[0m'

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

itemdescs= {
    "medkit": "Medkit\nHeals 10 hp from an ally of your choice.",
    "burn cream": "burn cream\ncures burn from an ally of your choice.",
    "healing remedy": "healing remedy\nheals 5 hp from an ally of your choice.",
    "poison darts": "poison darts\ndeals 2 damage to and gives poison 5 to\n an enemy of your choice.",
}

enlist= {
    "1": "solid calcite guardian",
    "2": "voidwalker",
    "3": "other voidwalker",
}
#the player's inventory loadout at the start of the game
items=["medkit","medkit","burn cream","healing remedy","poison darts"]
scrap=100

def turn (name, cl, mg, cn):
    itemused = 0
    action = 0
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
        action=1
    if actioncat=="2":
        print(" \n ")
        print("---------------")
        if cl=="1":
            print(" ")
            print("1-Multi- attack [5]")
            print("Deals 1 Wp damage and 1-2 peirce damage to all enemies.")
            print(" ")
            print("2-Better slash [6]")
            print("deals 4 WP damage and 4 Pierce damage\nto an enemy of your choice.")
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
        if cl=="3":
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
        action=input(f"what ability will {name} use?")




    if actioncat == "3":
        print(" \n-----------------")
        for (i, item) in enumerate(items, start=1):
            print(i,f"- {(itemdescs[item])}\n-----------------")
        itemused=input(f"what item would {name} like to use?")



    print(" \n ")
    print("---------------")

    print("1-⌬solid calcite guardian [",en1hp,"]")
    print("2-👁voidwaker [",en2hp,"]")
    print("3-👁other voidwaker [",en3hp,"]")
    print(" ")

    target=input(f"who will {name} target?")

    print(name,"will target the",(enlist[target]),".")
    return target, itemused, action
print (f" \n \n \n \n \nyou stand at the foot of tower {italics} Epsilon|14-δ {end}")
Useless=input("Are you ready to start? (type anything)")

print (" \n \n \n \n \n \n \n \n")
print ("<|> FLOOR 1 <|> \n \n 👁Conceptualization α1 \n This is message written by me, for all of you who will believe, and you who refuse to accept the truth behind the reality unfolding before you. \nFor the longest time, we have been waiting. Waiting for answers, yet seeking them aswell. when we do not find an answer, we claim it will come \nfor us soon, only to get tired and drained from the hundred year wait, so we try again. This cycle has continued for long \nenough, and it is time to put it to an end.")

print(" \n \n ")
print ("tnh has encountered a solid calcite guardian. two voidwakers have also decided to join.")
print (" \n ")
target1,itemused1,action1=turn("lasered","3","4","1")
print(target1,action1,itemused1)
print(" \n ")
print("---------------")
print(" \n ")
target2,itemused2,action2=turn("testingjared","1","3","2")
print(target2,action2,itemused2)
print(" \n ")
print("---------------")
print(" \n ")
target3,itemused3,action3=turn("other lasered","4","6","3")
print(target3,action3,itemused3)