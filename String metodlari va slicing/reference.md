**Python'da string (matnli qiymatlar)**, ularning **metodlari** va **slicing** (bo‘laklash) haqida
---

## 1. String nima?

* **String** (`str`) — matnni ifodalovchi ma’lumot turi.
* U **bir nechta belgilar ketma-ketligi** bo‘lib, qo‘shtirnoq (`" "` yoki `' '`) ichida yoziladi.
* Python’da string **immutable** (o‘zgarmas) tur hisoblanadi, ya’ni uni o‘zgartirib bo‘lmaydi.

```python
matn1 = "Salom"
matn2 = 'Python'
print(type(matn1))  # <class 'str'>
```

---

## 2. String yaratish usullari

```python
s1 = "Salom"        # qo'shtirnoq
s2 = 'Dunyo'        # bitta tirnoq
s3 = """Ko'p qatordan
iborat
matn"""             # uch tirnoq (multi-line)
```

---

## 3. String indexing va slicing

Stringdagi har bir belgi **indeks** orqali murojaat qilinadi:

* Indeks **0 dan** boshlanadi.
* Salbiy indeks orqali oxiridan murojaat qilish mumkin.

```python
s = "Python"
print(s[0])   # P
print(s[5])   # n
print(s[-1])  # n
print(s[-2])  # o
```

### **Slicing (bo‘laklash)**

* `s[start:end:step]` ko‘rinishida yoziladi.
* `start` – qayerdan boshlab,
* `end` – qayergacha (end belgisi kirmaydi),
* `step` – qadam.

```python
s = "Python dasturlash"

print(s[0:6])     # Python
print(s[:6])      # Python (boshi default 0)
print(s[7:])      # dasturlash (oxirigacha)
print(s[::2])     # Pto atsrs (har 2-belgidan)
print(s[::-1])    # hsalrut sad nohtyP (teskari qilib chiqaradi)
```

---

## 4. String metodlari

Python’da stringlar bilan ishlash uchun juda ko‘p **metodlar** bor. Keling eng ko‘p ishlatiladiganlarini ko‘ramiz.

### Harflarni o‘zgartirish

```python
s = "python dasturi"

print(s.upper())    # Barcha harflarni katta
print(s.lower())    # Barcha harflarni kichik
print(s.title())    # Har bir so'zni katta harf bilan
print(s.capitalize())  # Faqat birinchi harfni katta
print(s.swapcase())    # Har bir harfni qarama-qarshi registrga
```

---

### Qidirish va tekshirish

```python
s = "Python dasturi"

print(s.find("on"))     # 4 (birinchi uchragan indeks)
print(s.rfind("o"))     # 4 (oxiridan qidiradi)
print(s.index("dasturi"))  # 7 (topmasa xato beradi)
print(s.startswith("Py"))  # True
print(s.endswith("ri"))    # True
```

---

### Belgilarni sanash va almashtirish

```python
s = "banana"

print(s.count("a"))        # 3 (nechta 'a' borligini sanaydi)
print(s.replace("a", "o")) # bonono (a -> o)
```

---

### Bo‘lish va qo‘shish

```python
s = "Salom dunyo"

print(s.split())       # ['Salom', 'dunyo'] (bo‘shliqqa ko‘ra bo‘ladi)
print(s.split("o"))    # ['Sal', 'm duny', ''] (harflar bo‘yicha)
print("-".join(["Salom", "Dunyo"]))  # Salom-Dunyo
```

---

### Bo‘sh joylarni olib tashlash

```python
s = "   Python   "

print(s.strip())   # 'Python' (boshi va oxiridagi bo‘sh joylarni olib tashlaydi)
print(s.lstrip())  # faqat boshidan
print(s.rstrip())  # faqat oxiridan
```

---

### Tekshirish metodlari

```python
s1 = "123"
s2 = "abc"
s3 = "Abc123"

print(s1.isdigit())   # True (faqat raqammi?)
print(s2.isalpha())   # True (faqat harfmi?)
print(s3.isalnum())   # True (harf+raqamdan iboratmi?)
print(s2.islower())   # True
print(s2.isupper())   # False
```

---

## 5. Amaliy dastur misollari

### 1) Matnni teskari qilish

```python
matn = "Python"
teskari = matn[::-1]
print("Teskari:", teskari)
```

### 2) Gapdagi so‘zlar sonini topish

```python
matn = "Python dasturlash juda qiziqarli"
sozlar = matn.split()
print("So'zlar soni:", len(sozlar))
```

### 3) Harflar sanog‘i

```python
matn = "salom dunyo"
for harf in set(matn):
    if harf != " ":
        print(harf, "->", matn.count(harf))
```

---

📌 **Xulosa:**

* `slicing` — stringlardan kerakli qismini olish uchun ishlatiladi.
* `string metodlari` — matnlarni tahrirlash, qidirish, tekshirish va formatlash imkoniyatini beradi.

---