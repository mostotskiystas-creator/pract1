# --- Імпорт 10 різних бібліотек ---
import numpy as np            # бібліотека для роботи з масивами та матрицями
import pandas as pd           # таблиці та робота з даними
import requests               # HTTP запити (API)
import math                   # математика
import random                 # генерація випадкових чисел
import datetime               # робота з датами
import os                     # робота з операційною системою
import matplotlib.pyplot as plt   # графіки та візуалізація
from faker import Faker       # генерація фейкових даних
from PIL import Image         # робота з зображеннями (Pillow)

# --- Використання 5 різних бібліотек у try-блоках ---

# 1. NumPy
try:
    arr = np.array([1, 2, 3])          # створюємо масив
    print("NumPy result:", arr * 2)    # множимо всі елементи на 2
except Exception as e:
    print("NumPy error:", e)           # ловимо помилку

# 2. Pandas
try:
    df = pd.DataFrame({                # створюємо датафрейм
        "name": ["Stas", "Dima"],      # колонка імен
        "age": [16, 18]                # колонка віку
    })
    print("\nPandas DataFrame:")       
    print(df)                          # вивід таблиці
except Exception as e:
    print("Pandas error:", e)          # ловимо помилку

# 3. Requests
try:
    response = requests.get("https://api.github.com")   # робимо GET-запит
    print("\nRequests status code:", response.status_code)  # виводимо статус
except Exception as e:
    print("Requests error:", e)         # ловимо помилку

# 4. Faker
try:
    fake = Faker()                      # створюємо Faker об’єкт
    print("\nFake name:", fake.name())  # генеруємо фейкове ім’я
except Exception as e:
    print("Faker error:", e)            # ловимо помилку

# 5. Math
try:
    print("\nMath sqrt(16):", math.sqrt(16))   # корінь числа 16
except Exception as e:
    print("Math error:", e)            # ловимо помилку

print("\nПрограма виконана успішно!")   # фінальний вивід
