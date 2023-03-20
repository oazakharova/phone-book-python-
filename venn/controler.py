import view
import model


def start():
    while True:
        choice = view.main_menu()
        match choice:  # условие выбора
            case 1:
                model.open_file()
                view.show_message('Файл успешно открыт')
            case 2:
                model.save_file()
                view.show_message('Файл успешно сохранен')
            case 3:
                pb = model.get_phone_book()
                view.show_contacts(pb, 'Телефонная книга пуста или не открыта')
            case 4:
                contact = view.add_contact()
                model.add_contact(contact)
            case 5:
                pb = model.get_phone_book()
                if view.show_contacts(pb, 'Телефонная книга пуста или не открыта'):
                    index = view.input_index(
                        "Введите номер изменяемого контакта: ")
                    contact = view.change_contact(pb, index)
                    model.change_contact(contact, index)
                    view.show_message(
                        f'Контакт {model.get_phone_book()[index-1].get("name")} успешно изменен')
            case 6:
                search = view.input_search('Введите искомый элемент: ')
                result = model.find_contact(search)
                view.show_contacts(result, 'Контакты не найдены')
            case 7:
                search = view.input_search('Введите элемент для удаления: ')
                model.delete_contact(search)
                view.show_message(
                    f'Контакт удален')
            case 8:
                return
            # аналог else - если не 1-8. В данном случае остальных случаев быть не может, тк был сделан обработчик событиев (во view с помощью ленивого if):
            case _:
                pass  # заглушка
