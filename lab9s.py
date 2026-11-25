import os


# Функция объединения файлов
def merge_files(file1, file2, output_file):
    try:
        with open(output_file, "wb") as result:
            for filename in [file1, file2]:
                with open(filename, "rb") as source:
                    result.write(source.read())

        print("Файлы успешно объединены")

    except FileNotFoundError:
        print("Ошибка: файл не найден")

    except OSError:
        print("Ошибка при работе с файлами")


# Функция разделения файла
def split_file(filename, size):
    try:
        with open(filename, "rb") as source:
            part_number = 1

            while True:
                data = source.read(size)

                if not data:
                    break

                part_name = f"part_{part_number}.bin"

                with open(part_name, "wb") as part:
                    part.write(data)

                part_number += 1

        print("Файл успешно разделён на части")

    except FileNotFoundError:
        print("Ошибка: файл не найден")

    except OSError:
        print("Ошибка при работе с файлами")


# Функция ввода данных
def input_data():
    file1 = input("Введите имя первого файла: ")
    file2 = input("Введите имя второго файла: ")
    output_file = input("Введите имя объединённого файла: ")
    return file1, file2, output_file


# Основная часть программы
file1, file2, output_file = input_data()

merge_files(file1, file2, output_file)

split_file(output_file, 1024)