#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Примеры логических операторов в Python
"""

# Логические операторы
a = True
b = False

# Логическое И (and)
print(f"{a} and {b}: {a and b}")  # False
print(f"{a} and {a}: {a and a}")  # True
print(f"{b} and {b}: {b and b}")  # False

# Логическое ИЛИ (or)
print(f"{a} or {b}: {a or b}")  # True
print(f"{a} or {a}: {a or a}")  # True
print(f"{b} or {b}: {b or b}")  # False

# Логическое НЕ (not)
print(f"not {a}: {not a}")  # False
print(f"not {b}: {not b}")  # True

# Комбинированные операции
print(f"not ({a} and {b}): {not (a and b)}")  # True
print(f"not {a} or not {b}: {not a or not b}")  # True


# Короткое замыкание (short-circuit evaluation)
def return_true():
    print("Функция return_true вызвана")
    return True


def return_false():
    print("Функция return_false вызвана")
    return False


# В случае and, если первое значение False, второе не вычисляется
print("Пример короткого замыкания с and:")
result = return_false() and return_true()  # return_true не будет вызвана

# В случае or, если первое значение True, второе не вычисляется
print("\nПример короткого замыкания с or:")
result = return_true() or return_false()  # return_false не будет вызвана
