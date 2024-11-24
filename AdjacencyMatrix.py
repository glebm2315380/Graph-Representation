class AdjacencyMatrix:
    def __init__(self, num_vertices):
        self.num_vertices = num_vertices
        self.matrix = [[0] * num_vertices for _ in range(num_vertices)]

    def add_edge(self, u, v):
        self.matrix[u][v] = 1
        self.matrix[v][u] = 1  # Убираем эту строку, если граф ориентированный

    def remove_edge(self, u, v):
        self.matrix[u][v] = 0
        self.matrix[v][u] = 0  # Убираем эту строку, если граф ориентированный

    def display(self):
        for row in self.matrix:
            print(row)

    def has_edge(self, u, v):
        return self.matrix[u][v] == 1


# Пример использования
if __name__ == "__main__":
    graph = AdjacencyMatrix(5)
    graph.add_edge(0, 1)
    graph.add_edge(1, 2)
    graph.add_edge(3, 4)
    graph.display()
    print("Ребро между 1 и 2 существует:", graph.has_edge(1, 2))
    print("Ребро между 0 и 4 существует:", graph.has_edge(0, 4))
