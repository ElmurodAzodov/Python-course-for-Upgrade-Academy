`range()` — Python’da **ketma-ket butun sonlar** yaratadigan maxsus funksiya.
Uni odatda **for sikli** bilan ishlatamiz, lekin o‘zi ham oddiy obyekt sifatida mavjud.

---

## 🔑 Asosiy ko‘rinish

```python
range(stop)
range(start, stop)
range(start, stop, step)
```

* **start** – boshlanish soni (agar yozilmasa, 0 dan boshlaydi)
* **stop**  – to‘xtash nuqtasi (**shu sondan 1 kichik** gacha ketadi)
* **step**  – qadam (agar yozilmasa, 1)

---

## 1️⃣ Faqat `stop`

```python
for i in range(5):
    print(i)
```

Natija: `0 1 2 3 4`
0 dan 4 gacha bo‘lgan sonlar.

---

## 2️⃣ `start` va `stop`

```python
for i in range(2, 7):
    print(i)
```

Natija: `2 3 4 5 6`
2 dan 6 gacha.

---

## 3️⃣ `start`, `stop`, `step`

```python
for i in range(1, 10, 2):
    print(i)
```

Natija: `1 3 5 7 9`
1 dan 9 gacha, har safar 2 qadam.

---

## 4️⃣ Manfiy qadam

Orqaga sanash ham mumkin:

```python
for i in range(10, 0, -2):
    print(i)
```

Natija: `10 8 6 4 2`

---

## 5️⃣ `list()` bilan ko‘rish

`range` obyektni ro‘yxatga aylantirish:

```python
print(list(range(5)))         # [0, 1, 2, 3, 4]
print(list(range(2, 10, 3)))  # [2, 5, 8]
```

---

## 6️⃣ Foydali xususiyatlar

* **Engil (memory-efficient):** range butun ro‘yxatni saqlamaydi, kerak bo‘lganda sonlarni yaratadi.
* **len()** ishlaydi:

  ```python
  r = range(2, 10, 2)
  print(len(r))  # 4
  ```
* **`in` tekshiruvi**:

  ```python
  print(4 in range(10))  # True
  ```

---

## `for` sikli (loop) — asosiy tushuncha

Python’da **`for`** sikli **ma’lum ketma-ketlikdagi** (list, string, range va boshqalar) elementlarni **birma-bir** olib, har safar siz yozgan kodni bajaradi.

---

### 📌 Umumiy ko‘rinishi

```python
for o‘zgaruvchi in ketma_ketlik:
    # har bir element uchun bajariladigan kod
```

* **`o‘zgaruvchi`** – har gal ketma-ketlikdagi navbatdagi qiymatni oladi.
* **`ketma_ketlik`** – ustida aylanib chiqiladigan to‘plam (list, tuple, string, range …).

---

### 1️⃣ Oddiy misol: 0 dan 4 gacha sonlar

```python
for i in range(5):   # range(5) = 0,1,2,3,4
    print(i)
```

Natija:

```
0
1
2
3
4
```

---

### 2️⃣ Ro‘yxat (list) bilan

```python
mevalar = ["olma", "banan", "gilos"]
for meva in mevalar:
    print(meva)
```

Har bir elementni alohida chop etadi.

---

### 3️⃣ Matn (string) bilan

```python
for harf in "salom":
    print(harf)
```

`s`, `a`, `l`, `o`, `m` harflarini alohida chiqaradi.

---

### 4️⃣ Muhim buyruqlar

| Buyruq     | Vazifasi                                        |
| ---------- | ----------------------------------------------- |
| `break`    | Siklni butunlay to‘xtatadi.                     |
| `continue` | Hozirgi bosqichni o‘tkazib, keyingisiga o‘tadi. |

```python
for i in range(5):
    if i == 2:
        continue   # 2 ni o‘tkazib yuboradi
    if i == 4:
        break      # 4 da siklni to‘xtatadi
    print(i)
```

---

### 5️⃣ Indeks ham kerak bo‘lsa: `enumerate()`

```python
ranglar = ["qizil", "yashil", "ko'k"]
for indeks, rang in enumerate(ranglar):
    print(indeks, rang)
```

---

