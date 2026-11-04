jami = 0

with open("Vazifalar/harajatlar.txt", "r") as fayl:
    print("XARAJATLAR HISOBOTI")
    print("-------------------")

    for qator in fayl:
        malumot = qator.split()

        nomi = malumot[0]
        summa = int(malumot[1])

        print(nomi, "-", summa, "so'm")

        jami += summa

print("-------------------")
print("Jami xarajat:", jami, "so'm")