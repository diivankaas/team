from storage import NoteStorage
def main(storage = NoteStorage()):
        
    while True:
        print("\n--- Менеджер заметок ---")
        print("1. Добавить заметку")
        print("2. Показать все заметки")
        print("3. Удалить заметку по ID")
        print("4. Выход")

        choice = input("Выбери действие (1-4): ")

        if choice == '1':
            title = input("Введи заголовок: ")
            body = input("Введи текст заметки: ")
            storage.add_note(title, body)
        elif choice == '2':
            storage.get_all_notes()
        elif choice == '3':
            note_id = int(input("Введи ID заметки для удаления: "))
            storage.remove_note(note_id)
        elif choice == '4':
            print("Выход...")
            break
        else:
            print("Неверный ввод, попробуй снова.")

if __name__ == "__main__":
    main()