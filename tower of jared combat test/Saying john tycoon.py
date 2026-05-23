import json
money=0
johnpc=1
johnpc2=1
johnstones=0
stonepu=1
autojohns=0
level=0
while True:
    print("🪙",money)
    print("⬆️", level)
    print("💎",johnstones)
    print("John power",(johnpc*johnpc2)+level)
    money=money+autojohns
    action=input("Say \"John\" for money. \nSay \"Shop\" to access the shop.\nSay \"Save\" to save.\nSay \"Load\" to load.")
    if action.lower()==("john"):
        money=money+(johnpc*johnpc2)+level
    if action.lower()==("shop"):
        print("1- ⒿStronger johns: 🪙",johnpc*5)
        print("2- ⒿWAAAY Stronger johns: 🪙", johnpc2 * 25)
        print("2- ⬆️Level up: 🪙", level+1 * 100)
        print("4- 💎Shinier stones: 💎",stonepu*5 )
        print("5- ⒿAutojohn 200000000: 💎", autojohns * 25)
        choice=input("what would you like to buy?")
        if choice==("1") and money>johnpc*5-1:
            money=money-johnpc*5
            johnpc=johnpc+1
            johnstones=johnstones+1
        if choice == ("2") and money > johnpc2 * 25 - 1:
            money = money - johnpc2 * 25
            johnpc2 = johnpc2 + 1
            johnstones = johnstones + 1
        if choice == ("3") and money > level * 100 - 1:
            money = 0
            level = level + 1
            johnpc=1
            johnpc2=1
            johnstones = johnstones + 1
        if choice == ("4") and johnstones > stonepu * 5 - 1:
            johnstones = johnstones - stonepu * 5
            stonepu = stonepu + 1
        if choice == ("4") and johnstones > autojohns+1 * 5 - 1:
            johnstones = johnstones - autojohns+1 * 5
            autojohns = autojohns + 1
    if action==("just give me my money already"):
        money=100000
        level=100
        johnpc=100
        johnpc2=5
        autojohns=50
        johnstones=1000
    if action.lower()==("save"):
        savedata = {
            "level": level,
            "money": money,
            "johnstones": johnstones,
        }
        savedatajson = json.dumps(savedata)
        with open("save.johnsave","w") as johnsave:
            johnsave.write(savedatajson)
        print (savedatajson)
        print ("saved game!")
    if action.lower() == ("load"):
        with open("save.johnsave") as johnsave:
            savedatajson=johnsave.readline()
            savedata=json.loads(savedatajson)
        print (savedata)
        print ("loaded game!")
        level=savedata["level"]
        money=savedata["money"]
        johnstones=savedata["johnstones"]