# 1-topshiriq. Ismni teskari yozing
ism = input("Ismingizni kiriting: ")
print("Teskari:", ism[::-1])

# 2-topshiriq. Harflar sonini hisoblang
matn = input("\nMatn kiriting (2-topshiriq): ")
harflar_soni = len(matn.replace(" ", ""))
print("Bo‘sh joylarsiz harflar soni:", harflar_soni)

# 3-topshiriq. Gapdagi so‘zlar soni
gap = input("\nMatn kiriting (3-topshiriq): ")
sozlar_soni = len(gap.split())
print("So‘zlar soni:", sozlar_soni)

# 4-topshiriq. Belgilarni almashtiring
matn2 = input("\nMatn kiriting (4-topshiriq): ")
yangi_matn = matn2.replace('a', 'o')
print("Almashtirilgan matn:", yangi_matn)

# 5-topshiriq. Teskari tartibda chiqarish, lekin so‘z joyi o‘zgarmasin
matn3 = input("\nMatn kiriting (5-topshiriq): ")
teskari_sozlar = [soz[::-1] for soz in matn3.split()]
natija = " ".join(teskari_sozlar)
print("Natija:", natija)

# 6-topshiriq. Katta va kichik harflar
matn4 = input("\nMatn kiriting (6-topshiriq): ")
print("Katta harflarda:", matn4.upper())
print("Kichik harflarda:", matn4.lower())
print("Har bir so‘z bosh harf bilan:", matn4.title())

# 7-topshiriq. Belgilarni sanash
matn5 = input("\nMatn kiriting (7-topshiriq): ")
print("'a' harfi soni:", matn5.count('a'))

# 8-topshiriq. Matnni tozalash
matn6 = input('\nMatn kiriting (8-topshiriq, masalan: "  Python  "): ')
print("Tozalangan matn:", matn6.strip())

# 9-topshiriq. So‘zlarni bog‘lash
soz1 = input("\n1-so‘zni kiriting: ")
soz2 = input("2-so‘zni kiriting: ")
soz3 = input("3-so‘zni kiriting: ")
birlashtirilgan = "-".join([soz1, soz2, soz3])
print("Natija:", birlashtirilgan)

# 10-topshiriq. Belgilar indeksini topish
matn7 = input("\nMatn kiriting (10-topshiriq): ")
belgi = input("Qaysi belgini qidiramiz? ")
indeks = matn7.find(belgi)
if indeks != -1:
    print(f"'{belgi}' belgisi birinchi marta {indeks}-indeksta uchradi.")
else:
    print(f"'{belgi}' belgisi matnda topilmadi.")
