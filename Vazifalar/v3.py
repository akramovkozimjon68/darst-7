ism = input("Yangi ism kiriting: ")

with open("Vazifalar/main1.txt", "a") as fayl:
    fayl.write(ism + "\n")

print("Yangi ism qo'shildi!")