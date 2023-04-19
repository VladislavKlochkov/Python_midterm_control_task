from datetime import datetime

# Получение данных для заметки

def get_data() -> list:
    id = 1
    date = datetime.now().strftime("%Y-%m-%d %H:%M")
    name = input('Введите название заметки: ')
    content = input('Введите описание: ')
    return [id, date, name, content]


# Добавление записи в существующий журнал заметок.

def add_note(data: list, el: list) -> list:
    for element in data:
        for i in element:
            if i == el[0]:
                el[0] += 1
    data.append(el)
    return data


# Создание записи из данных в текстовом файле

def batch_create(data: list, batch_data) -> list:
    for el in batch_data:
        data = add_note(data, el)
    return data


# Сортировка заметок по дате

def sort_notes(data: list) -> list:
    return reversed(sorted(data, key=lambda x: datetime.strptime(x[1], '%Y-%m-%d %H:%M')))


# Вывод заметки

def print_note(record: list) -> None:
    print(f'"id"{record[0]}, {record[1]}, {record[2]}, {record[3]}')


# Вывод списка всех заметок

def print_notes(data: list) -> None:
    print(f'Заметки: ')
    for el in data:
        print_note(el)


# Выбор заметки по названию.

def select_note(data: list) -> list:
    note_name = input('Введите первые буквы названия заметки: ')
    for el in data:
        if note_name.casefold() in (el[2]).casefold():
            print(f'Вы выбрали заметку: ', el[2])
            return el


# Изменение полей выбранной заметки.

def update_note(data: list) -> list:
    change_note = select_note(data)

    while True:
        print('Выберите действие: ')
        print('0 - Выйти в главное меню')
        print('1 - Изменить название')
        print('2 - Изменить содержание')

        for el in data:
            if el == change_note:
                get_action = input('Введите действие: ')
                match get_action:
                    case '0':
                        print('Успешно!')
                        break
                    case '1':
                        change_note[2] = input('Введите новое название: ')
                    case '2':
                        change_note[3] = input('Заполните содержание: ')
                    case _:
                        print('Некорректный ввод данных!')
                change_note[1] = datetime.now().strftime("%Y-%m-%d %H:%M")
                el = change_note

        return data


# Удаление выбранной заметки

def delete_note(data: list) -> list:
    del_note = select_note(data)
    print(f'Вы удалили заметку: {del_note[2]}')
    for el in data:
        if el == del_note:
            data.remove(el)
            break
    return data
