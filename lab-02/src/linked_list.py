# Структура узла связного списка
class Node:
    """Узел односвязного списка.
    
    Атрибуты:
        data: Любые данные, хранящиеся в узле.
        next: Ссылка на следующий узел (None, если узел последний).
    """
    __slots__ = ('data', 'next')

    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    """Односвязный список с поддержкой head и tail указателей.
    
    Поддерживает вставку в начало за O(1) и в конец за O(1) при использовании tail.
    """

    def __init__(self):
        self.head = None  # Первый элемент списка
        self.tail = None  # Последний элемент списка (для O(1) вставки в конец)

    def insert_at_start(self, data):
        """Вставка элемента в начало списка. Сложность: O(1)."""
        new_node = Node(data)
        if self.head is None:
            # Список был пуст — обновляем и head, и tail
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head = new_node

    def insert_at_end(self, data):
        """Вставка элемента в конец списка. Сложность: O(1) благодаря tail."""
        new_node = Node(data)
        if self.tail is None:
            # Список был пуст
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node

    def delete_from_start(self):
        """Удаление первого элемента списка. Сложность: O(1).
        
        Возвращает данные удалённого элемента или None, если список пуст.
        """
        if self.head is None:
            return None  # Список пуст

        removed_data = self.head.data
        if self.head == self.tail:
            # Был только один элемент
            self.head = None
            self.tail = None
        else:
            self.head = self.head.next
        return removed_data

    def traversal(self):
        """Обход списка и возврат элементов в виде списка. Сложность: O(n)."""
        result = []
        current = self.head
        while current is not None:
            result.append(current.data)
            current = current.next
        return result