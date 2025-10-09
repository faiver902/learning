from typing import TextIO

lines = ["Hello Word\n", "Hello Work\n", "Hello World\n"]


def open_file(name, mode, *args, **kwargs):
    return open(name, mode, encoding="utf8", *args, **kwargs)


file = open_file("hello2.txt", "a+")


def write_file(file: TextIO, content):
    print(content, file=file)
    print("Список строк записан в файл")


def read_file_1(file: TextIO):
    file.seek(0)
    for line in file:
        print(line, end="")


def read_line(file: TextIO):
    file.seek(0)
    str_1 = file.readline()
    while str_1:
        print(str_1)
        str_1 = file.readline()


def read_all(file: TextIO):
    file.seek(0)
    content = file.read()
    print(content)


def write_read(file):
    def write():
        message = input("Введите строку: ")
        file.write(message + "\n")

    def read():
        file.seek(0)
        for message in file:
            print(message, end="")
        print()

    while True:
        selection = int(
            input("1.Запись в файл\t\t2.Чтение файла\t\t3.Выход\nВыберите действие: ")
        )
        match selection:
            case 1:
                write()
            case 2:
                read()
            case 3:
                break
            case _:
                print("Некорректный ввод")

    print("Программа завершена")


if __name__ == "__main__":
    try:
        # write_file(file, content)
        # read_file_1(file)
        # read_line(file)
        # read_all(file)
        write_read(file)
    finally:
        file.close()
