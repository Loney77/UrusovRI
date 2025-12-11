from collections import deque

def is_balanced_brackets(expression: str) -> bool:
    """Проверяет сбалансированность скобок в строке с использованием стека (list).
    
    Поддерживаемые скобки: (), [], {}.
    Сложность: O(n).
    """
    stack = []
    mapping = {')': '(', ']': '[', '}': '{'}

    for char in expression:
        if char in mapping.values():
            stack.append(char)  # Открывающая скобка — кладём в стек
        elif char in mapping:
            if not stack or stack.pop() != mapping[char]:
                return False  # Несоответствие или пустой стек
    return not stack  # True, если стек пуст


def simulate_print_queue(tasks: list[str]) -> list[str]:
    """Симулирует очередь печати с использованием deque (FIFO).
    
    Возвращает список задач в порядке их обработки.
    Сложность: O(n).
    """
    print_queue = deque(tasks)
    processed = []

    while print_queue:
        task = print_queue.popleft()  # FIFO: первая добавленная — первая извлечённая
        processed.append(task)
    return processed


def is_palindrome(sequence: str) -> bool:
    """Проверяет, является ли последовательность палиндромом, с использованием deque.
    
    Игнорирует регистр и неалфавитные символы (опционально можно уточнить).
    Для простоты считаем, что вход — только буквы/цифры без пробелов.
    Сложность: O(n).
    """
    dq = deque(sequence.lower())
    while len(dq) > 1:
        if dq.popleft() != dq.pop():
            return False
    return True


# Примеры использования
if __name__ == '__main__':
    # Проверка скобок
    expr1 = "{[()()]}"
    expr2 = "{[(])}"
    print(f"'{expr1}' сбалансирован: {is_balanced_brackets(expr1)}")  # True
    print(f"'{expr2}' сбалансирован: {is_balanced_brackets(expr2)}")  # False

    # Очередь печати
    jobs = ['doc1.pdf', 'photo.jpg', 'report.docx']
    print("Очередь печати:", simulate_print_queue(jobs))

    # Палиндром
    word1 = "Анна"
    word2 = "hello"
    print(f"'{word1}' — палиндром: {is_palindrome(word1)}")  # True (если без учёта регистра)
    print(f"'{word2}' — палиндром: {is_palindrome(word2)}")  # False
