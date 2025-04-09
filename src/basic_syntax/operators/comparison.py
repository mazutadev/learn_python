#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Примеры операторов сравнения в Python
"""

# Базовые операторы сравнения
a = 10
b = 5
c = 10

# Равно
print(f"{a} == {b}: {a == b}")  # False
print(f"{a} == {c}: {a == c}")  # True

# Не равно
print(f"{a} != {b}: {a != b}")  # True
print(f"{a} != {c}: {a != c}")  # False

# Больше
print(f"{a} > {b}: {a > b}")  # True
print(f"{a} > {c}: {a > c}")  # False

# Меньше
print(f"{a} < {b}: {a < b}")  # False
print(f"{a} < {c}: {a < c}")  # False

# Больше или равно
print(f"{a} >= {b}: {a >= b}")  # True
print(f"{a} >= {c}: {a >= c}")  # True

# Меньше или равно
print(f"{a} <= {b}: {a <= b}")  # False
print(f"{a} <= {c}: {a <= c}")  # True

# Сравнение строк
str1 = "hello"
str2 = "world"
str3 = "hello"

print(f"{str1} == {str2}: {str1 == str2}")  # False
print(f"{str1} == {str3}: {str1 == str3}")  # True
print(f"{str1} < {str2}: {str1 < str2}")  # True (лексикографическое сравнение)

# Сравнение с None
x = None
y = 10
print(f"x is None: {x is None}")  # True
print(f"y is None: {y is None}")  # False
