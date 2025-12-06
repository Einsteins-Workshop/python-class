from PIL import Image

import webbrowser

import numpy

Mariokart8_Character_want = input("Type stuff to find Mario things or enter number 1-44 for a mariokart 8 character:")

if Mariokart8_Character_want == ("Random"):
                num = numpy.random.randint(43)
                num=+1

if Mariokart8_Character_want.isnumeric():

        # Then print your mad lib using the user input
        print("Your Character is")

        if int(Mariokart8_Character_want)>44:
            image_path = "ddah5ao-4e201ced-8e18-4d59-81c9-c8742fc05d19.png"

        if int(Mariokart8_Character_want) < 1:
                image_path = "ddah5ao-4e201ced-8e18-4d59-81c9-c8742fc05d19.png"

        if Mariokart8_Character_want =="1":
            image_path = "70px-MK8_Mario_Icon.png"

        if Mariokart8_Character_want =="2":
            image_path = "70px-MK8_Luigi_Icon.png"

        if Mariokart8_Character_want =="3":
            image_path = "70px-MK8_Peach_Icon.png"

        if Mariokart8_Character_want =="4":
            image_path = "70px-MK8_Daisy_Icon.png"

        if Mariokart8_Character_want =="5":
            image_path = "70px-MK8_Rosalina_Icon.png"

        if Mariokart8_Character_want == "6":
                image_path = "70px-MK8_Tanooki_Mario_Icon.png"

        if Mariokart8_Character_want == "7":
                image_path = "70px-MK8_Cat_Peach_Icon.png"

        if Mariokart8_Character_want == "8":
                image_path = "70px-MK8_Yoshi_Icon.png"

        if Mariokart8_Character_want == "9":
                image_path = "70px-MK8_Toad_Icon.png"

        if Mariokart8_Character_want == "10":
                image_path = "70px-MK8_Koopa_Icon.png"

        if Mariokart8_Character_want == "11":
                image_path = "70px-MK8_ShyGuy_Icon.png"

        if Mariokart8_Character_want == "12":
                image_path = "70px-MK8_Lakitu_Icon.png"

        if Mariokart8_Character_want == "13":
                image_path = "70px-MK8_Toadette_Icon.png"

        if Mariokart8_Character_want == "14":
                image_path = "70px-MK8DX_King_Boo_Icon.png"

        if Mariokart8_Character_want == "15":
                image_path = "70px-MK8_BabyMario_Icon.png"

        if Mariokart8_Character_want == "16":
                image_path = "70px-MK8_BabyLuigi_Icon.png"

        if Mariokart8_Character_want == "17":
                image_path = "70px-MK8_BabyPeach_Icon.png"

        if Mariokart8_Character_want == "18":
                image_path = "70px-MK8_BabyDaisy_Icon.png"

        if Mariokart8_Character_want == "19":
                image_path = "70px-MK8_BabyRosalina_Icon.png"

        if Mariokart8_Character_want == "20":
                image_path = "70px-MK8_MMario_Icon.png"

        if Mariokart8_Character_want == "21":
                image_path = "70px-MK8_PGPeach_Icon.png"

        if Mariokart8_Character_want == "22":
                image_path = "70px-MK8_Wario_Icon.png"

        if Mariokart8_Character_want == "23":
                image_path = "70px-MK8_Waluigi_Icon.png"

        if Mariokart8_Character_want == "23":
                image_path = "70px-MK8_DKong_Icon.png"

        if Mariokart8_Character_want == "23":
                image_path = "70px-MK8_Bowser_Icon.png"

        if Mariokart8_Character_want == "24":
                image_path = "70px-MK8DX_Dry_Bones_Icon.png"

        if Mariokart8_Character_want == "25":
                image_path = "70px-MK8_Bowser_Jr_Icon.png"

        if Mariokart8_Character_want == "26":
                image_path = "70px-MK8_Dry_Bowser_Icon.png"

        if Mariokart8_Character_want == "27":
                image_path = "70px-MK8_Lemmy_Icon.png"

        if Mariokart8_Character_want == "28":
                image_path = "70px-MK8_Larry_Icon.png"

        if Mariokart8_Character_want == "29":
                image_path = "70px-MK8_Wendy_Icon.png"

        if Mariokart8_Character_want == "30":
                image_path = "70px-MK8_Ludwig_Icon.png"

        if Mariokart8_Character_want == "31":
                image_path = "70px-MK8_Iggy_Icon.png"

        if Mariokart8_Character_want == "32":
                image_path = "70px-MK8_Roy_Icon.png"

        if Mariokart8_Character_want == "33":
                image_path = "70px-MK8_Morton_Icon.png"

        if Mariokart8_Character_want == "34":
                image_path = "70px-MK8DX_Female_Inkling_Icon.png"

        if Mariokart8_Character_want == "35":
                image_path = "70px-VillagerMale-Icon-MK8.png"

        if Mariokart8_Character_want == "36":
                image_path = "70px-MK8_Isabelle_Icon.png"

        if Mariokart8_Character_want == "37":
                image_path = "70px-MK8D_BotW_Link_Icon.png"

        if Mariokart8_Character_want == "38":
                image_path = "70px-MK8D_Birdo_Icon.png"

        if Mariokart8_Character_want == "39":
                image_path = "70px-MK8DX_Petey_Piranha_Icon.png"

        if Mariokart8_Character_want == "40":
                image_path = "70px-MK8DX_Kamek_Icon.png"

        if Mariokart8_Character_want == "41":
                image_path = "70px-MK8DX_Pauline_Icon.png"

        if Mariokart8_Character_want == "42":
                image_path = "70px-MK8DX_Peachette_Icon.png"

        if Mariokart8_Character_want == "43":
                image_path = "70px-MK8DX_Diddy_Kong_Icon.png"

        if Mariokart8_Character_want == "44":
                image_path = "70px-MK8DX_Funky_Kong_Icon.png"

        image = Image.open(image_path)
        image.show()

else:
        if Mariokart8_Character_want ==("SuperMarioFanGame"):
                 Google_path = "https://scratch.mit.edu/projects/216123417"

        elif Mariokart8_Character_want == ("MarioFacts"):
                 Google_path = "https://www.youtube.com/switchstop"

        elif Mariokart8_Character_want == ("MarioNews"):
                Google_path = "https://mario.nintendo.com/news/"

        elif Mariokart8_Character_want == ("MarioTier"):
                Google_path = "https://tiermaker.com/categories/mario"

        elif Mariokart8_Character_want == ("MarioKahoot"):
                Google_path = "https://create.kahoot.it/details/super-mario-bros/83a5d10e-b23e-470a-899b-62c7c8e1089c"

        elif Mariokart8_Character_want == ("MarioOldGame"):
                Google_path = "https://scratch.mit.edu/projects/196684240"

        elif Mariokart8_Character_want == ("MarioLevelUpGame"):
                Google_path = "https://bookwormkevin.itch.io/lummm"

        elif Mariokart8_Character_want == ("IHateYou"):
                Google_path = "https://www.youtube.com/watch?v=jDwVkXVHIqg"
                print ("https://www.youtube.com/watch?v=jDwVkXVHIqg")

        elif Mariokart8_Character_want == ("ShopForMario"):
                Google_path = "https://www.nintendo.com/us/store/?srsltid=AfmBOopDzWyI6mYVKKO4lXNtetExhiEmpAZAcRUp-ytLdmX3GgHiXZa_"

        elif Mariokart8_Character_want == ("FunMario"):
                Google_path = "https://www.youtube.com/channel/UCNK813T2BNBwcfDPDTPeMPA"

webbrowser.open(Google_path)