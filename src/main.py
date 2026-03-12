def main():
    while True:
        print("\n--- Менеджер заметок ---")
        print("1. Добавить заметку")
        print("2. Показать все заметки")
        print("3. Удалить заметку по ID")
        print("4. Выход") #АнькаВстанька

        choice = input("Выбери действие (1-4): ")

        if choice == '1':
            title = input("Введи заголовок: ")
            body = input("Введи текст заметки: ")
            print(f"-> Здесь будет добавление заметки '{title}'")
        elif choice == '2':
            print("-> Здесь будет показ всех заметок")
        elif choice == '3':
            note_id = input("Введи ID заметки для удаления: ")
            print(f"-> Здесь будет удаление заметки с ID {note_id}")
        elif choice == '4':
            print("Выход...")
            break
        else:
            print("Неверный ввод, попробуй снова.")

if __name__ == "__main__":
    main()