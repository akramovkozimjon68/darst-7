with open("Vazifalar/sonlar.txt", "r") as fayl:
    sonlar = fayl.readlines()

with open("Vazifalar/juft_sonlar.txt", "w") as fayl:
    for son in sonlar:
        son = int(son.strip())

        if son % 2 == 0:
            fayl.write(str(son) + "\n")

print("Juft sonlar juft_sonlar.txt fayliga yozildi!")