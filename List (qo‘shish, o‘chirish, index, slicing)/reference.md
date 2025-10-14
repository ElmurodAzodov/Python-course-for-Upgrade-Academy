## 🧩 1-BO‘LIM: **KIRISH – Python’da List (Ro‘yxat) nima?**

---

### 🟢 **1. List nima?**

**List (ro‘yxat)** — bu Python’dagi **eng ko‘p ishlatiladigan ma’lumot turi** bo‘lib, **bir nechta qiymatlarni bitta o‘zgaruvchida saqlash** imkonini beradi.
List — **tartiblangan (ordered)**, **o‘zgartiriladigan (mutable)** va **takrorlanuvchi elementlarni** saqlashi mumkin bo‘lgan **ma’lumotlar tuzilmasi**.

```python
mevalar = ["olma", "banan", "anor", "gilos"]
print(mevalar)
# Natija: ['olma', 'banan', 'anor', 'gilos']
```

---

### 🟣 **2. Listning asosiy xususiyatlari**

| Xususiyat                        | Tushuntirish                                          | Misol                      |
| -------------------------------- | ----------------------------------------------------- | -------------------------- |
| **Tartiblangan**                 | Elementlar ketma-ketligi saqlanadi (indeks asosida)   | `["a", "b", "c"][0] → "a"` |
| **O‘zgartiriladigan (mutable)**  | Elementlarni o‘zgartirish, qo‘shish, o‘chirish mumkin | `mevalar[1] = "shaftoli"`  |
| **Takrorlanishga ruxsat beradi** | Bir xil qiymatlar bir necha marta bo‘lishi mumkin     | `[1, 2, 2, 3]`             |
| **Turli turlarni saqlay oladi**  | Har xil ma’lumot turlari bir ro‘yxatda                | `[1, "matn", True, 3.14]`  |

---

### 🟠 **3. Listning ichki tuzilishi (qisqacha texnik)**

Python’da **list — bu dinamik massiv**. Ya’ni, u elementlar soniga qarab **avtomatik kengayadi yoki qisqaradi**.
Listdagi elementlar **obyektlarga ishora (reference)** ko‘rinishida saqlanadi.

Misol:

```python
a = [1, 2, 3]
b = a
b[0] = 99
print(a)  # [99, 2, 3] — ikkisi bir xotira manzilga qaragan!
```

✅ Agar mustaqil nusxa kerak bo‘lsa:

```python
import copy
b = copy.deepcopy(a)
```

---

### 🔵 **4. List va boshqa ma’lumot turlari farqi**

| Ma’lumot turi  | Tartib             | O‘zgartiriladi | Takrorlanishga ruxsat | Kalit-qiymat juftligi | Misol            |
| -------------- | ------------------ | -------------- | --------------------- | --------------------- | ---------------- |
| **List**       | ✅                  | ✅              | ✅                     | ❌                     | `[1, 2, 3]`      |
| **Tuple**      | ✅                  | ❌              | ✅                     | ❌                     | `(1, 2, 3)`      |
| **Set**        | ❌                  | ✅              | ❌                     | ❌                     | `{1, 2, 3}`      |
| **Dictionary** | ✅ (kalit bo‘yicha) | ✅              | Kalit unikal          | ✅                     | `{"ism": "Ali"}` |

**Xulosa:**

* Ma’lumotlar tartibi kerak bo‘lsa — `list` yoki `tuple`.
* Takrorlanmas elementlar kerak bo‘lsa — `set`.
* Kalit-qiymat juftligi kerak bo‘lsa — `dict`.

---

### 🧠 **5. Listdan foydalanishning amaliy holatlari**

**Ro‘yxatlar** quyidagi holatlarda juda qulay:

* Foydalanuvchi kiritgan ma’lumotlarni saqlash;
* Fayldan o‘qilgan qatorlarni yig‘ish;
* Hisob-kitob yoki filtratsiya uchun ma’lumotlar to‘plamini saqlash;
* Dasturdagi vaqtinchalik massiv sifatida.

**Misol:**

```python
talabalar = []
n = int(input("Nechta talaba ismini kiritasiz? "))

for i in range(n):
    ism = input(f"{i+1}-talaba ismini kiriting: ")
    talabalar.append(ism)

print("Talabalar ro‘yxati:", talabalar)
```

**Namuna chiqish:**

```
Nechta talaba ismini kiritasiz? 3
1-talaba ismini kiriting: Ali
2-talaba ismini kiriting: Laylo
3-talaba ismini kiriting: Bobur
Talabalar ro‘yxati: ['Ali', 'Laylo', 'Bobur']
```

---

### 🧩 **6. Ehtimoliy xatolik holatlari**

1. **Indeksdan tashqariga murojaat:**

   ```python
   mevalar = ["olma", "banan"]
   print(mevalar[3])  # ❌ IndexError
   ```

2. **Bo‘sh list ustida o‘chirish:**

   ```python
   mevalar = []
   mevalar.pop()  # ❌ IndexError: pop from empty list
   ```

3. **Listni nusxalashda havola muammosi:**

   ```python
   a = [1, 2, 3]
   b = a  # Boshqa nom, lekin bir xil manzil
   b.append(4)
   print(a)  # [1, 2, 3, 4]
   ```

---

### 🏁 **Xulosa:**

* List — Python’dagi **eng muhim va moslashuvchan** ma’lumot turi.
* U **tartibga ega**, **o‘zgartiriladi**, **takrorlanuvchi qiymatlarni** saqlaydi.
* Ro‘yxatlar bilan ishlashda **indeks**, **mutability**, va **nusxalashdagi farqlar** muhim.

---

---

## 🧩 2-BO‘LIM: **Python’da List yaratish**

---

