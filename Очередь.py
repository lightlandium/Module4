class Queue:
    """Простая очередь на основе списка."""

    def __init__(self):
        """Инициализация пустой очереди."""
        self.items = []

    def enqueue(self, item):
        """Добавляет элемент в конец очереди."""
        self.items.append(item)

    def dequeue(self):
        """Удаляет и возвращает элемент из начала очереди."""
        if self.is_empty():
            raise IndexError("Очередь пуста")
        return self.items.pop(0)  # pop(0) удаляет первый элемент

    def is_empty(self):
        """Проверяет, пуста ли очередь."""
        return len(self.items) == 0

    def size(self):
        """Возвращает количество элементов в очереди."""
        return len(self.items)


# Пример использования
queue = Queue()
queue.enqueue(1)
queue.enqueue(2)
queue.enqueue(3)

print("Размер очереди:", queue.size())  # Размер очереди: 3

while not queue.is_empty():
    item = queue.dequeue()
    print("Извлечен элемент:", item)
