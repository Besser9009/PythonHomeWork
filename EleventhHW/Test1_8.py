from os import path

file_base = "base.txt"
last_id = 0
all_data = []

if not path.exists(file_base):
    with open(file_base, "w", encoding="utf-8") as f:
        pass

def read_records():
    global all_data, last_id

    with open(file_base, encoding="utf-8") as f:
        all_data = [i.strip() for i in f]
        if all_data:
            last_id = int(all_data[-1].split()[0])
            return all_data
    return []

def show_all():
    if all_data:
        print(*all_data, sep="\n")
    else:
        print("Нет данных!\n1")

def add_new_contact():
    global last_id
    array = ["Фамилию", "Имя", "Отчество", "Номер телефона"]
    string = ""
    for i in array:
        string += input(f"Введите {i} ") + " "
    last_id += 1

    with open(file_base, "a", encoding="utf-8") as f:
        f.write(f"{last_id} {string}\n")


def search_contact():
    search_data = exist_contact(0, input("Введите искомые данные: "))
    if search_data:
        print(*search_data, sep="\n")
    else:
        print("Данные не корректны или записаны не верно...")

def change_contact(data_tuple):
    global all_data
    symbol = "\n"

    record_id, num_data, data = data_tuple

    for i, v in enumerate(all_data):
        if v.split()[0] == record_id:
            v = v.split()
            v[int(num_data)] = data
            if exist_contact(0, " ".join(v[1:])):
                print("Данные уже существуют :)")
                return
            all_data[i] = " ".join(v)
            break

    with open(file_base, 'w', encoding="utf-8") as f:
        f.write(f'{symbol.join(all_data)}\n')
    print("Запись изменена\n")

def del_contact():
    global all_data

    symbol = "\n"
    show_all()
    del_record = input("Введите id записи: ")

    if exist_contact(del_record, ""):
        all_data = [k for k in all_data if k.split()[0] != del_record]

        with open(file_base, 'w', encoding="utf-8") as f:
            f.write(f'{symbol.join(all_data)}\n')
        print("Запись удалена!\n")
    else:
        print("Данные не коректны...")

def main_menu():
    play = True
    while play:
        read_records()
        answer = input("Записная книга:\n"
                       "1. Показать все контакта\n"
                       "2. Добавить контакт\n"
                       "3. Поиск контакта\n"
                       "4. Изменить контакт\n"
                       "5. Удалить контакт\n"
                       "6. Выход\n")
        match answer:
            case "1":
                show_all()
            case "2":
                add_new_contact()
            case "3":
                search_contact()
            case "4":
                work = edit_menu()
                if work:
                    change_contact(work)
            case "5":
                del_contact()
            case "6":
                play = False
            case _:
                print("Введите другой пункт в меню!\n")

def exist_contact(rec_id, data):
    if rec_id:
        candidates = [i for i in all_data if rec_id in i.split()[0]]
    else:
        candidates = [i for i in all_data if data in i]
    return candidates

def data_collection(num):
    answer = input(f"Введите {num}: ")
    while True:
        if num in "Фамилия Имя Отчество":
            if answer.isalpha():
                break
        if num == "телефонный номер":
            if answer.isdigit() and len(answer) == 11:
                break
        answer = input(f"Данные в порядке\n"
                       f"Используйте только буквы из алфавита"
                       f"Номер состоит из 11 чисел\n"
                       f"Введите {num}: ")
    return answer

def edit_menu():
    add_dict = {"1": "Фамилию", "2": "Имя", "3": "Отчество", "4": "Номер телефона"}

    show_all()
    record_id = input("Введите искомый id: ")
    if exist_contact(record_id, ""):
        while True:
            print("\nХочу изменить: ")
            change = input("1. Фамилию\n"
                           "2. Имя\n"
                           "3. Отчество\n"
                           "4. Номер телефона\n"
                           "5. Выход")
            match change:
                case "1" | "2" | "3" | "4":
                    return record_id, change, data_collection(add_dict[change])
                case "5":
                    return 0
                case _:
                    print("Такого пункта нет, введите другой номер пункта.")
    else:
        print("Введённые вами данные не коректны...")

main_menu()