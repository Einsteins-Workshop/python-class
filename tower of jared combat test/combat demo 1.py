health1=15
stamina1=10
attunement1=12
health2=15
stamina2=10
attunement2=12
health3=15
stamina3=10
attunement3=12

print("---Lasered---")
print(" ")
print("1-attack")
print("2-abilities")
print("3-items")
print("4-psi")
print("5-skip")
actioncat=input("what would lasered like to do?")
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
    action1=input("what ability will lasered use?")