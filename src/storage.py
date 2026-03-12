class NoteStorage:
    def __init__(self):
        self.notes = []
        self.id_counter = 1

    def add_note(self, title, body):
        note = [self.id_counter, title, body]
        self.notes.append(note)
        print(f"Добавлена заметка {self.id_counter}")
        self.id_counter += 1

    def get_all_notes(self):
        if len(self.notes) == 0:
            print("Заметок нет")
        else:
            for note in self.notes:
                print(f"{note[0]}. {note[1]} - {note[2]}")

    def remove_note(self, note_id):
        for note in self.notes:
            if note[0] == note_id:
                self.notes.remove(note)
                print(f"Удалена заметка {note_id}")
                return
        print(f"Заметка {note_id} не найдена")
        # Это написала ДИАНА

