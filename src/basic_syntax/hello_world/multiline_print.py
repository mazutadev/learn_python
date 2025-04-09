#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Примеры многострочного вывода в Python
"""

# Многострочный вывод с использованием тройных кавычек
print(
    """
Hello,
World!
"""
)

# Многострочный вывод с использованием escape-последовательностей
print("Hello,\nWorld!")

# Многострочный вывод с использованием нескольких вызовов print
print("Hello,")
print("World!")

# Многострочный вывод с использованием списка
lines = ["Hello,", "World!"]
print("\n".join(lines))

# Многострочный вывод с форматированием
name = "Python"
print(
    f"""
Hello,
{name}!
"""
)
