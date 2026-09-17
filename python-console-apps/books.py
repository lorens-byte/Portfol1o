import json
import os

FILE_NAME = "books.json"


def load_books():
    # завантажує список книг з файлу books.json
    if not os.path.exists(FILE_NAME):
        return []

    with open(FILE_NAME, "r", encoding="utf-8") as f:
        books = json.load(f)
    return books


def save_books(books):
    # зберігає список книг у файл books.json
    with open(FILE_NAME, "w", encoding="utf-8") as f:
        json.dump(books, f, ensure_ascii=False, indent=4)


def add_book():
    # додає нову книгу і зберігає в файл
    books = load_books()

    title = input("Введіть назву книги: ")
    author = input("Введіть автора книги: ")
    year = input("Введіть рік видання: ")

    new_book = {"назва": title, "автор": author, "рік": year}
    books.append(new_book)

    save_books(books)
    print(f"Книга '{title}' додана до колекції.")


def delete_book():
    # видаляє книгу за назвою і зберігає зміни в файл
    books = load_books()
    title = input("Введіть назву книги, яку треба видалити: ")

    new_books = []
    found = False
    for book in books:
        if book["назва"] == title:
            found = True
        else:
            new_books.append(book)

    if found:
        save_books(new_books)
        print(f"Книга '{title}' видалена.")
    else:
        print("Книгу з такою назвою не знайдено.")


def show_books():
    # показує всі книги зі списку
    books = load_books()

    if len(books) == 0:
        print("Колекція книг порожня.")
        return

    print("\nСписок книг:")
    for book in books:
        print(f"- {book['назва']} | {book['автор']} | {book['рік']} рік")


def main():
    while True:
        print("\n===== Колекція книг =====")
        print("1. Додати книгу")
        print("2. Видалити книгу за назвою")
        print("3. Показати всі книги")
        print("4. Вийти")

        choice = input("Оберіть пункт меню: ")

        if choice == "1":
            add_book()

        elif choice == "2":
            delete_book()

        elif choice == "3":
            show_books()

        elif choice == "4":
            print("Дякую за використання програми!")
            break

        else:
            print("Такого пункту немає, спробуйте ще раз.")


main()