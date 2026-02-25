from collections import deque

class Node:
    def __init__(self, value):
        self.value = value
        self.outbound = []
        self.inbound = []

    def point_to(self, other):
        """Добавляет направленное ребро от текущего узла к другим."""
        self.outbound.append(other)
        other.inbound.append(self)

    def __str__(self):
        return f'Node({self.value})'


class Graph:
    def __init__(self, root):
        self._root = root

    def dfs(self):
        """Заглушка для обхода в глубину."""
        pass

    def bfs(self):
        """Обход графа в ширину, начиная с корневого узла.
        Возвращает список значений узлов в порядке посещения."""
        if self._root is None:
            return []

        visited = set()      # множество посещённых узлов
        queue = deque()      # очередь для BFS
        result = []          # порядок обхода

        queue.append(self._root)
        visited.add(self._root)

        while queue:
            node = queue.popleft()
            result.append(node.value)

            # Добавляем всех непосещённых соседей (исходящие рёбра)
            for neighbor in node.outbound:
                if neighbor not in visited:
                    visited.add(neighbor)
                    queue.append(neighbor)

        return result


# ТЕСТИРОВАНИЕ
if __name__ == '__main__':
    # Создаём узлы
    node0 = Node(0)
    node1 = Node(1)
    node2 = Node(2)
    node3 = Node(3)
    node4 = Node(4)

    # Строим направленные рёбра
    node0.point_to(node1)
    node0.point_to(node2)
    node0.point_to(node3)
    node1.point_to(node0)
    node1.point_to(node2)
    node2.point_to(node0)
    node2.point_to(node1)
    node2.point_to(node4)
    node3.point_to(node0)
    node4.point_to(node2)

    # Создаём граф с корнем в узле 0
    graph = Graph(node0)

    # Выполняем BFS
    bfs_order = graph.bfs()
    print("Порядок обхода BFS:", bfs_order)

    # Ожидаемый результат
    expected = [0, 1, 2, 3, 4]
    assert bfs_order == expected, f"Ошибка: получено {bfs_order}, ожидалось {expected}"
    print("Успешно!")