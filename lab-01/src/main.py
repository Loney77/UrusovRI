import random
import time
from typing import List, Optional

import matplotlib.pyplot as pyplot
import numpy


def linear_search(arr: List[int], target: int) -> Optional[int]:
    """
    Линейный поиск элемента в массиве.

    Args:
        arr: Массив для поиска
        target: Искомый элемент

    Returns:
        Индекс элемента или None если не найден
    """
    for i in range(len(arr)):  # O(n) - цикл по всем элементам
        if arr[i] == target:  # O(1) - сравнение
            return i  # O(1) - возврат результата
    return None  # O(1) - возврат None
    # Общая сложность: O(n)


def binary_search(arr: List[int], target: int) -> Optional[int]:
    """
    Бинарный поиск элемента в отсортированном массиве.

    Args:
        arr: Отсортированный массив
        target: Искомый элемент

    Returns:
        Индекс элемента или None если не найден
    """
    left = 0  # O(1) - инициализация
    right = len(arr) - 1  # O(1) - инициализация

    while left <= right:  # O(log n) -  уменьшает диапазон в 2 раза на шаг
        mid = (left + right) // 2  # O(1) - вычисление середины
        if arr[mid] == target:  # O(1) - сравнение
            return mid  # O(1) - возврат результата
        elif arr[mid] < target:  # O(1) - сравнение
            left = mid + 1  # O(1) - обновление левой границы
        else:
            right = mid - 1  # O(1) - обновление правой границы

    return None  # O(1) - возврат None
    # Общая сложность: O(log n)


def generate_sorted_array(size: int) -> List[int]:
    """Генерирует отсортированный массив заданного размера."""
    return sorted(random.sample(range(size * 10), size))


def measure_search_time(
    search_func, arr: List[int], target: int, iterations: int = 100
) -> float:
    """
    Измеряет среднее время выполнения функции поиска.

    Args:
        search_func: Функция поиска
        arr: Массив для поиска
        target: Искомый элемент
        iterations: Количество итераций для усреднения

    Returns:
        Среднее время выполнения в секундах
    """
    total_time = 0.0

    for _ in range(iterations):
        start_time = time.perf_counter()  # O(1)
        search_func(arr, target)  # Сложность зависит от search_func
        end_time = time.perf_counter()  # O(1)
        total_time += end_time - start_time  # O(1)

    return total_time / iterations  # O(1)


