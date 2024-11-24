class AdjacencyList:
    def __init__(self, num_vertices):
        self.num_vertices = num_vertices
        self.adj_list = {i: [] for i in range(num_vertices)}

    def add_edge(self, u, v):
        self.adj_list[u].append(v)
        self.adj_list[v].append(u)  # Убираем эту строку, если граф ориентированный

    def remove_edge(self, u, v):
        self.adj_list[u].remove(v)
        self.adj_list[v].remove(u)  # Убираем эту строку, если граф ориентированный

    def display(self):
        for vertex, neighbors in self.adj_list.items():
            print(f"{vertex}: {neighbors}")

    def has_edge(self, u, v):
        return v in self.adj_list[u]


# Пример использования
if __name__ == "__main__":
    graph = AdjacencyList(5)
    graph.add_edge(0, 1)
    graph.add_edge(1, 2)
    graph.add_edge(3, 4)
    graph.display()
    print("Ребро между 1 и 2 существует:", graph.has_edge(1, 2))
    print("Ребро между 0 и 4 существует:", graph.has_edge(0, 4))