### 🟢 **1. Bo‘sh list yaratish**

Python’da bo‘sh ro‘yxat yaratishning ikki usuli bor:

#### 🧱 Usul 1: Kvadrat qavslar yordamida

```python
my_list = []
print(my_list)  # []
print(type(my_list))  # <class 'list'>
```

#### 🧱 Usul 2: `list()` funksiyasi yordamida

```python
my_list = list()
print(my_list)  # []
```

✅ **Qachon ishlatiladi?**

* Agar keyinchalik `append()` yordamida elementlar qo‘shmoqchi bo‘lsangiz.
* Dinamik ma’lumotlar (masalan, foydalanuvchi kiritgan ma’lumotlar) uchun.

---

### 🟣 **2. Elementlar bilan list yaratish**

List yaratishda elementlarni **kvadrat qavs ichiga** vergul orqali yozamiz:

```python
sonlar = [10, 20, 30, 40]
mevalar = ["olma", "anor", "banan"]
aralash = [1, "matn", 3.14, True]

print(sonlar)
print(mevalar)
print(aralash)
```

**Natija:**

```
[10, 20, 30, 40]
['olma', 'anor', 'banan']
[1, 'matn', 3.14, True]
```

✅ **Qachon ishlatiladi?**

* Dasturda ma’lum qiymatlar oldindan ma’lum bo‘lsa (statik ma’lumotlar).

---

### 🟠 **3. `list()` funksiyasi yordamida boshqa turlardan list yaratish**

`list()` funksiyasi **iterable (takrorlanadigan)** obyektlardan list yaratadi.

#### 📘 Misollar:

```python
# Stringdan list
matn = "salom"
harflar = list(matn)
print(harflar)  # ['s', 'a', 'l', 'o', 'm']

# Tupledan list
tuple_data = (1, 2, 3)
list_data = list(tuple_data)
print(list_data)  # [1, 2, 3]

# Setdan list
my_set = {10, 20, 30}
my_list = list(my_set)
print(my_list)  # [10, 20, 30] (Tartib saqlanmaydi!)
```

⚠️ **Eslatma:** Set tartibsiz, shuning uchun `list()` bilan aylantirganda elementlarning tartibi o‘zgarishi mumkin.

---

### 🔵 **4. Ichma-ich list yaratish (Nested list)**

List ichida yana list bo‘lishi mumkin. Bular **2D (ikki o‘lchovli) listlar** deyiladi.

```python
matritsa = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

print(matritsa[0])     # [1, 2, 3]
print(matritsa[1][2])  # 6
```

✅ **Qachon ishlatiladi?**

* Jadval (table), matritsa, reyting, koordinata kabi ma’lumotlarni saqlashda.

---

### 🔴 **5. Bo‘sh listga element qo‘shish – `append()` metodi**

`append()` — ro‘yxatning oxiriga **bitta element qo‘shadi**.

```python
mevalar = []
mevalar.append("olma")
mevalar.append("banan")
print(mevalar)
```

**Natija:**

```
['olma', 'banan']
```

---

### 🟢 **6. Ro‘yxatni foydalanuvchi kiritgan ma’lumotlar bilan yaratish**

Misol: foydalanuvchidan 5 ta son kiritib, listga joylash:

```python
sonlar = []
for i in range(5):
    son = int(input(f"{i+1}-sonni kiriting: "))
    sonlar.append(son)

print("Siz kiritgan sonlar:", sonlar)
```

---

### 🧠 **7. Ehtimoliy xatolik holatlari**

1. **Bo‘sh listga to‘g‘ridan-to‘g‘ri indeks bilan murojaat:**

   ```python
   lst = []
   lst[0] = 10  # ❌ IndexError
   ```

   ✅ To‘g‘risi:

   ```python
   lst.append(10)
   ```

2. **Setdan yaratilgan list tartibsiz bo‘lishi:**

   ```python
   my_set = {1, 2, 3, 4}
   print(list(my_set))  # Har safar tartib o‘zgarishi mumkin
   ```

---

### 🏁 **Xulosa:**

| Yaratish usuli      | Sintaksis             | Tavsif                                     |
| ------------------- | --------------------- | ------------------------------------------ |
| Kvadrat qavs        | `my_list = [1, 2, 3]` | Eng keng tarqalgan usul                    |
| `list()` funksiyasi | `list("abc")`         | Boshqa iterable obyektlardan list yaratadi |
| Bo‘sh list          | `[]` yoki `list()`    | Keyinchalik to‘ldirish uchun ishlatiladi   |
| Ichma-ich list      | `[[1,2],[3,4]]`       | Jadval yoki matritsalar uchun              |

---

---

## 🧩 3-BO‘LIM: **List elementlariga murojaat qilish**

---

### 🟢 **1. Indeks orqali murojaat qilish**

List elementlariga **indeks** (ya’ni tartib raqami) orqali murojaat qilinadi.
Indekslash **0 dan boshlanadi.**

```python
mevalar = ["olma", "banan", "anor", "gilos"]

print(mevalar[0])  # 1-element: olma
print(mevalar[2])  # 3-element: anor
```

---

### 🔵 **2. Manfiy indekslar (negative indexing)**

Python’da manfiy indekslar **ro‘yxat oxiridan** hisoblanadi:

* `-1` → oxirgi element
* `-2` → oxiridan oldingi element

```python
mevalar = ["olma", "banan", "anor", "gilos"]
print(mevalar[-1])  # gilos
print(mevalar[-2])  # anor
```

✅ Foydali holatlar:

* Oxirgi elementni olish (`list[-1]`)
* Oxirdan boshlab tahlil qilish

---

### 🟣 **3. Slicing (kesish) – listdan bo‘lak olish**

