with open("Vazifalar/mahsulotlar.txt", "w") as fayl:
    for i in range(5):
        mahsulot = input(f"{i+1}-mahsulotni kiriting: ")
        fayl.write(mahsulot + "\n")

print("\nMahsulotlar ro'yxati:")

with open("Vazifalar/mahsulotlar.txt", "r") as fayl:
    for mahsulot in fayl:
        print(mahsulot.strip())