def main():
    """Основная функция для проведения экспериментов."""
    # Характеристики ПК (заполнить своими данными)
    pc_info = """
    Характеристики ПК для тестирования:
    - Процессор: Intel Core i7-1165G7 @ 2.80GHz
    - Оперативная память: 16 GB DDR4
    - ОС: Windows 10
    - Python: 3.13
    """
    print(pc_info)

    # Параметры эксперимента
    sizes = [1000, 2000, 5000, 10000, 20000,
             50000, 100000, 200000, 500000, 1000000]
    iterations = 50

    # Результаты
    linear_times = []
    binary_times = []

    print("Запуск экспериментов...")
    print(f"Размеры массивов: {sizes}")
    print(f"Итераций на каждый размер: {iterations}")
    print("-" * 60)

    for size in sizes:
        print(f"Тестирование размера {size}...")

        # Генерация отсортированного массива
        arr = generate_sorted_array(size)

        # Выбор целевых элементов для тестирования
        middle_element = arr[size // 2]  # O(1)
        missing_element = -1  # O(1) - гарантированно отсутствует

        # Тестирование линейного поиска (худший случай - отсутствующий элемент)
        linear_time = measure_search_time(
            linear_search, arr, missing_element, iterations
        )
        linear_times.append(linear_time)

        # Тестирование бинарного поиска (средний случай)
        binary_time = measure_search_time(
            binary_search, arr, middle_element, iterations
        )
        binary_times.append(binary_time)

        print(f"  Линейный поиск: {linear_time:.8f} сек")
        print(f"  Бинарный поиск: {binary_time:.8f} сек")

    # Визуализация результатов
    plot_results(sizes, linear_times, binary_times)


def plot_results(
    sizes: List[int], linear_times: List[float], binary_times: List[float]
):
    """
    Строит графики результатов экспериментов.

    Args:
        sizes: Размеры массивов
        linear_times: Времена линейного поиска
        binary_times: Времена бинарного поиска
    """
    pyplot.figure(figsize=(15, 6))

    # График 1: Линейная шкала
    pyplot.subplot(1, 2, 1)
    pyplot.plot(sizes, linear_times, "b-o",
                label="Линейный поиск O(n)", linewidth=2)
    pyplot.plot(sizes, binary_times, "r-o",
                label="Бинарный поиск O(log n)", linewidth=2)
    pyplot.xlabel("Размер массива")
    pyplot.ylabel("Время выполнения (сек)")
    pyplot.title("Сравнение алгоритмов поиска (линейная шкала)")
    pyplot.legend()
    pyplot.grid(True, alpha=0.3)

    # График 2: Логарифмическая шкала по осям
    pyplot.subplot(1, 2, 2)
    pyplot.loglog(sizes, linear_times, "b-o",
                  label="Линейный поиск O(n)", linewidth=2)
    pyplot.loglog(sizes, binary_times, "r-o",
                  label="Бинарный поиск O(log n)", linewidth=2)
    pyplot.xlabel("Размер массива(log scale)")
    pyplot.ylabel("Время выполнения(log scale)")
    pyplot.title("Сравнение алгоритмов поиска(логарифмическая шкала)")
    pyplot.legend()
    pyplot.grid(True, alpha=0.3)

    pyplot.tight_layout()
    pyplot.savefig("search_comparison.png", dpi=300, bbox_inches="tight")
    pyplot.show()

    # Дополнительный анализ
    analyze_complexity(sizes, linear_times, binary_times)


def analyze_complexity(
    sizes: List[int], linear_times: List[float], binary_times: List[float]
):
    """
    Анализирует соответствие теоретической сложности практическим результатам.

    Args:
        sizes: Размеры массивов
        linear_times: Времена линейного поиска
        binary_times: Времена бинарного поиска
    """
    print("\n" + "=" * 60)
    print("АНАЛИЗ РЕЗУЛЬТАТОВ")
    print("=" * 60)

    # Анализ линейного поиска
    print("ЛИНЕЙНЫЙ ПОИСК (O(n)):")
    ratios = []
    for i in range(1, len(sizes)):
        time_ratio = linear_times[i] / linear_times[i - 1]
        size_ratio = sizes[i] / sizes[i - 1]
        ratios.append(time_ratio / size_ratio)
        print(
            f"  Размер {sizes[i-1]} -> {sizes[i]}: "
            f"время увел. в {time_ratio:.2f} раз, "
            f"ожидалось {size_ratio:.2f} раз"
        )

    avg_ratio = sum(ratios) / len(ratios)
    print(f"  Среднее соответствие теоретической сложности: {avg_ratio:.2f}")

    # Анализ бинарного поиска
    print("\nБИНАРНЫЙ ПОИСК (O(log n)):")
    log_ratios = []
    for i in range(1, len(sizes)):
        time_ratio = binary_times[i] / binary_times[i - 1]
        expected_log_ratio = numpy.log2(sizes[i]) / numpy.log2(sizes[i - 1])
        log_ratios.append(time_ratio / expected_log_ratio)
        print(
            f"  Размер {sizes[i-1]} -> {sizes[i]}: "
            f"время увел. в {time_ratio:.2f} раз, "
            f"ожидалось ~{expected_log_ratio:.2f} раз"
        )

    avg_log_ratio = sum(log_ratios) / len(log_ratios)
    print(
        f"  Среднее соответствие теоретической сложности: {avg_log_ratio:.2f}")


if __name__ == "__main__":
    main()

# Результаты:
"""
Характеристики ПК для тестирования:
    - Процессор: Intel Core i7-1165G7 @ 2.80GHz
    - Оперативная память: 16 GB DDR4
    - ОС: Windows 10
    - Python: 3.13

Запуск экспериментов...
Размеры массивов: [1000, 2000, 5000, 10000, 20000, 50000,
100000, 200000, 500000, 1000000]
Итераций на каждый размер: 50
------------------------------------------------------------
Тестирование размера 1000...
  Линейный поиск: 0.00003176 сек
  Бинарный поиск: 0.00000120 сек
Тестирование размера 2000...
  Линейный поиск: 0.00020053 сек
  Бинарный поиск: 0.00000411 сек
Тестирование размера 5000...
  Линейный поиск: 0.00047991 сек
  Бинарный поиск: 0.00000329 сек
Тестирование размера 10000...
  Линейный поиск: 0.00071152 сек
  Бинарный поиск: 0.00000325 сек
Тестирование размера 20000...
  Линейный поиск: 0.00109824 сек
  Бинарный поиск: 0.00000227 сек
Тестирование размера 50000...
  Линейный поиск: 0.00593425 сек
  Бинарный поиск: 0.00000526 сек
Тестирование размера 100000...
  Линейный поиск: 0.00769390 сек
  Бинарный поиск: 0.00000271 сек
Тестирование размера 200000...
  Линейный поиск: 0.02120470 сек
  Бинарный поиск: 0.00000329 сек
Тестирование размера 500000...
  Линейный поиск: 0.07812537 сек
  Бинарный поиск: 0.00001196 сек
Тестирование размера 1000000...
  Линейный поиск: 0.19829873 сек
  Бинарный поиск: 0.00000500 сек

============================================================
АНАЛИЗ РЕЗУЛЬТАТОВ
============================================================
ЛИНЕЙНЫЙ ПОИСК (O(n)):
  Размер 1000 -> 2000: время увел. в 6.31 раз, ожидалось 2.00 раз
  Размер 2000 -> 5000: время увел. в 2.39 раз, ожидалось 2.50 раз
  Размер 5000 -> 10000: время увел. в 1.48 раз, ожидалось 2.00 раз
  Размер 10000 -> 20000: время увел. в 1.54 раз, ожидалось 2.00 раз
  Размер 20000 -> 50000: время увел. в 5.40 раз, ожидалось 2.50 раз
  Размер 50000 -> 100000: время увел. в 1.30 раз, ожидалось 2.00 раз
  Размер 100000 -> 200000: время увел. в 2.76 раз, ожидалось 2.00 раз
  Размер 200000 -> 500000: время увел. в 3.68 раз, ожидалось 2.50 раз
  Размер 500000 -> 1000000: время увел. в 2.54 раз, ожидалось 2.00 раз
  Среднее соответствие теоретической сложности: 1.40

БИНАРНЫЙ ПОИСК (O(log n)):
  Размер 1000 -> 2000: время увел. в 3.43 раз, ожидалось ~1.10 раз
  Размер 2000 -> 5000: время увел. в 0.80 раз, ожидалось ~1.12 раз
  Размер 5000 -> 10000: время увел. в 0.99 раз, ожидалось ~1.08 раз
  Размер 10000 -> 20000: время увел. в 0.70 раз, ожидалось ~1.08 раз
  Размер 20000 -> 50000: время увел. в 2.32 раз, ожидалось ~1.09 раз
  Размер 50000 -> 100000: время увел. в 0.51 раз, ожидалось ~1.06 раз
  Размер 100000 -> 200000: время увел. в 1.22 раз, ожидалось ~1.06 раз
  Размер 200000 -> 500000: время увел. в 3.64 раз, ожидалось ~1.08 раз
  Размер 500000 -> 1000000: время увел. в 0.42 раз, ожидалось ~1.05 раз
  Среднее соответствие теоретической сложности: 1.44
"""
