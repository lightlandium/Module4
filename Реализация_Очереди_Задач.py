class Task:
    """Класс, представляющий задачу"""
    def __init__(self, name):
        self.name = name


class TaskQueue:
    """Очередь задач (FIFO)"""
    def __init__(self):
        """Инициализирует пустую очередь"""
        self._tasks = []

    def add_task(self, task):
        """Добавляет задачу в конец очереди"""
        self._tasks.append(task)

    def get_next_task(self):
        """Извлекает и возвращает задачу из начала очереди.
        Если очередь пуста, возвращает None.
        """
        if self.is_empty():
            return None
        # Удаляем первый элемент списка и возвращаем его
        return self._tasks.pop(0)

    def is_empty(self):
        """Проверяет, пуста ли очередь"""
        return len(self._tasks) == 0


# Демонстрация работы (по примеру)
queue = TaskQueue()

task1 = Task("Задача 1")
task2 = Task("Задача 2")
task3 = Task("Задача 3")

queue.add_task(task1)
queue.add_task(task2)
queue.add_task(task3)

next_task = queue.get_next_task()
print(f"Следующая задача: {next_task.name if next_task else 'Нет задач'}")  # Задача 1

queue.get_next_task()  # Извлекаем задачу 2

print(f"Очередь пуста: {queue.is_empty()}")  # False (осталась задача 3)





