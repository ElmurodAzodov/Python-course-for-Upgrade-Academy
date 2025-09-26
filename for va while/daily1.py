# i = 0
# while i < 5:
#     print(i)
#     i += 1
    
# n = 0
# while n < 5:
#     n += 1
#     if n == 3:
#         continue  # 3 ni tashlab o‘tadi
#     print(n)
# else:
#     print("Sikl tabiiy tugadi")

# secret = 7
# while True:
#     guess = int(input("1-10 orasida son kiriting: "))
#     if guess == secret:
#         print("Topdingiz!")
#         break
#     print("Yana urinib ko‘ring.")

# total = 0
# for i in range(1, 101):
#     if i % 2 == 0:
#         total += i
# print("1-100 orasidagi juft sonlar yig‘indisi:", total)

# while True:
#     print("\nMenyu:\n1. Salom de\n2. Chiqish")
#     tanlov = input("Tanlang: ")
#     if tanlov == "1":
#         print("Salom!")
#     elif tanlov == "2":
#         print("Dastur tugadi.")
#         break
#     else:
#         print("Noto‘g‘ri tanlov!")

# i = 20
# while i >= 0:
#     if i % 2 == 0:         # faqat juft sonlar
#         if i == 10:        # 10 bo‘lsa – tashlab o‘tamiz
#             i -= 2
#             continue
#         print(i)
#     i -= 2                 # har gal 2 ga kamaytirish
summa = 0
son = 0
while son <= 100:
    if son % 2 == 0:
        summa += son
    son += 1
print(summa)
