#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Примеры побитовых операторов в Python
"""

# Побитовые операторы
a = 0b1010  # 10 в десятичной
b = 0b1100  # 12 в десятичной

# Побитовое И (AND)
print(f"{bin(a)} & {bin(b)} = {bin(a & b)}")  # 0b1000 (8)

# Побитовое ИЛИ (OR)
print(f"{bin(a)} | {bin(b)} = {bin(a | b)}")  # 0b1110 (14)

# Побитовое исключающее ИЛИ (XOR)
print(f"{bin(a)} ^ {bin(b)} = {bin(a ^ b)}")  # 0b0110 (6)

# Побитовое НЕ (NOT)
print(f"~{bin(a)} = {bin(~a)}")  # -0b1011 (-11)

# Побитовый сдвиг влево
print(f"{bin(a)} << 2 = {bin(a << 2)}")  # 0b101000 (40)

# Побитовый сдвиг вправо
print(f"{bin(a)} >> 2 = {bin(a >> 2)}")  # 0b0010 (2)


# Практический пример: проверка битов
def check_bit(number, bit_position):
    mask = 1 << bit_position
    return (number & mask) != 0


# Проверка битов числа 10 (0b1010)
print("\nПроверка битов числа 10:")
for i in range(4):
    print(f"Бит {i}: {check_bit(a, i)}")


# Установка бита
def set_bit(number, bit_position):
    mask = 1 << bit_position
    return number | mask


# Сброс бита
def clear_bit(number, bit_position):
    mask = ~(1 << bit_position)
    return number & mask


# Примеры установки и сброса битов
print("\nУстановка и сброс битов:")
number = 0b1010
print(f"Исходное число: {bin(number)}")
number = set_bit(number, 1)
print(f"После установки бита 1: {bin(number)}")
number = clear_bit(number, 3)
print(f"После сброса бита 3: {bin(number)}")
