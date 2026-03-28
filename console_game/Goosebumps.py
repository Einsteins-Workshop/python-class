from PIL import Image

import webbrowser

import numpy

Goosebumps = input("Find witch Goosebumps book you get:")

if Goosebumps == ("Random"):
                num = numpy.random.randint(43)
                num=+1

if Goosebumps.isnumeric():

        # Then print your mad lib using the user input


        if Goosebumps =="1":
            image_path = "Welcome_to_Dead_House_29.png"

        if Goosebumps =="2":
            image_path = "Stay_Out_of_the_Basement_29.png"

        if Goosebumps =="3":
            image_path = "Monster_Blood_29.webp"

        if Goosebumps =="4":
            image_path = "Say_Cheese_and_Die28Cover%29.webp"

        if Goosebumps =="5":
            image_path = "The_Curse_of_the_Mummy28Cover%29.webp"

        if Goosebumps == "6":
                image_path = "Let21_29.webp"
        if Goosebumps == "7":
                image_path = "Night_of_the_Living_Dummy_29.webp"

        if Goosebumps == "8":
                image_path = "The_Girl_Who_Cried_Monster_29.webp"

        if Goosebumps == "9":
                image_path = "Welcome_to_Camp_Nightmare_29.webp"

        if Goosebumps == "10":
                image_path = "The_Ghost_Next_Door_(Cover).webp"

        if Goosebumps == "11":
                image_path = "The_Haunted_Mask_29.webp"

        if Goosebumps == "12":
                image_path = "Be_Careful_What_You_Wish_For..._29.webp"

        if Goosebumps == "13":
                image_path = "Piano_Lessons_Can_Be_Murder_(Cover).webp"

        if Goosebumps == "14":
                image_path = "The_Werewolf_of_Fever_Swamp_29.webp"

        if Goosebumps == "15":
                image_path = "You_Can21_29.webp"

        if Goosebumps == "16":
                image_path = "One_Day_at_HorrorLand_(Cover).webp"

        if Goosebumps == "17":
                image_path = "Why_I28Cover%29.webp"

        if Goosebumps == "18":
                image_path = "Monster_Blood_II_29.webp"

        if Goosebumps == "19":
                image_path = "Deep_Trouble_29.webp"

        if Goosebumps == "20":
                image_path = "The_Scarecrow_Walks_at_Midnight_29.webp"

        if Goosebumps == "21":
                image_path = "Go_Eat_Worms28Cover%29.webp"

        if Goosebumps == "22":
                image_path = "Ghost_Beach_29.webp"

        if Goosebumps == "23":
                image_path = "Return_of_the_Mummy_29.webp"

        if Goosebumps == "23":
                image_path = "Phantom_of_the_Auditorium_29.webp"

        if Goosebumps == "24":
                image_path = "Attack_of_the_Mutant_29.webp"

        if Goosebumps == "25":
                image_path = "My_Hairiest_Adventure_29.webp"

        if Goosebumps == "26":
                image_path = "A_Night_in_Terror_Tower_29.webp"

        if Goosebumps == "27":
                image_path = "The_Cuckoo_Clock_of_Doom_29.webp"

        if Goosebumps == "28":
                image_path = "Monster_Blood_III_29.webp"

        if Goosebumps == "29":
                image_path = "It_Came_from_Beneath_the_Sink28Cover%29.webp"

        if Goosebumps == "30":
                image_path = "Night_of_the_Living_Dummy_II_29.webp"

        if Goosebumps == "31":
                image_path = "The_Barking_Ghost_29.webp"

        if Goosebumps == "32":
                image_path = "The_Horror_at_Camp_Jellyjam_29.webp"

        if Goosebumps == "33":
                image_path = "Revenge_of_the_Lawn_Gnomes_29.webp"

        if Goosebumps == "34":
                image_path = "A_Shocker_on_Shock_Street_29.webp"

        if Goosebumps == "35":
                image_path = "The_Haunted_Mask_II_29.webp"

        if Goosebumps == "36":
                image_path = "The_Headless_Ghost_29.webp"

        if Goosebumps == "37":
                image_path = "The_Abominable_Snowman_of_Pasadena_(Cover).webp"

        if Goosebumps == "38":
                image_path = "How_I_Got_My_Shrunken_Head_29.webp"

        if Goosebumps == "39":
                image_path = "Night_of_the_Living_Dummy_III_29.webp"

        if Goosebumps == "40":
                image_path = "Bad_Hare_Day_29.webp"

        if Goosebumps == "41":
                image_path = "Egg_Monsters_from_Mars_29.webp"

        if Goosebumps == "42":
                image_path = "The_Beast_from_the_East_29.webp"

        if Goosebumps == "43":
                image_path = "Say_Cheese_and_Die28Cover%29.webp"

        if Goosebumps == "44":
                image_path = "Ghost_Camp_29.webp"

        if Goosebumps == "45":
                image_path = "How_to_Kill_a_Monster_29.webp"

        if Goosebumps == "46":
                image_path = "Legend_of_the_Lost_Legend_29.webp"

        if Goosebumps == "47":
                image_path = "Attack_of_the_Jack-O28Cover%29.webp"

        if Goosebumps == "48":
                image_path = "Vampire_Breath_(Cover).webp"

        if Goosebumps == "49":
                image_path = "Calling_All_Creeps28Cover%29.webp"


        image = Image.open(image_path)
        image.show()
