import sys
from termcolor import  colored

alignmentdict= {
    "1": "superstructure- aligned",
    "2": "catastrophe- surviving",
    "3": "void- resurrected"
}
magicdict= {
    "1": "the void",
    "2": "corruption",
    "3": "the fallen sun",
    "4": "the opalescent",
    "5": "telepathy",
    "6": "gravity"
}
classdict= {
    "1": "fighter",
    "2": "ranger",
    "3": "alchemist",
    "4": "assassin",
    "5": "scavenger",
}


name1 = input("What is the name of your first character?")
color1 = input("Great. now, what color are they?")
print("-----------")
print("1-Superstructure")
print("2-survivors")
print("3-fallen")
align1 = input(f"please select an alignment for {name1}. This will have a minor effect on gameplay.")
print("-----------")
print("1-fighter")
print("2-ranger")
print("3-Alchemist")
print("4-assassin")
print("5-scavenger")
class1 = input(f"please select a class for {name1}. This will have a major effect on gameplay.")
print("-----------")
print("1-void")
print("2-corruption")
print("3-fallen sun")
print("4-opalescent")
print("5-telepathy")
print("6-gravity")
magic1 = input(f"please select a psychic attunement for {name1}. This will have a major effect on gameplay.")

print(" ")

name2 = input("What is the name of your second character?")
color2 = input("Great. now, what color are they?")
print("-----------")
print("1-Superstructure")
print("2-survivors")
print("3-fallen")
align2 = input(f"please select an alignment for {name2}. This will have a minor effect on gameplay.")
print("-----------")
print("1-fighter")
print("2-ranger")
print("3-Alchemist")
print("4-assassin")
print("5-noble")
class2 = input(f"please select a class for {name2}. This will have a major effect on gameplay.")
print("-----------")
print("1-void")
print("2-corruption")
print("3-fallen sun")
print("4-opalescent")
print("5-telepathy")
print("6-gravity")
magic2 = input(f"please select a psychic attunement for {name2}. This will have a major effect on gameplay.")

print(" ")

name3 = input("What is the name of your third character?")
color3 = input("Great. now, what color are they?")
print("-----------")
print("1-Superstructure")
print("2-survivors")
print("3-fallen")
align3 = input(f"please select an alignment for {name3}. This will have a minor effect on gameplay.")
print("-----------")
print("1-fighter")
print("2-ranger")
print("3-Alchemist")
print("4-assassin")
print("5-noble")
class3 = input(f"please select a class for {name3}. This will have a major effect on gameplay.")
print("-----------")
print("1-void")
print("2-corruption")
print("3-fallen sun")
print("4-opalescent")
print("5-telepathy")
print("6-gravity")
magic3 = input(f"please select a psychic attunement for {name3}. This will have a major effect on gameplay.")

print(" \n \n \n ")

print(f"--------{name1}--------")

print((alignmentdict[align1]), (classdict[class1]),"attuned to the school of", (magicdict[magic1]))
print(" ")
print(f"--------{name2}--------")

print((alignmentdict[align2]), (classdict[class2]),"attuned to the school of", (magicdict[magic2]))
print(" ")
print(f"--------{name3}--------")

print((alignmentdict[align3]), (classdict[class3]),"attuned to the school of", (magicdict[magic3]))
print(" ")