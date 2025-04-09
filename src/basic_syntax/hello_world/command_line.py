#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Пример скрипта, который можно запустить из командной строки
"""

import sys


def main():
    """
    Основная функция скрипта
    """
    # Проверяем, были ли переданы аргументы командной строки
    if len(sys.argv) > 1:
        name = sys.argv[1]
    else:
        name = "World"

    print(f"Hello, {name}!")


if __name__ == "__main__":
    main()