**Slicing** yordamida listdan bir qismini ajratib olish mumkin:
`sintaksis: list[start:end:step]`

* `start` – boshlanish indeksi (kiritiladi)
* `end` – tugash indeksi (kiritilmaydi)
* `step` – qadam (ixtiyoriy)

```python
sonlar = [10, 20, 30, 40, 50, 60]

print(sonlar[1:4])   # [20, 30, 40]
print(sonlar[:3])    # [10, 20, 30]
print(sonlar[3:])    # [40, 50, 60]
print(sonlar[::2])   # [10, 30, 50]
print(sonlar[::-1])  # [60, 50, 40, 30, 20, 10] – teskari tartib
```

⚠️ **Eslatma:**
Indeks diapazoni tashqarida bo‘lsa, Python xato bermaydi – mavjud qismini qaytaradi.

---

### 🟠 **4. Elementni o‘zgartirish**

List o‘zgartiriladigan (mutable) tur, shuning uchun element qiymatini bemalol almashtirish mumkin:

```python
mevalar = ["olma", "banan", "anor"]
mevalar[1] = "shaftoli"

print(mevalar)  # ['olma', 'shaftoli', 'anor']
```

---

### 🔴 **5. `for` sikli orqali elementlarga murojaat**

`for` yordamida listdagi har bir element ustida amallar bajarish mumkin:

```python
mevalar = ["olma", "banan", "anor"]

for meva in mevalar:
    print("Men", meva, "ni yaxshi ko‘raman!")
```

**Natija:**

```
Men olma ni yaxshi ko‘raman!
Men banan ni yaxshi ko‘raman!
Men anor ni yaxshi ko‘raman!
```

---

### 🟢 **6. Indeks bilan birga aylanish (`enumerate`)**

Agar har bir element bilan birga **uning indeksi** ham kerak bo‘lsa, `enumerate()` funksiyasidan foydalaniladi.

```python
mevalar = ["olma", "banan", "anor"]

for indeks, meva in enumerate(mevalar):
    print(f"{indeks}: {meva}")
```

**Natija:**

```
0: olma
1: banan
2: anor
```

✅ **`enumerate()`** siklda indeksni avtomatik beradi — bu kodni soddalashtiradi.

---

### 🟣 **7. `in` operatori yordamida tekshirish**

`in` operatori ro‘yxatda element bor yoki yo‘qligini tekshiradi.

```python
mevalar = ["olma", "banan", "anor"]

print("olma" in mevalar)   # True
print("gilos" in mevalar)  # False
```

Agar yo‘q bo‘lsa `False` qaytaradi, xatolik chiqarmaydi.

---

### 🔵 **8. List uzunligini aniqlash – `len()`**

`len()` funksiyasi ro‘yxatdagi elementlar sonini qaytaradi.

```python
mevalar = ["olma", "banan", "anor", "gilos"]
print(len(mevalar))  # 4
```

---

### 🧩 **9. Ichma-ich list elementlariga murojaat**

Agar list ichida list bo‘lsa (nested list), bir necha indeks yordamida ichki elementga kirish mumkin:

```python
matritsa = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

print(matritsa[0][1])  # 2
print(matritsa[2][2])  # 9
```

---

### 🧠 **10. Ehtimoliy xatolik holatlari**

1. **Indeksdan tashqariga murojaat qilish**

   ```python
   mevalar = ["olma", "banan"]
   print(mevalar[5])  # ❌ IndexError
   ```

2. **Bo‘sh listga slicing**

   ```python
   bo‘sh = []
   print(bo‘sh[0:2])  # ✅ Bo‘sh list qaytaradi, xato emas
   ```

3. **Manfiy indeks noto‘g‘ri ishlatish**

   ```python
   mevalar = ["olma"]
   print(mevalar[-2])  # ❌ IndexError
   ```

---

### 🧮 **11. Amaliy misol**

Foydalanuvchidan ro‘yxat kiritib, faqat juft indeksdagi elementlarni chiqarish:

```python
mevalar = []

n = int(input("Nechta meva nomi kiritasiz? "))
for i in range(n):
    nom = input(f"{i+1}-meva nomini kiriting: ")
    mevalar.append(nom)

print("Juft indeksdagi mevalar:")
for i in range(0, len(mevalar), 2):
    print(mevalar[i])
```

**Namuna:**

```
Nechta meva nomi kiritasiz? 5
1-meva nomini kiriting: olma
2-meva nomini kiriting: anor
3-meva nomini kiriting: banan
4-meva nomini kiriting: nok
5-meva nomini kiriting: gilos
Juft indeksdagi mevalar:
olma
banan
gilos
```

---

### 🏁 **Xulosa**

| Amal                   | Tavsif                          | Misol                             |
| ---------------------- | ------------------------------- | --------------------------------- |
| `list[i]`              | Belgilangan indeksdagi element  | `mevalar[0]`                      |
| `list[-1]`             | Oxirgi element                  | `mevalar[-1]`                     |
| `list[start:end:step]` | Bo‘lak olish (slicing)          | `mevalar[1:3]`                    |
| `for x in list`        | Har bir elementni o‘qish        | `for m in mevalar:`               |
| `enumerate(list)`      | Indeks + element olish          | `for i, m in enumerate(mevalar):` |
| `'x' in list`          | Element mavjudligini tekshirish | `'olma' in mevalar`               |
| `len(list)`            | Elementlar soni                 | `len(mevalar)`                    |

---
---

## 🧩 4-BO‘LIM: **Listni o‘zgartirish**

---

### 🟢 **1. Elementni almashtirish (qiymatini o‘zgartirish)**

Listdagi element qiymatini indeks orqali o‘zgartirish mumkin.

