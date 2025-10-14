## 2-BO‘LIM: **List yaratish** — toʻliq tushuntirish, misollar va dasturlar

Python’da roʻyxat (list) yaratishning bir nechta usullari bor. Quyida har bir usulni **taʼrif**, **sintaksis/argumentlar**, **qachon ishlatish**, **kod misol(lar)** va **ehtimoliy xatoliklar** bilan batafsil ko‘rib chiqamiz. ✨

---

### 🟩 1) List literal (kvadrat qavslar) — eng tez va aniq usul

**Tushuntirish:** Toʻgʻridan-toʻgʻri elementlarni kvadrat qavslar `[]` ichida yozib list hosil qilasiz.

**Sintaksis:**

```python
L = [elem1, elem2, ...]
```

**Qachon ishlatish:** Agar elementlar oldindan maʼlum bo‘lsa yoki kod ichida konstant list kerak bo‘lsa — literal eng qulay va o‘qilishi eng yaxshi.

**Misollar:**

```python
mevalar = ["olma", "banan", "anor"]
aralash = [1, "salom", 3.14, True]
print(mevalar)      # ['olma', 'banan', 'anor']
print(aralash)      # [1, 'salom', 3.14, True]
```

**E'tibor:** List literal bilan yaratilgan list ichidagi elementlar istalgan turda bo‘lishi mumkin.

---

### 🟦 2) `list()` konstruktori — iterable dan list yaratish

**Tushuntirish:** `list()` ga iterable (ketma-ketlik) berib, uning elementlaridan yangi roʻyxat hosil qilasiz.

**Sintaksis va argumentlar:**

```python
list([iterable])
```

* `iterable` — ixtiyoriy, iterable obyekt (string, tuple, set, dict, range, generator, map, va hokazo). Agar `iterable` berilmasa, bo‘sh list qaytaradi.

**Qachon ishlatish:** Iterable ni roʻyxatga aylantirish kerak bo‘lganda (masalan, `map`, `filter`, `range`, `generator`, `tuple`, `set` va hokazo).

**Misollar:**

```python
print(list())               # []
print(list("salom"))        # ['s','a','l','o','m']  (string → xarflar)
print(list((1,2,3)))        # [1, 2, 3]             (tuple → list)
print(list(range(5)))       # [0, 1, 2, 3, 4]
print(list({10,20,30}))     # [10, 20, 30]         (set elementlari — tartib noma'lum)
```

**Muammolar / xatoliklar:**

* `list(5)` → `TypeError`: `int` iterable emas.
* `list(None)` → `TypeError`: `NoneType` iterable emas.
* `list('soz'.split())` — agar siz soʻzni bo‘lib olingan soʻzlar roʻyxatini xohlasangiz, `split()` bilan ishlash toʻgʻri; aks holda `list('soz')` har bir belgini chiqaradi.

**Tavsiya:** `map`, `filter` yoki generator natijasini listga aylantirishda `list(...)` ishlatiladi:

```python
nums = list(map(int, ["1","2","3"]))
```

---

### 🟨 3) Boʻsh list yaratish va keyin `append()` bilan toʻldirish

**Tushuntirish:** Dastlab bo‘sh list (`[]` yoki `list()`) yaratiladi, keyin `append()` yordamida elementlar ketma-ket qo‘shiladi.

**Sintaksis:**

```python
L = []
L.append(x)
```

**Qachon ishlatish:** Elementlar ketma-ket, foydalanuvchi kiritishi yoki tsikl ichida yaratilganda — dinamik tuzish uchun ideal.

**Misol (foydalanuvchi kiritishi):**

```python
talabalar = []
n = 3
for i in range(n):
    talabalar.append(input(f"{i+1}-talabaning ismi: "))
print(talabalar)
```

