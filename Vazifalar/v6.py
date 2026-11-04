ism = input("Qidirilayotgan ismni kiriting: ")

with open("Vazifalar/main1.txt", "r") as fayl:
    ismlar = fayl.readlines()

if ism + "\n" in ismlar or ism in [x.strip() for x in ismlar]:
    print("Ism topildi")
else:
    print("Ism topilmadi")