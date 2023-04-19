import view
import functions as f
import export_import as ex


def menu(data: list):
    while True:
        
        get = view.show_menu()
        match get:
            case '0':
                print('До свидания!')
                break
            case '1':
                data = f.add_note(data, f.get_data())
            case '2':
                f.print_notes(f.sort_notes(data))
            case '3':
                f.select_note(data)
            case '4':
                f.update_note(data)
            case '5':
                f.delete_note(data)
            case '6':
                name_file = ex.get_file_name()
                batch_data = ex.get_batch_data(name_file)
                data = f.batch_create(data, batch_data)
            case '7':
                name_file = ex.get_file_name()
                f.sort_notes(data)
                ex.record_data(name_file, data)
            case _:
                print('Некорректный ввод данных!')

notes = []
menu(notes)