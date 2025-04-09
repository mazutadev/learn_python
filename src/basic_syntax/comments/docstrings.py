#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Примеры docstrings в Python
"""


def calculate_sum(a, b):
    """
    Вычисляет сумму двух чисел.

    Args:
        a (int): Первое число
        b (int): Второе число

    Returns:
        int: Сумма двух чисел

    Examples:
        >>> calculate_sum(2, 3)
        5
        >>> calculate_sum(-1, 1)
        0
    """
    return a + b


class Calculator:
    """
    Класс для выполнения математических операций.

    Attributes:
        version (str): Версия калькулятора
    """

    version = "1.0"

    def __init__(self):
        """
        Инициализирует новый экземпляр калькулятора.
        """
        pass

    def multiply(self, a, b):
        """
        Умножает два числа.

        Args:
            a (int): Первый множитель
            b (int): Второй множитель

        Returns:
            int: Произведение двух чисел
        """
        return a * b
