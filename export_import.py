# Ввод абсолютного пути

def get_file_name() -> str:
    return input('Введите имя файла: ')


# Импорт данных из текстового файла формата csv.

def get_batch_data(name_file: str) -> list: 
    lst = []
    with open(name_file, 'r', encoding='utf-8') as file:
        for line in file:
            lst.append(list(line.strip().split(';')))
    return lst


# Экспорт данных в текстовый файл формата csv.

def record_data(name_file, data): 
    with open (name_file, 'w', encoding = 'utf-8') as file:
        for el in data:
            file.write(f'{el[0]};{el[1]};{el[2]};{el[3]}\n')
