import csv
import heapq

# === Load Graph (jalan antar kota) ===
def load_graph(filename):
    graph = {}
    with open(filename, newline='', encoding='utf-8-sig') as csvfile:
        reader = csv.DictReader(csvfile, delimiter=';')
        for row in reader:
            asal = row['Kota Asal']
            tujuan = row['Kota Tujuan']
            jarak = int(row['Jarak Jalan'])
            graph.setdefault(asal, []).append((tujuan, jarak))
            graph.setdefault(tujuan, []).append((asal, jarak))  # graf dua arah
    return graph

# === Load Heuristik (jarak perkiraan ke Banyuwangi) ===
def load_heuristic(filename):
    heuristic = {}
    with open(filename, newline='', encoding='utf-8-sig') as csvfile:
        reader = csv.DictReader(csvfile, delimiter=';')
        for row in reader:
            kota = row['Kota Asal']
            h = int(row['Heuristik ke Banyuwangi'])
            heuristic[kota] = h
    return heuristic

# === Algoritma A* ===
def astar(graph, heuristic, start, goal):
    queue = [(heuristic[start], 0, start, [])]  # (f, g, node, path)
    visited = set()

    while queue:
        f, g, node, path = heapq.heappop(queue)

        if node in visited:
            continue
        visited.add(node)

        path = path + [node]

        if node == goal:
            return g, path  # total cost (g) dan jalur

        for neighbor, edge_cost in graph.get(node, []):
            if neighbor not in visited:
                g_new = g + edge_cost
                f_new = g_new + heuristic.get(neighbor, float("inf"))
                heapq.heappush(queue, (f_new, g_new, neighbor, path))

    return float("inf"), []

# === Main Program ===
if __name__ == "__main__":
    file_graph = "csv/Tugas Kelompok 1 - Peta Cilegon ke Banyuwangi.csv"
    file_heuristic = "csv/Tugas Kelompok 1 - Heuristik ke Banyuwangi.csv"

    graph = load_graph(file_graph)
    heuristic = load_heuristic(file_heuristic)

    start = "Cilegon"
    goal = "Banyuwangi"

    cost, path = astar(graph, heuristic, start, goal)
    print(f"Jalur A* dari {start} ke {goal}: {' -> '.join(path)}")
    print(f"Total jarak: {cost} km")