**Amaliy dastur (fayldan o'qish):**

```python
lines = []
with open("matn.txt", encoding="utf-8") as f:
    for line in f:
        lines.append(line.rstrip("\n"))
# end
```

**Performance eslatma:** `append()` amortizatsiyalangan O(1) — ko‘p hollarda samarali.

---

### 🟪 4) List comprehension bilan yaratish (keng ishlatiladi) — qisqacha eslatma

**Tushuntirish:** Listni bir yoʻla ifoda orqali hosil qilish usuli. (Batafsil 8-bo‘limda kengaytirilgan.)

**Sintaksis (oddiy):**

```python
L = [f(x) for x in iterable if condition]
```

**Qachon ishlatish:** Transformatsiya yoki filtr qilish uchun, tez, ixcham va ko‘pincha ancha tezroq.

**Misol:**

```python
kvadratlar = [x*x for x in range(10)]
```

(Batafsil: bu 8-bo‘limda to‘liq.)

---

### 🟫 5) `+` va `*` operatorlari orqali yaratish / kengaytirish

**Tushuntirish:**

* `+` — ikki listni birlashtiradi va yangi list qaytaradi.
* `*` — listni takrorlab yangi list hosil qiladi.

**Sintaksis:**

```python
L = [1,2] + [3,4]    # [1,2,3,4]
L = [0] * 5          # [0,0,0,0,0]
```

**Qachon ishlatish:** Qisqa statik listlarni tez yaratish yoki birlashtrish kerak bo‘lsa.

**E'tiborli xato (mutable ichki elementlar):**

```python
M = [[0]*3] * 3
# kutilgan: [[0,0,0],[0,0,0],[0,0,0]]
M[0][0] = 9
print(M)  # [[9,0,0],[9,0,0],[9,0,0]]  <-- hamma qatorlar bir obyektga ishora qiladi
```

**Toʻgʻri usul:**

```python
M = [[0]*3 for _ in range(3)]
M[0][0] = 9
print(M)  # faqat birinchi qator o'zgardi
```

---

### 🟧 6) Unpacking va `[*iterable]` — yangi variant

**Tushuntirish:** `*` operatori bilan iterable ni li͟st literal ichida “ochib” yangi list hosil qilishingiz mumkin.

**Misol:**

```python
t = (1,2,3)
L = [*t, 4]      # [1,2,3,4]
L2 = [*range(3)]
```

**Qachon foydali:** Bir nechta iterable ni birlashtirib yangi list qilishda (xuddi `chain` kabi).

---

### 🟢 7) Generator yoki iteratordan list olish

**Tushuntirish:** Agar mavjud generator/iterator bo‘lsa, `list(generator)` orqali elementlarni toʻliq listga yuklaysiz.

**Misol:**

```python
gen = (x*x for x in range(5))
L = list(gen)   # [0,1,4,9,16]
# gen endi ishlamaydi — iteratorlar bir martalik
```

**Eslatma:** Agar iterator juda katta bo‘lsa, toʻliq listga aylantirish `MemoryError` ga olib kelishi mumkin — bunday hollarda generatorni qadam-qadam ishlatish yoki `itertools`/`deque` kabi vositalar ishlatiladi.

---

### 🟡 8) Fayl va tashqi manbalardan list yaratish — amaliy misol

**Fayldagi qatorlarni listga olish:**

```python
with open("data.txt", encoding="utf-8") as f:
    lines = f.readlines()           # har bir element oxirida '\n' bilan
    # yoki:
    lines2 = f.read().splitlines()  # '\n' tashlab, chiroyli ro'yxat
```

**CSV misoli (soddalashtirilgan):**

```python
import csv
rows = []
with open("data.csv", newline="", encoding="utf-8") as f:
    reader = csv.reader(f)
    for row in reader:
        rows.append(row)  # har bir row ro'yxat (columns ro'yxati)
```

---

### 🔴 9) Nusxa olish (shallow copy) eslatmasi — yaratish davrida muhim

**Tushuntirish:** List yaratish paytida `=` ishlatilsa, yangi nom — eski listga havola (reference) bo‘ladi, nusxa olinmaydi.

**Misol (nojo‘ya):**

```python
a = [1,2,3]
b = a       # nusxa emas — hammasi bir xil obyektga ishora qiladi
b.append(4)
print(a)    # [1,2,3,4]  <-- a ham o'zgardi
```

**Toʻgʻri nusxa olish (yaratishda):**

```python
a = [1,2,3]
b = a.copy()      # yoki b = list(a) yoki b = a[:] 
b.append(9)
print(a)  # [1,2,3]
print(b)  # [1,2,3,9]
```

---

### ⚠️ 10) Eng ko‘p uchraydigan hatoliklar va sabab-natija

* `list(5)` → `TypeError: 'int' object is not iterable`. Sabab: `list()` faqat iterable qabul qiladi. Tuzatish: `list(range(5))` yoki `[5]`.
* `list("soz")` kutilmagan natija: ko‘pincha matnni bo‘laklarga (so‘zlarga) bo‘lish uchun `split()` kerak (`"matn so'z".split()`).
* `[[0]*n]*m` — ichki listlar bir obyektdir, shuning uchun o‘zgartirish barchasini o‘zgartiradi. Tuzatish: `[ [0]*n for _ in range(m) ]`.
* Juda katta list yaratish (`list(range(10**9))`) — `MemoryError`. Tuzatish: generator/iterator yoki faqat zarur bo‘lgan qismni ishlash.

---

### 🧠 11) Amaliy maslahatlar (best practices)

* Agar elementlar maʼlum va statik bo‘lsa — literal `[]` ishlating.
* Agar iterable dan o‘tkazayotgan bo‘lsangiz — `list(iterable)` aniq va tushunarli.
* Massivni bosqichma-bosqich yig‘ish uchun `append()` yoki comprehension (agar bir martada hosil qilsa) afzal.
* Katta maʼlumotlarda generator va `itertools` ishlatish xotirani tejaydi.
* Ichma-ich listlar (2D) yaratishda `[[0]*n for _ in range(m)]` dan foydalaning — `*` operatori bilan nusxa olishdan saqlaning.

---

### 🧪 12) Qisqa amaliy dasturlar (misollar)

**A) Foydalanuvchidan sonlarni olib list yaratish:**

```python
n = int(input("Nechta son? "))
nums = []
for _ in range(n):
    nums.append(int(input("Son: ")))
print("Siz kiritganlar:", nums)
```

**B) Matndan so‘zlar roʻyxatini olish:**

```python
text = "Bu bir test matni, so'zlar bilan ishlash uchun."
words = text.replace(",", "").split()  # punktuatsiyani olib tashlab split
print(words)
```

**C) Generatorni roʻyxatga aylantirish:**

```python
gen = (i*i for i in range(10) if i%2==0)
evens_sq = list(gen)
print(evens_sq)  # [0,4,16,36,64]
```

**D) Tuple → list va keyin o'zgartirish:**

```python
t = (1,2,3)
L = list(t)
L[0] = 99
print(L)  # [99,2,3]
```

---

### ✅ 13) Xulosa (qisqacha)

* List yaratish uchun asosiy usullar: **literal `[]`**, **`list(iterable)`**, **append orqali dinamik toʻldirish**, **list comprehension**, **`+`/`*` operatorlari**, va **`[*iterable]` unpacking**.
* Har metodning o‘z holatga mos ishlatilishi bor: literallar statik listlar uchun, `list()` konvertatsiya uchun, `append()` tsiklda yig‘ish uchun, comprehension esa bir qator transformatsiyalar uchun qulay.
* E'tibor: iterables, generatorlar, va mutable ichki obyektlar bilan bog‘liq xatoliklarga ehtiyot bo‘ling.

---