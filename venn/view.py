import text_fields


def main_menu() -> int:
    print(text_fields.main_menu)
    # теперь не нужно исправлять в разных частях программы длину, если что-то будет добавлено в пункты меню
    length_menu = len(text_fields.main_menu.split('\n')) - 1
    while True:
        choice = input('Выберите пункт меню: ')
        if choice.isdigit() and 0 < int(choice) <= length_menu:
            # метод ленивого if - сначала проверяется, число ли введено, тк если нет, то дальше проверка не будет проводиться, тк будет уже false, поэтому, если ввести букву, ошибки не будет, а значит, программа не сломается
            return int(choice)
        else:
            print(f'Введите число от 1 до {length_menu}: ')


def show_contacts(book: list[dict], error_message: str):
    if not book:
        print(error_message)
        return False
    else:
        for i, contact in enumerate(book, 1):
            print(f'{i}. {contact.get("name"):<20} '
                  f'{contact.get("phone"):<20} '
                  f'{contact.get("comment"):<20} ')  # форматирование строк - под содержимое переменной до двоеточия оставляется 20 символов, если меньше 20 символов - ровнение по левому краю - чтобы смотрелось как таблица
        return True


def add_contact() -> dict:
    name = input('Введите имя: ')
    phone = input('Введите номер телефона: ')
    comment = input('Введите комментарий: ')
    return {'name': name, 'phone': phone, 'comment': comment}


def input_index(message: str):
    return int(input(message))


def change_contact(book: list[dict], index: int):
    print('Введите новые данные или оставьте пустое поле, если нет изменений')
    contact = add_contact()
    return {'name': contact.get('name') if contact.get('name') else book[index-1].get('name'),
            'phone': contact.get('phone') if contact.get('phone') else book[index-1].get('phone'),
            'comment': contact.get('comment') if contact.get('comment') else book[index-1].get('comment')}
    book[index-1]


def show_message(message: str):
    print('-'*len(message))  # красивучие черточки, магия
    print(message)
    print('-'*len(message))


def input_search(message):
    return input(message)


# def delete_contact(message):
#     return input(message)
