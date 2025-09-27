from PIL import Image

Mariokart8_Character_want = input("Enter number 1-42:")

# Then print your mad lib using the user input
print("Your Character is")

if int(Mariokart8_Character_want)>42:
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

image = Image.open(image_path)
image.show()