class Node:
    def __init__(self, value):
        self.value = value
        self.outbound = []
        self.inbound = []

    def point_to(self, other):
        self.outbound.append(other)
        other.inbound.append(self)

    def __str__(self):
        return f'Node({self.value})'

    __repr__ = __str__


class Graph:
    def __init__(self, root):
        self._root = root

    def dfs(self):
        if self.root is None:
            return []
        visited = []   # список пройденных вершин в порядке обхода
        stack = [self._root]     # стек вершин

        while stack:
            node = stack.pop()
            if node not in visited:
                visited.append(node)
                # Добавляем соседей в обратном порядке для сохранения порядка обхода
                for neighbor in reversed(node.outbound):
                    stack.append(neighbor)   # соседи хранятся в стеке

        return visited
