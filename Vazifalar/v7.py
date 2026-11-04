with open("Vazifalar/main1.txt", "r") as fayl:
    matn = fayl.read()

sozlar = matn.split()

if sozlar:
    eng_uzun = max(sozlar, key=len)
    print("Eng uzun so'z:", eng_uzun)
    print("Uzunligi:", len(eng_uzun))
else:
    print("Faylda so'z mavjud emas!")