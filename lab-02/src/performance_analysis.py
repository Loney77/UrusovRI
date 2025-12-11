# performance_plots.py
# Самодостаточный скрипт для построения графиков производительности

import timeit
from collections import deque
import matplotlib.pyplot as plt


# === Минимальная реализация LinkedList (только для вставки в начало) ===
class Node:
    __slots__ = ('data', 'next')
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def insert_at_start(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    # delete_from_start и traversal не нужны для бенчмарка, пропускаем


# === Функции замеров ===
def benchmark_list_insert_start(n: int) -> float:
    lst = []
    start = timeit.default_timer()
    for i in range(n):
        lst.insert(0, i)
    return timeit.default_timer() - start


def benchmark_linkedlist_insert_start(n: int) -> float:
    ll = LinkedList()
    start = timeit.default_timer()
    for i in range(n):
        ll.insert_at_start(i)
    return timeit.default_timer() - start


def benchmark_list_pop_start(n: int) -> float:
    lst = list(range(n))
    start = timeit.default_timer()
    for _ in range(n):
        lst.pop(0)
    return timeit.default_timer() - start


def benchmark_deque_pop_start(n: int) -> float:
    dq = deque(range(n))
    start = timeit.default_timer()
    for _ in range(n):
        dq.popleft()
    return timeit.default_timer() - start


# === Запуск замеров ===
sizes = list(range(100, 1001, 100))  # от 100 до 1000 с шагом 100

list_insert_times = []
linkedlist_insert_times = []
list_pop_times = []
deque_pop_times = []

for n in sizes:
    list_insert_times.append(benchmark_list_insert_start(n))
    linkedlist_insert_times.append(benchmark_linkedlist_insert_start(n))
    list_pop_times.append(benchmark_list_pop_start(n))
    deque_pop_times.append(benchmark_deque_pop_start(n))


# === Построение графиков ===
plt.style.use('seaborn-v0_8-whitegrid')
plt.figure(figsize=(14, 6))

# График 1: Вставка в начало
plt.subplot(1, 2, 1)
plt.plot(sizes, list_insert_times, label='list.insert(0, x)', marker='o', linewidth=2)
plt.plot(sizes, linkedlist_insert_times, label='LinkedList.insert_at_start', marker='s', linewidth=2)
plt.title('Вставка в начало: list vs LinkedList\n(теория: O(n) vs O(1))', fontsize=12)
plt.xlabel('Количество операций')
plt.ylabel('Время (сек)')
plt.legend()
plt.grid(True, linestyle='--', alpha=0.7)

# График 2: Удаление из начала (очередь)
plt.subplot(1, 2, 2)
plt.plot(sizes, list_pop_times, label='list.pop(0)', marker='o', linewidth=2)
plt.plot(sizes, deque_pop_times, label='deque.popleft()', marker='s', linewidth=2)
plt.title('Удаление из начала: list vs deque\n(теория: O(n) vs O(1))', fontsize=12)
plt.xlabel('Количество операций')
plt.ylabel('Время (сек)')
plt.legend()
plt.grid(True, linestyle='--', alpha=0.7)

plt.tight_layout(pad=3.0)
plt.savefig('performance_comparison.png', dpi=200, bbox_inches='tight')
plt.show()