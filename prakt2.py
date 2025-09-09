main_list = [12, 5, 7, 20, 3, 18, 1, 25, 14, 9,
             "car", "house", "river", "mountain", "cloud",
             "forest", "road", "city", "lake", "tree"]

ints = sorted([x for x in main_list if isinstance(x, int)])
strings = sorted([x for x in main_list if isinstance(x, str)])

sorted_list = ints + strings

multiples_of_two = [x for x in ints if x % 2 == 0]

uppercased_strings = [x.upper() for x in strings]

print("Основний список:", main_list)
print("Відсортований список:", sorted_list)
print("Елементи, кратні двом:", multiples_of_two)
print("Рядки капсом:", uppercased_strings)
