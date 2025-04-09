#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Примеры работы с файлами в Python
"""


# Запись в файл
def write_to_file():
    with open("example.txt", "w", encoding="utf-8") as f:
        f.write("Первая строка\n")
        f.write("Вторая строка\n")
        f.write("Третья строка\n")


# Чтение из файла
def read_from_file():
    with open("example.txt", "r", encoding="utf-8") as f:
        # Чтение всего файла
        content = f.read()
        print("Содержимое файла:")
        print(content)


# Чтение построчно
def read_lines():
    with open("example.txt", "r", encoding="utf-8") as f:
        print("Чтение построчно:")
        for line in f:
            print(line.strip())


# Добавление в файл
def append_to_file():
    with open("example.txt", "a", encoding="utf-8") as f:
        f.write("Новая строка\n")


# Работа с бинарными файлами
def binary_file():
    # Запись в бинарный файл
    with open("binary.bin", "wb") as f:
        f.write(b"Hello World")

    # Чтение из бинарного файла
    with open("binary.bin", "rb") as f:
        content = f.read()
        print(f"Бинарные данные: {content}")


# Обработка ошибок при работе с файлами
def safe_file_operations():
    try:
        with open("nonexistent.txt", "r") as f:
            content = f.read()
    except FileNotFoundError:
        print("Файл не найден")
    except IOError:
        print("Ошибка ввода-вывода")
    else:
        print("Файл успешно прочитан")
    finally:
        print("Операция завершена")
