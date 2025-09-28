import csv
import heapq

def load_graph(filename):
    graph = {}
    with open(filename, newline='', encoding='utf-8-sig') as csvfile:
        reader = csv.DictReader(csvfile, delimiter=';')  # ← pakai delimiter ';'
        print("Fieldnames:", reader.fieldnames)  # debug cek header
        for row in reader:
            asal = row['Kota Asal']
            tujuan = row['Kota Tujuan']
            jarak = int(row['Jarak Jalan'])
            graph.setdefault(asal, []).append((tujuan, jarak))
            graph.setdefault(tujuan, []).append((asal, jarak))
    return graph

def ucs(graph, start, goal):
    queue = [(0, start, [])]
    visited = set()
    
    while queue:
        cost, node, path = heapq.heappop(queue)
        
        if node in visited:
            continue
        visited.add(node)
        
        path = path + [node]
        
        if node == goal:
            return cost, path
        
        for neighbor, edge_cost in graph.get(node, []):
            if neighbor not in visited:
                heapq.heappush(queue, (cost + edge_cost, neighbor, path))
    
    return float("inf"), []

if __name__ == "__main__":
    file_graph = "csv/Tugas Kelompok 1 - Peta Cilegon ke Banyuwangi.csv"
    graph = load_graph(file_graph)

    start = "Cilegon"
    goal = "Banyuwangi"

    cost, path = ucs(graph, start, goal)
    print(f"Jalur UCS dari {start} ke {goal}: {' -> '.join(path)}")
    print(f"Total jarak: {cost} km")
