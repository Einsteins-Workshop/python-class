def Mage_Mage():
    Mage_powers = {
        "Arcane energy level": 10,
        "Elemental forces level": 10,
        "reality-altering spells level": 10,
        "Defense level": 6
    }
    print("As a Mage your powers are:")
    print( Mage_powers)
def Dark_Mage():
    Dark_Mage_powers = {
        "Necromancy level": 10,
        "Shadow & Chaos Magic level": 10,
        "Curses level": 10,
        "Summoning level": 10
    }
    print("As a Dark Mage your powers are:")
    print(Dark_Mage_powers)
def Healer_Healer():
    Healer_powers = {
        "Resurrection level": 10,
        "Physical Healing level": 10,
        "Combat level": 6
    }
    print("As a Healer your powers are:")
    print(Healer_powers)
def Assassin_Assassin():
    Assassin_powers = {
        "Martial arts level": 10,
        "Poison Mastery level": 10,
        "Stealth level": 10,
        "Teleportation level": 10,
        "Cloaking level": 10
    }
    print("As a Assassin your powers are:")
    print(Assassin_powers)
def Knight_Knight():
    Knight_powers = {
        "Combat level": 10,
        "Combat Spells level": 10,
        "Traversal abilities level": 10
    }
    print("As a Knight your powers are:")
    print(Knight_powers)
def Dark_Knight():
    Dark_Mage_powers = {
        "Dark magic level": 10,
        "Necrotic damage level": 10,
        "Command/summon the undead level": 10
    }
    print("As a Dark Knight your powers are:")
    print(Dark_Mage_powers)

print("Hi, this game is going to be a where you are lost and are trying to find your way.")
print("You can carry objects and other thing. Your powers are ranked by number.")
name = input("What do you want your name to be here: ")
print("   ")
print("   ")

Starting_powers = {
    "Magic level": 1,
    "Attack level": 1,
    "Defense level": 1
}

print("Your starting powers are:")
print(Starting_powers)

print("Ok so you are can pick a class. Please spell thing the same way as shown")
class_power = input("You can be a Mage, a dark Mage, Healer, a Knight, a Dark Knight or a Assassin: ")
if (class_power == "Mage"):
    Mage_Mage()

if (class_power == "Dark Mage"):
    Dark_Mage()

if (class_power == "Healer"):
    Healer_Healer()

if (class_power == "Assassin"):
    Assassin_Assassin()

if (class_power == "Knight"):
    Knight_Knight()

if (class_power == "Dark Knight"):
    Dark_Knight()

# Next time add a places and stuff like that or maybe a job
# Make monsters or stuff