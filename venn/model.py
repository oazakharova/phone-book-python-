# считываем 1 раз справочник, кладем его в переменную и работаем дальше с ней - ближе к ООП


phone_book = []
path = 'venn\phone.txt'


def open_file():
    with open(path, 'r', encoding='UTF-8') as file:
        data = file.readlines()
    for fields in data:
        fields = fields.strip().split(';')
        contact = {'name': fields[0],
                   'phone': fields[1],
                   'comment': fields[2]}
        # открывается файл и в phone_book закидывается уже в виде словаря все, что есть
        phone_book.append(contact)


def get_phone_book():
    return phone_book


# можно называть так же, тк они в разных модулях, в разных файлах
def add_contact(contact: dict):
    phone_book.append(contact)


def change_contact(contact: dict, index: int):
    phone_book.pop(index-1)
    phone_book.insert(index-1, contact)


def save_file():
    data = []
    for contact in phone_book:
        data.append(';'.join(list(contact.values())))
    data = '\n'.join(data)
    with open(path, 'w', encoding='UTF-8') as file:
        file.write(data)


def find_contact(search: str) -> list[dict]:
    result = []
    for contact in phone_book:
        for field in contact.values():
            if search.lower() in field.lower():
                result.append(contact)
    return result


def delete_contact(search: str):
    # phone_book.remove(contact)
    result = []
    for contact in phone_book:
        for field in contact.values():
            if search.lower() in field.lower():
                phone_book.remove(contact)
    return result
