class IncidenceMatrix:
    def __init__(self, num_vertices):
        self.num_vertices = num_vertices
        self.edges = []
        self.matrix = []

    def add_edge(self, u, v):
        self.edges.append((u, v))
        self.update_matrix()

    def update_matrix(self):
        self.matrix = [[0] * len(self.edges) for _ in range(self.num_vertices)]
        for edge_index, (u, v) in enumerate(self.edges):
            self.matrix[u][edge_index] = 1
            self.matrix[v][edge_index] = 1  # Убираем эту строку, если граф ориентированный

    def display(self):
        for row in self.matrix:
            print(row)

    def has_edge(self, u, v):
        return (u, v) in self.edges or (v, u) in self.edges


# Пример использования
if __name__ == "__main__":
    graph = IncidenceMatrix(5)
    graph.add_edge(0, 1)
    graph.add_edge(1, 2)
    graph.add_edge(3, 4)
    graph.display()
    print("Ребро между 1 и 2 существует:", graph.has_edge(1, 2))
    print("Ребро между 0 и 4 существует:", graph.has_edge(0, 4))
