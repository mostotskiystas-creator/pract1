from decorators import range_guard

@range_guard
def add(a, b):
    return a + b

print(add(10, 20))   # ✔ OK
print(add(0, 100))   # ✔ OK
print(add(150, 20))  # ❌ ValueError
