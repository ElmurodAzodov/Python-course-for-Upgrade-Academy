
Operatorlar — bu Python’da **amal bajaruvchi belgilar yoki so‘zlar**. Ular yordamida biz qiymatlar ustida turli hisob-kitoblarni yoki solishtirishlarni qilamiz.

📌 Operatorlar 3 asosiy turga bo‘linadi:

1. **Arifmetik operatorlar**
2. **Taqqoslash (solishtirish) operatorlari**
3. **Mantiqiy operatorlar**

---

## 1. Arifmetik operatorlar

Arifmetik operatorlar sonlar ustida matematik amallarni bajaradi.

| Operator | Nima qiladi       | Misol     | Natija |
| -------- | ----------------- | --------- | ------ |
| `+`      | Qo‘shish          | `5 + 3`   | `8`    |
| `-`      | Ayrish            | `10 - 4`  | `6`    |
| `*`      | Ko‘paytirish      | `6 * 7`   | `42`   |
| `/`      | Bo‘lish           | `15 / 2`  | `7.5`  |
| `//`     | Butun bo‘lish     | `15 // 2` | `7`    |
| `%`      | Qoldiqni olish    | `15 % 2`  | `1`    |
| `**`     | Darajaga oshirish | `2 ** 3`  | `8`    |

### Misol:

```python
a = 15
b = 2

print("Qo‘shish:", a + b)     # 17
print("Ayrish:", a - b)      # 13
print("Ko‘paytirish:", a * b) # 30
print("Bo‘lish:", a / b)     # 7.5
print("Butun bo‘lish:", a // b) # 7
print("Qoldiq:", a % b)      # 1
print("Daraja:", a ** b)     # 225
```

---

## 2. Taqqoslash (solishtirish) operatorlari

Bu operatorlar qiymatlarni solishtiradi va **True** (rost) yoki **False** (yolg‘on) qiymat qaytaradi.

| Operator | Ma’nosi             | Misol    | Natija  |
| -------- | ------------------- | -------- | ------- |
| `==`     | Tengmi?             | `5 == 5` | `True`  |
| `!=`     | Teng emasmi?        | `5 != 3` | `True`  |
| `>`      | Kattami?            | `7 > 3`  | `True`  |
| `<`      | Kichikmi?           | `7 < 3`  | `False` |
| `>=`     | Katta yoki tengmi?  | `5 >= 5` | `True`  |
| `<=`     | Kichik yoki tengmi? | `4 <= 5` | `True`  |

### Misol:

```python
x = 10
y = 20

print("Tengmi:", x == y)   # False
print("Teng emasmi:", x != y) # True
print("Kattami:", x > y)   # False
print("Kichikmi:", x < y)  # True
print("Katta yoki tengmi:", x >= 10) # True
print("Kichik yoki tengmi:", y <= 20) # True
```

---

## 3. Mantiqiy operatorlar

Bu operatorlar **mantiqiy ifodalarni** birlashtirishda ishlatiladi.

| Operator | Ma’nosi                    | Misol                  | Natija  |
| -------- | -------------------------- | ---------------------- | ------- |
| `and`    | Ikkalasi ham rost bo‘lsa   | `(5 > 2) and (10 > 5)` | `True`  |
| `or`     | Bittasi rost bo‘lsa yetadi | `(5 > 10) or (10 > 5)` | `True`  |
| `not`    | Teskarisini olish          | `not(5 > 2)`           | `False` |

### Misol:

```python
a = 5
b = 10
c = 15

print("and operatori:", a < b and b < c) # True (5<10 va 10<15)
print("or operatori:", a > b or b < c)   # True (10<15 rost)
print("not operatori:", not(a < b))      # False (a<b rost, teskarisi esa False)
```

---

## 🔥 Kichik amaliy mashq

```python
# Foydalanuvchidan son kiritib, tekshiramiz
son = int(input("Son kiriting: "))

print("Son juftmi?", son % 2 == 0)   # taqqoslash operatori
print("Son musbatmi?", son > 0)      # taqqoslash operatori
print("Son juft va musbatmi?", (son % 2 == 0) and (son > 0))  # mantiqiy operator
```

➡️ Bu dastur foydalanuvchidan son olib, uni **juftlik, musbatlik** va ikkala shartni tekshiradi.