from AdjacencyMatrix import AdjacencyMatrix
from AdjacencyList import AdjacencyList
from IncidenceMatrix import IncidenceMatrix

def test_graph_representations():
    print("=== Матрица смежности ===")
    adj_matrix = AdjacencyMatrix(4)
    adj_matrix.add_edge(0, 1)
    adj_matrix.add_edge(2, 3)
    adj_matrix.display()

    print("\n=== Список смежности ===")
    adj_list = AdjacencyList(4)
    adj_list.add_edge(0, 1)
    adj_list.add_edge(2, 3)
    adj_list.display()

    print("\n=== Матрица инцидентности ===")
    inc_matrix = IncidenceMatrix(4)
    inc_matrix.add_edge(0, 1)
    inc_matrix.add_edge(2, 3)
    inc_matrix.display()

if __name__ == "__main__":
    test_graph_representations()
