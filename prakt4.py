
def format_price(price: float) -> str:
    return f"ціна: {price:.2f} грн"


def check_availability(*items, stock=None) -> dict:
    if stock is None:
        stock = {}
    return {item: stock.get(item, False) for item in items}

def process_order(order: list, stock: dict, prices: dict):
  
    availability = check_availability(*order, stock=stock)

    if not all(availability.values()):
        print("❌ Замовлення неможливе, бо деякі товари відсутні:")
        for item, available in availability.items():
            if not available:
                print(f"   - {item}")
        return

   
    total = sum(prices[item] for item in order)
    print(" Ваше замовлення:")
    for item in order:
        print(f"   - {item}: {format_price(prices[item])}")
    print(f" Загальна {format_price(total)}")

def main():
   
    prices = {
        "хліб": 25.5,
        "молоко": 32.0,
        "яйця": 48.75,
        "сир": 120.0,
        "масло": 85.3
    }

   
    stock = {
        "хліб": True,
        "молоко": True,
        "яйця": False,
        "сир": True,
        "масло": True
    }

    while True:
        print("\n--- Магазин ---")
        print("1. Переглянути ціну товару")
        print("2. Зробити замовлення")
        print("3. Вийти")

        choice = input("Виберіть опцію: ")

        if choice == "1":
            item = input("Введіть назву товару: ").strip().lower()
            if item in prices:
                print(f"{item}: {format_price(prices[item])}")
            else:
                print("❌ Такого товару немає.")

        elif choice == "2":
            order = input("Введіть товари через кому: ").strip().lower().split(",")
            order = [item.strip() for item in order]
            process_order(order, stock, prices)

        elif choice == "3":
            print("👋 Дякуємо за відвідування!")
            break
        else:
            print("❌ Невірний вибір!")

if __name__ == "__main__":
    main()