### Qisqa xulosa

* **`for`** – ma’lum elementlar soni bor bo‘lsa ishlatiladi.
* Har bir elementni avtomatik olib, kodni takrorlaydi.
* `range`, `break`, `continue`, `enumerate` kabi yordamchi vositalar bilan juda qulay.


Python’da **`for`** va **`while`** sikllari (loops) takrorlanuvchi ishlarni bajarish uchun ishlatiladi. Quyida ularni **to‘liq tushuntirish**, asosiy “metodlar” (aniqrog‘i – xususiyatlar va bog‘liq funksiyalar) hamda amaliy **dasturiy misollar** bilan ko‘rib chiqamiz.

---

## 1️⃣ `for` sikli

### Asosiy g‘oya

`for` sikli **iterable** (ro‘yxat, satr, diapazon (`range`) va h.k.) elementlarini birma-bir olib, kod blokini takrorlaydi.

**Sintaksis:**

```python
for o‘zgaruvchi in iterable:
    # takrorlanadigan kod
```

### Muhim tushunchalar

* **`range(start, stop, step)`**: sonlar ketma-ketligini yaratadi.

  * `start` – boshlanish (default 0)
  * `stop` – to‘xtash (to‘xtash nuqtasi kirmaydi)
  * `step` – qadam (default 1)

* **break**: siklni to‘xtatadi.

* **continue**: joriy aylanishni o‘tkazib, keyingisiga o‘tadi.

* **else**: sikl tabiiy tugasa (break bilan emas), `else` bo‘limi bajariladi.

### Oddiy misol

```python
# 1 dan 5 gacha sonlarni chiqarish
for i in range(1, 6):
    print(i)
```

### Ro‘yxat bo‘yicha yurish

```python
fruits = ["olma", "banan", "gilos"]
for f in fruits:
    print(f.upper())  # har bir mevaning bosh harfini katta qiladi
```

### break/continue/else

```python
for x in range(5):
    if x == 3:
        break  # 3 ga yetganda to‘xtaydi
    print(x)
else:
    print("Bu matn faqat break bo‘lmasa chiqariladi")
```

---

## 2️⃣ `while` sikli

### Asosiy g‘oya

`while` sharti **True** bo‘lsa, kod blokini takrorlaydi.

**Sintaksis:**

```python
while shart:
    # takrorlanadigan kod
```

### Muhim elementlar

* **break / continue**: `for` dagidek ishlaydi.
* **else**: shart **False** bo‘lib tugasa bajariladi.

### Oddiy misol

```python
i = 0
while i < 5:
    print(i)
    i += 1   # cheksiz sikldan qochish uchun
```

### break/continue/else

```python
n = 0
while n < 5:
    n += 1
    if n == 3:
        continue  # 3 ni tashlab o‘tadi
    print(n)
else:
    print("Sikl tabiiy tugadi")
```

---

## 3️⃣ Amaliy dasturiy misollar

### Misol 1: Foydalanuvchi topmaguncha son so‘rash (`while`)

```python
secret = 7
while True:
    guess = int(input("1-10 orasida son kiriting: "))
    if guess == secret:
        print("Topdingiz!")
        break
    print("Yana urinib ko‘ring.")
```

### Misol 2: Juft sonlarni yig‘indisi (`for`)

```python
total = 0
for i in range(1, 101):
    if i % 2 == 0:
        total += i
print("1-100 orasidagi juft sonlar yig‘indisi:", total)
```

### Misol 3: Menyu bilan dastur (`while`)

```python
while True:
    print("\nMenyu:\n1. Salom de\n2. Chiqish")
    tanlov = input("Tanlang: ")
    if tanlov == "1":
        print("Salom!")
    elif tanlov == "2":
        print("Dastur tugadi.")
        break
    else:
        print("Noto‘g‘ri tanlov!")
```

---

## Xulosa

* **`for`** – elementlar ketma-ketligi bo‘yicha yurish uchun qulay.
* **`while`** – shartga asoslangan takrorlash uchun mos.
* Har ikkalasida ham `break`, `continue`, `else` ishlaydi.
* Infinite (cheksiz) siklni oldini olish uchun `while` da shartni yangilab borish zarur.
