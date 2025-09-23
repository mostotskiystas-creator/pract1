def main():
    students = {}

    print("Введіть ім'я студента та його оцінку (1-12). Для завершення введіть 'stop'.")

    while True:
        name = input("Ім'я студента: ").strip()
        if name.lower() == "stop":
            break

        try:
            grade = int(input("Оцінка: "))
            if 1 <= grade <= 12:
                students[name] = grade
            else:
                print("❌ Оцінка має бути від 1 до 12!")
        except ValueError:
            print("❌ Потрібно ввести число!")

    
    print("\n📋 Список студентів та їх оцінки:")
    for name, grade in students.items():
        print(f"{name}: {grade}")

    if students:
        avg = sum(students.values()) / len(students)
        print(f"\n📊 Середній бал групи: {avg:.2f}")

        # Категорії
        excellent = [n for n, g in students.items() if 10 <= g <= 12]
        good = [n for n, g in students.items() if 7 <= g <= 9]
        bad = [n for n, g in students.items() if 4 <= g <= 6]
        failed = [n for n, g in students.items() if 1 <= g <= 3]

        print(f" Відмінники (10-12): {len(excellent)} -> {', '.join(excellent) if excellent else 'немає'}")
        print(f" Хорошисти (7-9): {len(good)} -> {', '.join(good) if good else 'немає'}")
        print(f" Відстаючі (4-6): {len(bad)} -> {', '.join(bad) if bad else 'немає'}")
        print(f" Не здали (1-3): {len(failed)} -> {', '.join(failed) if failed else 'немає'}")
    else:
        print("\nНемає введених студентів.")

if __name__ == "__main__":
    main()
