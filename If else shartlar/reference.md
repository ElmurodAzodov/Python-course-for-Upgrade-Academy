
## 1. If/else nima?

👉 `if/else` — bu **shartli operator**. U kodni ma’lum **shart bajarilganda** yoki **bajarilmaganda** turlicha yo‘nalishda ishlashiga imkon beradi.

Soddaroq qilib aytganda:

* `if` → “Agar shart to‘g‘ri bo‘lsa, bu kodni bajar.”
* `else` → “Agar shart noto‘g‘ri bo‘lsa, boshqa kodni bajar.”
* `elif` → “Agar oldingi shartlar noto‘g‘ri bo‘lsa, lekin bu shart to‘g‘ri bo‘lsa, shu kodni bajar.”

---

## 2. Asosiy sintaksis (tuzilishi)

```python
if shart:
    # Agar shart True bo‘lsa, shu qism bajariladi
else:
    # Agar shart False bo‘lsa, shu qism bajariladi
```

### Misol 1:

```python
yosh = 20

if yosh >= 18:
    print("Siz voyaga yetgansiz.")
else:
    print("Siz voyaga yetmagansiz.")
```

✅ Natija: `Siz voyaga yetgansiz.`

---

## 3. `elif` (else if)

Bir nechta shartlarni ketma-ket tekshirish uchun ishlatiladi.

```python
if shart1:
    # birinchi shart to‘g‘ri bo‘lsa
elif shart2:
    # agar birinchi noto‘g‘ri, ammo ikkinchi to‘g‘ri bo‘lsa
else:
    # hammasi noto‘g‘ri bo‘lsa
```

### Misol 2:

```python
ball = 75

if ball >= 90:
    print("A’lo")
elif ball >= 70:
    print("Yaxshi")
elif ball >= 50:
    print("Qoniqarli")
else:
    print("Qoniqarsiz")
```

✅ Natija: `Yaxshi`

---

## 4. If ichida if (nested if)

Shart ichida yana shart yozish mumkin.

```python
login = "admin"
parol = "1234"

if login == "admin":
    if parol == "1234":
        print("Kirish muvaffaqiyatli!")
    else:
        print("Parol xato!")
else:
    print("Login topilmadi!")
```

✅ Natija: `Kirish muvaffaqiyatli!`

---

## 5. If’ni qisqa yozish (Ternary operator)

Bitta qatorda `if/else` yozish mumkin.

```python
yosh = 16
status = "Voyaga yetgan" if yosh >= 18 else "Voyaga yetmagan"
print(status)
```

✅ Natija: `Voyaga yetmagan`

---

## 6. Bir nechta shartlarni tekshirish (and / or / not)

* **and** → hammasi to‘g‘ri bo‘lishi kerak.
* **or** → bittasi bo‘lsa ham to‘g‘ri bo‘lishi yetarli.
* **not** → shartni teskarisiga o‘zgartiradi.

### Misol 3:

```python
yosh = 25
fuqaro = True

if yosh >= 18 and fuqaro:
    print("Saylovda ovoz berishingiz mumkin.")
else:
    print("Sizga ruxsat berilmaydi.")
```

### Misol 4:

```python
kun = "shanba"

if kun == "shanba" or kun == "yakshanba":
    print("Bugun dam olish kuni.")
else:
    print("Bugun ish kuni.")
```

---

## 7. Amaliy mini-misol (Kalkulyator)

```python
a = int(input("Birinchi sonni kiriting: "))
b = int(input("Ikkinchi sonni kiriting: "))
amal = input("Amalni kiriting (+, -, *, /): ")

if amal == "+":
    print("Natija:", a + b)
elif amal == "-":
    print("Natija:", a - b)
elif amal == "*":
    print("Natija:", a * b)
elif amal == "/":
    if b != 0:
        print("Natija:", a / b)
    else:
        print("0 ga bo‘lish mumkin emas!")
else:
    print("Noto‘g‘ri amal tanlandi.")
```

---

## Xulosa:

* `if` → shartni tekshiradi.
* `elif` → qo‘shimcha shartlar uchun.
* `else` → qolgan barcha holatlar uchun.
* `and`, `or`, `not` → murakkab shartlarni yozishda.
* Qisqa yozilishi: `Agar shart to‘g‘ri bo‘lsa qiymat1 else qiymat2`.

---