```python
mevalar = ["olma", "banan", "anor"]
mevalar[1] = "shaftoli"

print(mevalar)
```

**Natija:**

```
['olma', 'shaftoli', 'anor']
```

⚠️ Agar indeks mavjud bo‘lmasa, `IndexError` yuz beradi.

---

### 🟣 **2. Yangi element qo‘shish**

Python’da listga element qo‘shishning bir nechta usuli bor:

---

#### ✅ **a) `append()` – oxiriga bitta element qo‘shish**

```python
sonlar = [10, 20, 30]
sonlar.append(40)
print(sonlar)
```

**Natija:** `[10, 20, 30, 40]`

**Tavsif:**

* Argument: **bitta element**
* Yangi element **ro‘yxat oxiriga** qo‘shiladi
* O‘zgartirilgan list qaytariladi (`None` emas)

⚠️ Ko‘p element qo‘shmoqchi bo‘lsangiz, `extend()` dan foydalaning.

---

#### ✅ **b) `insert(index, element)` – belgilangan joyga qo‘shish**

```python
mevalar = ["olma", "banan", "anor"]
mevalar.insert(1, "shaftoli")

print(mevalar)
```

**Natija:** `['olma', 'shaftoli', 'banan', 'anor']`

**Tavsif:**

* `index` — yangi element joylashadigan pozitsiya
* `element` — qo‘shiladigan qiymat
* Eski elementlar o‘ngga suriladi

---

#### ✅ **c) `extend(iterable)` – bir nechta elementlarni qo‘shish**

```python
a = [1, 2, 3]
b = [4, 5, 6]

a.extend(b)
print(a)
```

**Natija:** `[1, 2, 3, 4, 5, 6]`

**Tavsif:**

* Argument sifatida har qanday **iterable** (list, tuple, set, string) beriladi.
* Har bir element **alohida** qo‘shiladi.

```python
x = ["a", "b"]
x.extend("cd")
print(x)  # ['a', 'b', 'c', 'd']
```

---

### 🔵 **3. Elementni o‘chirish**

Listdan elementlarni o‘chirishning bir nechta usuli bor:

---

#### ✅ **a) `remove(value)` – qiymat bo‘yicha o‘chirish**

```python
mevalar = ["olma", "banan", "anor", "banan"]
mevalar.remove("banan")
print(mevalar)
```

**Natija:** `['olma', 'anor', 'banan']`

**Tavsif:**

* Faqat **birinchi uchragan qiymatni** o‘chiradi.
* Agar qiymat topilmasa — `ValueError` yuz beradi.

⚠️ Oldin tekshirib olish tavsiya qilinadi:

```python
if "nok" in mevalar:
    mevalar.remove("nok")
```

---

#### ✅ **b) `pop(index)` – indeks bo‘yicha o‘chirish va qiymatni qaytarish**

```python
sonlar = [10, 20, 30, 40]
ochirilgan = sonlar.pop(2)

print(sonlar)
print("O‘chirilgan:", ochirilgan)
```

**Natija:**

```
[10, 20, 40]
O‘chirilgan: 30
```

**Tavsif:**

* Argument: indeks (ixtiyoriy)
* Agar indeks kiritilmasa, **oxirgi element** o‘chiriladi.
* O‘chirilgan qiymatni qaytaradi.

⚠️ Agar list bo‘sh bo‘lsa yoki indeks mavjud bo‘lmasa, `IndexError`.

---

#### ✅ **c) `del` operatori – indeks yoki bo‘lakni o‘chirish**

```python
sonlar = [10, 20, 30, 40, 50]
del sonlar[1]  # 20 ni o‘chiradi
print(sonlar)
```

**Natija:** `[10, 30, 40, 50]`

**Bo‘lakni o‘chirish (slicing bilan):**

```python
del sonlar[1:3]
print(sonlar)  # [10, 50]
```

**Butun listni o‘chirish:**

```python
del sonlar
```

---

#### ✅ **d) `clear()` – butun listni tozalash**

```python
mevalar = ["olma", "banan", "anor"]
mevalar.clear()
print(mevalar)
```

**Natija:** `[]`

---

### 🟠 **4. Listni teskari qilish va tartiblash**

#### 🪞 **a) `reverse()` – teskari tartibda joylashtirish**

```python
sonlar = [10, 20, 30]
sonlar.reverse()
print(sonlar)  # [30, 20, 10]
```

---

#### 🔤 **b) `sort()` – elementlarni tartiblash**

```python
sonlar = [50, 10, 30, 20]
sonlar.sort()
print(sonlar)  # [10, 20, 30, 50]
```

**Parametrlar:**

* `reverse=True` → kamayish tartibida
* `key=function` → maxsus tartiblash qoidasi

```python
sozlar = ["olma", "banan", "anor"]
sozlar.sort(reverse=True)
print(sozlar)  # ['olma', 'banan', 'anor'] teskari alfavitda
```

---

### 🧠 **5. Ehtimoliy xatolik holatlari**

| Vaziyat                               | Kod                  | Natija                     |
| ------------------------------------- | -------------------- | -------------------------- |
| `remove()` qiymat topa olmasa         | `lst.remove("yo‘q")` | `ValueError`               |
| `pop()` bo‘sh listda                  | `[].pop()`           | `IndexError`               |
| `insert()` noto‘g‘ri indeks           | `insert(100, "x")`   | Avtomatik oxiriga qo‘shadi |
| `sort()` turli tipli elementlar bilan | `[1, "a"].sort()`    | `TypeError`                |

---

### 💡 **6. Amaliy misol**

**Foydalanuvchidan mevalar ro‘yxatini kiritish va ularni tahrirlash:**

