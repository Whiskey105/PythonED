from csv import DictReader, DictWriter
from os.path import exists

class LenNumberError(RuntimeError):
    def __init__(self, txt):
        self.txt = txt

def get_info():
    is_valid_first_name = False
    while not is_valid_first_name:
        try:
            first_name = input('Введите имя: ')
            if len(first_name) < 2:
                raise LenNumberError('Невалидная длина!')
            else:
                is_valid_first_name = True
        except LenNumberError as err:
            print(err)
            continue
        
    is_valid_last_name = False
    while not is_valid_last_name:
        try:
            last_name = input('Введите фамилию: ')
            if len(last_name) < 2:
                raise LenNumberError('Невалидная длина!')
            else:
                is_valid_last_name = True
        except LenNumberError as err:
            print(err)
            continue
        

    is_valid_number = False
    while not is_valid_number:
        try:
            phone_number = int(input('Введите номер: '))
            if len(str(phone_number)) != 11:
                raise LenNumberError('Невалидная длина!')
            else:
                is_valid_number = True
        except ValueError:
            print('Невалидный номер!')
            continue
        except LenNumberError as err:
            print(err)
            continue

    return [first_name, last_name, phone_number]

def create_file(file_name):
    with open(file_name, 'w', encoding='utf-8') as data:
        f_writer = DictWriter(data, fieldnames=['имя','фамилия','телефон'])
        f_writer.writeheader()

def read_file(file_name):
    with open(file_name, 'r', encoding='utf-8') as data:
        f_reader = DictReader(data)
        return list(f_reader)
    
def wrtite_file(file_name):
    res = read_file(file_name)
    user_data = get_info()
    for el in res:
        if el['телефон'] == str(user_data[2]):
            print('Такой пользователь уже сущесвует!')
            return
    obj =  {'имя': user_data[0], 'фамилия': user_data[1],'телефон': user_data[2]}
    res.append(obj)
    with open(file_name, 'w', encoding='utf-8', newline='') as data:
        f_writer = DictWriter(data, fieldnames=['имя','фамилия','телефон'])
        f_writer.writeheader()
        f_writer.writerows(res)

def print_file(file_name):
    res = read_file(file_name)
    row = 0
    for el in res:
        print(row, el)
        row += 1

def copy_file(file_name, dest_name):
    source_list = read_file(file_name)
    print_file(file_name)
    is_valid_row_number = False
    while not is_valid_row_number:
        try:
            row_number = int(input('Введите номер строки для копирования: '))
            if row_number < 0 or row_number > len(source_list) - 1:
                raise LenNumberError('Невалидный номер строки!')
            else:
                is_valid_row_number = True
        except ValueError:
            print('Невалидный номер строки!')
            continue
        except LenNumberError as err:
            print(err)
            continue
    source_row = source_list[row_number]
    des =  read_file(dest_name)
    des.append(source_row)
    with open(dest_name, 'w', encoding='utf-8', newline='') as destination:
        f_writer = DictWriter(destination, fieldnames=['имя','фамилия','телефон'])
        f_writer.writeheader()
        f_writer.writerows(des)



file_name = 'phone.csv'
dest_name = 'output.csv'

def main():
    while True:
        command = input("Введите команду: ")
        if command == 'q':
            break
        elif command == 'w':
            if not exists(file_name):
                create_file(file_name)
            wrtite_file(file_name)
        elif command == 'r':
            if not exists(file_name):
                print('Файл не создан! Создайте файл!')
                continue
            print(*read_file(file_name))
        elif command == 'c':
            if not exists(dest_name):
                create_file(dest_name)
            copy_file(file_name, dest_name)
        elif command == 'p':
            if not exists(file_name):
                print('Файл не создан! Создайте файл!')
                continue
            print_file(file_name)
main()    
