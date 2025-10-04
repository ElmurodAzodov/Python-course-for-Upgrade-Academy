A = int(input("A ni kiriting (butun musbat, A>B): "))
B = int(input("B ni kiriting (butun musbat): "))

# Bo'sh qismi hisoblash
while A >= B:        # A dan B ni ayirishni davom ettiramiz
    A -= B           # bu yerda faqat ayirish ishlatiladi

print("Bo'sh qismi:", A)