```python
mevalar = []

# Ro‘yxat yaratish
n = int(input("Nechta meva nomi kiritasiz? "))
for i in range(n):
    meva = input(f"{i+1}-meva: ")
    mevalar.append(meva)

print("Boshlang‘ich ro‘yxat:", mevalar)

# Element qo‘shish
yangi = input("Qo‘shmoqchi bo‘lgan mevani kiriting: ")
mevalar.append(yangi)

# Element o‘chirish
ochir = input("Qaysi mevani o‘chirmoqchisiz? ")
if ochir in mevalar:
    mevalar.remove(ochir)

# Tartiblash
mevalar.sort()

print("Yangilangan ro‘yxat:", mevalar)
```

---

### 🏁 **Xulosa**

| Amal               | Tavsif                                 | Misol                    |
| ------------------ | -------------------------------------- | ------------------------ |
| `append(x)`        | Oxiriga element qo‘shish               | `lst.append(5)`          |
| `insert(i, x)`     | Belgilangan joyga qo‘shish             | `lst.insert(1, "olma")`  |
| `extend(iterable)` | Bir nechta element qo‘shish            | `lst.extend([4,5])`      |
| `remove(x)`        | Qiymat bo‘yicha o‘chirish              | `lst.remove("olma")`     |
| `pop(i)`           | Indeks bo‘yicha o‘chirish va qaytarish | `lst.pop(2)`             |
| `del lst[i]`       | Indeks yoki bo‘lakni o‘chirish         | `del lst[1:3]`           |
| `clear()`          | Hammasini o‘chirish                    | `lst.clear()`            |
| `sort()`           | Tartiblash                             | `lst.sort(reverse=True)` |
| `reverse()`        | Teskari qilish                         | `lst.reverse()`          |

---

---

## 🧩 5-BO‘LIM: **List ustida amallar**

Bu bo‘limda listlar bilan **matematik va mantiqiy amallar**, **birlashtirish**, **ko‘paytirish**, **kesish (slicing)**, **teskari tartiblash**, **tartiblash**, va **nusxalash** kabi amallarni o‘rganamiz.

---

### 🟢 **1. Listlarni qo‘shish (`+` operatori)**

Ikki yoki undan ortiq listlarni **birlashtirish** uchun `+` operatoridan foydalaniladi.
Natijada **yangi list** hosil bo‘ladi (asl listlar o‘zgarmaydi).

```python
a = [1, 2, 3]
b = [4, 5, 6]
c = a + b
print(c)
```

**Natija:** `[1, 2, 3, 4, 5, 6]`

✅ **Foydali holatlar:**

* Bir nechta ma’lumotlarni bitta ro‘yxatda jamlash.
* Foydalanuvchi ma’lumotlarini ketma-ket qo‘shish.

---

### 🔵 **2. Listni ko‘paytirish (`*` operatori)**

Listni `n` marta takrorlash uchun ishlatiladi.
Bu ham **yangi list** hosil qiladi.

```python
meva = ["olma", "banan"]
print(meva * 3)
```

**Natija:** `['olma', 'banan', 'olma', 'banan', 'olma', 'banan']`

⚠️ Agar list ichida **mutable** element (masalan, ichki list) bo‘lsa, `*` bilan ko‘paytirish havolalar (reference) bilan ishlaydi — bu ba’zan noxush natijalar beradi:

```python
a = [[0]] * 3
a[0][0] = 99
print(a)  # [[99], [99], [99]] — hammasi bitta manzilga ishora qiladi!
```

✅ **To‘g‘ri yo‘l:**

```python
a = [[0] for _ in range(3)]
```

---

### 🟣 **3. Listni kesish (slicing)**

Slicing listdan bo‘lak olish uchun ishlatiladi:
`sintaksis: list[start:end:step]`

```python
sonlar = [10, 20, 30, 40, 50, 60]

print(sonlar[1:4])   # [20, 30, 40]
print(sonlar[:3])    # [10, 20, 30]
print(sonlar[3:])    # [40, 50, 60]
print(sonlar[::2])   # [10, 30, 50]
print(sonlar[::-1])  # [60, 50, 40, 30, 20, 10]
```

🧠 **Slicing orqali nusxalash:**

```python
a = [1, 2, 3]
b = a[:]   # To‘liq nusxa
b.append(4)
print(a, b)  # a o‘zgarmaydi
```

---

### 🟠 **4. Listni teskari qilish (`reverse()` va slicing)**

#### ✅ `reverse()` metodi

Listni joyida (in-place) o‘zgartiradi.

```python
sonlar = [10, 20, 30]
sonlar.reverse()
print(sonlar)
```

**Natija:** `[30, 20, 10]`

#### ✅ Slicing yordamida

```python
sonlar = [10, 20, 30]
teskari = sonlar[::-1]
print(teskari)
```

**Natija:** `[30, 20, 10]`
⚠️ Bu usul **yangi list** hosil qiladi, asl ro‘yxat o‘zgarmaydi.

---

### 🔴 **5. Listni tartiblash (`sort()` va `sorted()`)**

#### ✅ `sort()` – joyida (asl listni) tartiblaydi

```python
sonlar = [40, 10, 30, 20]
sonlar.sort()
print(sonlar)
```

**Natija:** `[10, 20, 30, 40]`

* `reverse=True` → kamayish tartibida tartiblaydi
* `key=function` → o‘ziga xos tartiblash mezoni

```python
sozlar = ["olma", "Banan", "anor"]
sozlar.sort(key=str.lower)
print(sozlar)
```

**Natija:** `['anor', 'Banan', 'olma']` (katta-kichik harflarni farqlamaydi)

---

#### ✅ `sorted()` – yangi tartiblangan list qaytaradi

```python
sonlar = [5, 2, 9, 1]
yangi = sorted(sonlar)
print("Yangi:", yangi)
print("Asl:", sonlar)
```

