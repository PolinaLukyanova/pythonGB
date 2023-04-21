# Задача №49. Общее обсуждение
# Создать телефонный справочник с
# возможностью импорта и экспорта данных в
# формате .txt. Фамилия, имя, отчество, номер
# телефона - данные, которые должны находиться
# в файле.
# 1. Программа должна выводить данные
# 2. Программа должна сохранять данные в
# текстовом файле
# 3. Пользователь может ввести одну из
# характеристик для поиска определенной
# записи(Например имя или фамилию
# человека)
# 4. Использование функций. Ваша программа
# не должна быть линейной


def console_file():
    pass

def read_file():
    with open(path_file, 'r', encoding='UTF-8') as f:
        for line in f:
            print(line.strip())

def write_file():
    with open(path_file, 'a', encoding='UTF-8') as f:
        f.writelines('\n'+input())


def find_file():
    find_info = input()
    with open(path_file, 'r', encoding='UTF-8') as f:
        for line in f:
            if find_info in line:
                print(line)




def main():
    find_file()

path_file = r'phonebook.txt'
if __name__ == '__main__':
    main()