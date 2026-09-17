items = []  # список товарів, кожен товар - це словник 


def add_item(name, price):
    # додає товар у список
    items.append({"name": name, "price": price})
    print(f"Товар '{name}' доданий у список.")


def total_price():
    # підраховує загальну суму покупок
    total = 0
    for item in items:
        total = total + item["price"]
    return total


def show_items():
    # виводить список товарів та їхні ціни
    if len(items) == 0:
        print("Список товарів порожній.")
        return

    print("\nСписок покупок:")
    for item in items:
        print(f"- {item['name']}: {item['price']} грн")


def main():
    while True:
        print("\n===== Калькулятор покупок =====")
        print("1. Додати товар")
        print("2. Показати товари")
        print("3. Показати загальну суму")
        print("4. Вийти")

        choice = input("Оберіть пункт меню: ")

        if choice == "1":
            name = input("Введіть назву товару: ")
            price = float(input("Введіть ціну товару: "))
            add_item(name, price)

        elif choice == "2":
            show_items()

        elif choice == "3":
            print(f"Загальна сума покупок: {total_price()} грн")

        elif choice == "4":
            print("Дякую за використання програми!")
            break

        else:
            print("Такого пункту немає, спробуйте ще раз.")


main()