**Natija:**

```
Yangi: [1, 2, 5, 9]
Asl: [5, 2, 9, 1]
```

✅ `sorted()` → asl listni o‘zgartirmaydi.

---

### 🟢 **6. Listlarni taqqoslash**

Python’da listlar **elementlar ketma-ketligi** bo‘yicha solishtiriladi.

```python
print([1, 2, 3] == [1, 2, 3])  # True
print([1, 2, 3] != [3, 2, 1])  # True
print([1, 2] < [1, 3])          # True (2 < 3)
```

---

### 🟣 **7. Listni nusxalash**

#### ✅ To‘g‘ridan-to‘g‘ri havola (reference)

```python
a = [1, 2, 3]
b = a
b.append(4)
print(a)  # [1, 2, 3, 4]
```

⚠️ Ikkisi **bitta manzilni** ko‘rsatadi!

---

#### ✅ To‘g‘ri nusxalash usullari:

```python
# 1) copy() metodi
a = [1, 2, 3]
b = a.copy()

# 2) slicing
b = a[:]

# 3) list() funksiyasi
b = list(a)
```

**Hammasi yangi list hosil qiladi.**

---

### 🔵 **8. Amaliy misollar**

#### 🔹 Misol 1. Ikki listni birlashtirish

```python
ism = ["Ali", "Laylo"]
yosh = [20, 21]
birgalikda = ism + yosh
print(birgalikda)
```

**Natija:** `['Ali', 'Laylo', 20, 21]`

---

#### 🔹 Misol 2. Juft indeksdagi elementlarni olish

```python
sonlar = [1, 2, 3, 4, 5, 6]
juftlar = sonlar[::2]
print(juftlar)  # [1, 3, 5]
```

---

#### 🔹 Misol 3. Ro‘yxatni kamayish tartibida tartiblash

```python
ballar = [56, 89, 45, 90, 70]
ballar.sort(reverse=True)
print(ballar)
```

**Natija:** `[90, 89, 70, 56, 45]`

---

#### 🔹 Misol 4. Foydalanuvchidan ma’lumot olib teskari chiqarish

```python
sonlar = []
for i in range(5):
    son = int(input(f"{i+1}-sonni kiriting: "))
    sonlar.append(son)

print("Kiritilgan sonlar:", sonlar)
print("Teskari tartibda:", sonlar[::-1])
```

---

### 🧠 **9. Ehtimoliy xatolik holatlari**

| Vaziyat                                    | Kod                 | Natija                           |
| ------------------------------------------ | ------------------- | -------------------------------- |
| `+` bilan boshqa tipni qo‘shish            | `[1, 2] + 3`        | ❌ TypeError                      |
| `sort()`da turli turlar                    | `[1, "a"].sort()`   | ❌ TypeError                      |
| `*` bilan ichki list                       | `[[0]] * 3`         | Barcha elementlar bir xil obyekt |
| `reverse()` va `sort()` qiymat qaytarmaydi | `print(lst.sort())` | `None` chiqadi                   |

---

### 🏁 **Xulosa**

| Amal          | Tavsif                  | Misol                    |
| ------------- | ----------------------- | ------------------------ |
| `a + b`       | Listlarni birlashtirish | `[1,2]+[3,4]`            |
| `a * n`       | Listni takrorlash       | `[1,2]*3`                |
| `a[:]`        | Nusxalash / slicing     | `lst[1:3]`               |
| `lst[::-1]`   | Teskari tartib          | `lst[::-1]`              |
| `sort()`      | Joyida tartiblash       | `lst.sort(reverse=True)` |
| `sorted(lst)` | Yangi tartiblangan list | `sorted(lst)`            |
| `copy()`      | Mustaqil nusxa          | `lst.copy()`             |

---

---

## 🧩 6-BO‘LIM: **Listning foydali funksiyalari va metodlari**

Bu bo‘limda listlar bilan tez-tez ishlatiladigan **standart funksiyalar** (`len()`, `max()`, `min()`, `sum()`) hamda **maxsus metodlar** (`index()`, `count()`, `copy()`, `clear()`) haqida to‘liq tushuntiramiz.

---

### 🟢 **1. `len()` – elementlar sonini aniqlash**

`len()` funksiyasi listdagi **elementlar sonini** qaytaradi.

```python
mevalar = ["olma", "banan", "anor", "gilos"]
print(len(mevalar))
```

**Natija:** `4`

✅ **Foydali holatlar:**

* `for` siklida chegarani aniqlash
* Foydalanuvchidan ma’lumot kiritish sonini cheklash
* List bo‘sh yoki yo‘qligini tekshirish:

  ```python
  if len(mevalar) == 0:
      print("List bo‘sh")
  ```

---

### 🔵 **2. `max()` va `min()` – eng katta va eng kichik qiymatlar**

Faqat **sonli yoki tartiblanadigan** elementlar uchun ishlaydi.

```python
sonlar = [4, 10, 2, 99, 45]
print("Eng katta:", max(sonlar))
print("Eng kichik:", min(sonlar))
```

**Natija:**

```
Eng katta: 99
Eng kichik: 2
```

✅ **Matnli listlarda ham ishlaydi (alfavit tartibi):**

```python
sozlar = ["olma", "banan", "anor"]
print(max(sozlar))  # 'olma' (alfavitda oxiri)
print(min(sozlar))  # 'anor' (alfavitda birinchi)
```

⚠️ **Xatolik holati:**
Turli tipli qiymatlar bilan ishlatilmaydi:

```python
max([1, "ikki", 3])  # ❌ TypeError
```

---

### 🟣 **3. `sum()` – elementlar yig‘indisini hisoblash**

Faqat **raqamli elementlar** uchun ishlaydi.

```python
sonlar = [10, 20, 30]
print(sum(sonlar))
```

**Natija:** `60`

**Qo‘shimcha argument:** boshlang‘ich qiymat (`start`)

```python
print(sum(sonlar, 100))  # 100 + (10 + 20 + 30) = 160
```

⚠️ Matnli listlarda ishlamaydi.

---

### 🟠 **4. `index()` – element indeksini topish**

`index()` berilgan elementning **birinchi topilgan** indeksini qaytaradi.

```python
mevalar = ["olma", "banan", "anor", "banan"]
print(mevalar.index("banan"))
```

**Natija:** `1`

**Qo‘shimcha argumentlar:**

* `index(qiymat, start, end)`

```python
print(mevalar.index("banan", 2))  # 3
```

⚠️ Agar qiymat topilmasa — `ValueError`:

```python
mevalar.index("nok")  # ❌ ValueError
```

✅ Oldin tekshirib olish tavsiya qilinadi:

```python
if "nok" in mevalar:
    print(mevalar.index("nok"))
```

---

### 🔴 **5. `count()` – element necha marta uchrashini aniqlash**

```python
mevalar = ["olma", "banan", "olma", "anor", "olma"]
print(mevalar.count("olma"))
```

**Natija:** `3`

✅ **Qo‘llanilishi:**

* Statistik ma’lumotlar yig‘ish
* Takrorlanishlarni tahlil qilish
* Ma’lum qiymat sonini tekshirish

---

### 🟢 **6. `copy()` – mustaqil nusxa yaratish**

`copy()` ro‘yxatning **mustaqil (yangi)** nusxasini yaratadi.
Bu juda muhim, chunki oddiy `b = a` deganda ikkala o‘zgaruvchi **bitta xotira manzilni** ko‘rsatadi.

```python
a = [1, 2, 3]
b = a.copy()

b.append(4)

print("a:", a)
print("b:", b)
```

**Natija:**

```
a: [1, 2, 3]
b: [1, 2, 3, 4]
```

✅ Endi `b` va `a` mustaqil.

⚠️ **Eslatma:** Ichma-ich listlarda `copy()` yuzaki nusxa (shallow copy) yaratadi:

```python
a = [[1, 2], [3, 4]]
b = a.copy()
b[0][0] = 99
print(a)  # [[99, 2], [3, 4]]
```

✅ Bunday hollarda `deepcopy()` kerak:

```python
import copy
b = copy.deepcopy(a)
```

---

### 🟣 **7. `clear()` – ro‘yxatni tozalash**

Listdagi **barcha elementlarni o‘chiradi**, lekin o‘zgaruvchining o‘zi saqlanadi.

```python
mevalar = ["olma", "banan", "anor"]
mevalar.clear()
print(mevalar)
```

**Natija:** `[]`

---

### 🟠 **8. Bir nechta metodlarni ketma-ket ishlatish**

```python
sonlar = [5, 3, 8, 5, 2, 5, 9]
print("Dastlabki:", sonlar)
print("Eng ko‘p uchragan:", max(sonlar, key=sonlar.count))
print("Eng kam uchragan:", min(sonlar, key=sonlar.count))
```

**Natija:**

```
Dastlabki: [5, 3, 8, 5, 2, 5, 9]
Eng ko‘p uchragan: 5
Eng kam uchragan: 8
```

---

### 🔵 **9. Amaliy misollar**

#### 🔹 Misol 1. Foydalanuvchi kiritgan sonlar ustida hisoblash

```python
sonlar = []
for i in range(5):
    son = int(input(f"{i+1}-sonni kiriting: "))
    sonlar.append(son)

print("Yig‘indi:", sum(sonlar))
print("O‘rtacha:", sum(sonlar)/len(sonlar))
print("Eng katta:", max(sonlar))
print("Eng kichik:", min(sonlar))
```

---

#### 🔹 Misol 2. Elementni topish va necha marta qatnashganini bilish

```python
sozlar = ["olma", "banan", "olma", "anor", "olma"]
qidiruv = input("Qaysi so‘zni tekshirmoqchisiz? ")
if qidiruv in sozlar:
    print(f"'{qidiruv}' {sozlar.count(qidiruv)} marta uchradi.")
else:
    print("Bunday so‘z yo‘q.")
```

---

### 🧠 **10. Xatolik holatlari**

| Vaziyat                           | Kod                 | Natija             |
| --------------------------------- | ------------------- | ------------------ |
| `index()` qiymat topa olmasa      | `lst.index("yo‘q")` | ❌ `ValueError`     |
| `max()` yoki `min()` bo‘sh listda | `max([])`           | ❌ `ValueError`     |
| `sum()` matnli elementlar bilan   | `sum(["a", "b"])`   | ❌ `TypeError`      |
| `copy()` chuqur listda            | `[[1],[2]].copy()`  | Faqat yuzaki nusxa |

---

### 🏁 **Xulosa**

| Funksiya / Metod | Tavsif                      | Misol            |
| ---------------- | --------------------------- | ---------------- |
| `len(lst)`       | Elementlar soni             | `len([1,2,3])`   |
| `max(lst)`       | Eng katta qiymat            | `max([1,9,3])`   |
| `min(lst)`       | Eng kichik qiymat           | `min([1,9,3])`   |
| `sum(lst)`       | Yig‘indi                    | `sum([1,2,3])`   |
| `index(x)`       | Qiymatning indeksi          | `lst.index("a")` |
| `count(x)`       | Qiymat necha marta uchragan | `lst.count(5)`   |
| `copy()`         | Mustaqil nusxa              | `lst.copy()`     |
| `clear()`        | Hammasini o‘chirish         | `lst.clear()`    |

---

---

## 🧩 7-BO‘LIM: **Ichma-ich listlar (Nested Lists)**

### 🟢 1. Ichma-ich list nima?

**Ichma-ich list** — bu **list ichida boshqa listlar saqlanadigan** tuzilma.
Bunday listlar ko‘p o‘lchovli ma’lumotlarni (masalan, **jadval**, **matritsa**, **o‘quvchilar ro‘yxati**) ifodalash uchun ishlatiladi.

```python
matritsa = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
```

Bu list 3 ta ichki listdan iborat, har bir ichki listda 3 tadan element bor.

---

### 🔵 2. Ichki elementlarga murojaat qilish

Bitta indeks emas, **ikkita (yoki undan ortiq)** indeks ishlatiladi:

```python
print(matritsa[0])      # [1, 2, 3]
print(matritsa[0][1])   # 2
print(matritsa[2][2])   # 9
```

**Izoh:**
`matritsa[2][2]` → 3-qatordagi 3-element (9).

---

### 🟣 3. Ichki elementni o‘zgartirish

Oddiy listdagidek, faqat indekslar ketma-ket yoziladi:

```python
matritsa[1][2] = 60
print(matritsa)
```

**Natija:**

```
[[1, 2, 3],
 [4, 5, 60],
 [7, 8, 9]]
```

---

### 🟠 4. Ichma-ich listni aylantirib chiqish (for sikli bilan)

#### 🔹 Oddiy sikl bilan (qatorlar bo‘yicha):

```python
for qator in matritsa:
    print(qator)
```

**Natija:**

```
[1, 2, 3]
[4, 5, 6]
[7, 8, 9]
```

#### 🔹 Ichki sikl bilan (har bir elementni olish):

```python
for qator in matritsa:
    for element in qator:
        print(element, end=" ")
```

**Natija:**
`1 2 3 4 5 6 7 8 9`

---

### 🔴 5. Ichma-ich list yaratish uchun `append()` dan foydalanish

```python
matritsa = []
for i in range(3):
    qator = []
    for j in range(3):
        qator.append(i * j)
    matritsa.append(qator)

print(matritsa)
```

**Natija:**
`[[0, 0, 0], [0, 1, 2], [0, 2, 4]]`

---

### 🟢 6. List comprehension bilan ichma-ich list yaratish

```python
matritsa = [[i * j for j in range(3)] for i in range(3)]
print(matritsa)
```

**Natija:**
`[[0, 0, 0], [0, 1, 2], [0, 2, 4]]`

Bu usul — **kodni ixcham va tez** qiladi.

---

### 🔵 7. Ichki listlardan ma’lum ustunni olish

Masalan, yuqoridagi 3×3 matritsada **2-ustunni** olish:

```python
ustun = [qator[1] for qator in matritsa]
print(ustun)
```

**Natija:** `[0, 1, 2]`

---

### 🟣 8. Ichki listni teskari tartiblash yoki sortlash

```python
matritsa = [
    [3, 1, 2],
    [6, 4, 5],
]
for qator in matritsa:
    qator.sort()

print(matritsa)
```

**Natija:**

```
[[1, 2, 3], [4, 5, 6]]
```

---

### 🟠 9. Amaliy misollar

#### 🔹 Misol 1. 3×3 matritsa ichidagi barcha elementlar yig‘indisi

```python
matritsa = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

yigindi = 0
for qator in matritsa:
    yigindi += sum(qator)

print("Yig‘indi:", yigindi)
```

**Natija:** `Yig‘indi: 45`

---

#### 🔹 Misol 2. 2D listda eng katta elementni topish

```python
katta = matritsa[0][0]
for qator in matritsa:
    for son in qator:
        if son > katta:
            katta = son
print("Eng katta:", katta)
```

**Natija:** `Eng katta: 9`

---

#### 🔹 Misol 3. Foydalanuvchidan ma’lumot bilan 2D list yaratish

```python
matritsa = []
n = int(input("Qatorlar soni: "))
m = int(input("Ustunlar soni: "))

for i in range(n):
    qator = []
    for j in range(m):
        qiymat = int(input(f"[{i},{j}] elementni kiriting: "))
        qator.append(qiymat)
    matritsa.append(qator)

print("Matritsa:")
for qator in matritsa:
    print(qator)
```

---

#### 🔹 Misol 4. Matritsani teskari chiqarish

```python
for qator in matritsa[::-1]:
    print(qator[::-1])
```

---

### 🧠 10. Ehtimoliy xatoliklar

| Vaziyat                        | Kod                               | Natija                                           |
| ------------------------------ | --------------------------------- | ------------------------------------------------ |
| Ichki indeks xatosi            | `matritsa[2][5]`                  | ❌ `IndexError`                                   |
| Ko‘paytirishda havola muammosi | `[[0]*3]*3`                       | ❌ Barcha qatorlar bir xil manzilga ishora qiladi |
| Chuqur nusxalash               | `copy()` emas, `deepcopy()` kerak | `import copy` bilan                              |

✅ **To‘g‘ri usul:**

```python
matritsa = [[0 for _ in range(3)] for _ in range(3)]
```

---

### 🏁 **Xulosa**

| Amal                        | Tavsif                   | Misol                     |
| --------------------------- | ------------------------ | ------------------------- |
| `matritsa[i][j]`            | Ichki elementga murojaat | `matritsa[1][2]`          |
| Ichki `for` sikl            | Har bir elementni olish  | `for q in m: for e in q:` |
| `[[... for j] for i]`       | 2D list comprehension    |                           |
| `sum(qator)`                | Qatordagi yig‘indi       |                           |
| `[[0]*n for _ in range(m)]` | Mustaqil 2D list         |                           |

---