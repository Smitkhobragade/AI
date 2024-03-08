import tkinter as tk
from tkinter import ttk
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import networkx as nx

# Load Romania map image
map_image = mpimg.imread('romania_map.jpg')

# Romania map graph representation
romania_map = {
    'Arad': {'Zerind': 75, 'Timisoara': 118, 'Sibiu': 140},
    'Zerind': {'Arad': 75, 'Oradea': 71},
    'Oradea': {'Zerind': 71, 'Sibiu': 151},
    'Timisoara': {'Arad': 118, 'Lugoj': 111},
    'Lugoj': {'Timisoara': 111, 'Mehadia': 70},
    'Mehadia': {'Lugoj': 70, 'Drobeta': 75},
    'Drobeta': {'Mehadia': 75, 'Craiova': 120},
    'Craiova': {'Drobeta': 120, 'Rimnicu Vilcea': 146, 'Pitesti': 138},
    'Rimnicu Vilcea': {'Craiova': 146, 'Sibiu': 80, 'Pitesti': 97},
    'Sibiu': {'Arad': 140, 'Oradea': 151, 'Rimnicu Vilcea': 80, 'Fagaras': 99},
    'Fagaras': {'Sibiu': 99, 'Bucharest': 211},
    'Pitesti': {'Rimnicu Vilcea': 97, 'Craiova': 138, 'Bucharest': 101},
    'Bucharest': {'Fagaras': 211, 'Pitesti': 101, 'Giurgiu': 90, 'Urziceni': 85},
    'Giurgiu': {'Bucharest': 90},
    'Urziceni': {'Bucharest': 85, 'Vaslui': 142, 'Hirsova': 98},
    'Hirsova': {'Urziceni': 98, 'Eforie': 86},
    'Eforie': {'Hirsova': 86},
    'Vaslui': {'Urziceni': 142, 'Iasi': 92},
    'Iasi': {'Vaslui': 92, 'Neamt': 87},
    'Neamt': {'Iasi': 87}
}

# Create GUI window
root = tk.Tk()
root.title("Romania Map BFS Visualization")

# Add dropdowns for selecting source and destination
source_label = ttk.Label(root, text="Select Source:")
source_label.grid(row=0, column=0, padx=10, pady=5)
source_var = tk.StringVar()
source_dropdown = ttk.Combobox(root, textvariable=source_var)
source_dropdown['values'] = tuple(romania_map.keys())
source_dropdown.grid(row=0, column=1, padx=10, pady=5)

destination_label = ttk.Label(root, text="Select Destination:")
destination_label.grid(row=1, column=0, padx=10, pady=5)
destination_var = tk.StringVar()
destination_dropdown = ttk.Combobox(root, textvariable=destination_var)
destination_dropdown['values'] = tuple(romania_map.keys())
destination_dropdown.grid(row=1, column=1, padx=10, pady=5)

# Add Submit button
def submit():
    source = source_var.get()
    destination = destination_var.get()
    bfs_algorithm(source, destination)

submit_button = ttk.Button(root, text="Submit", command=submit)
submit_button.grid(row=2, column=0, columnspan=2, pady=10)

# Display map
def display_map(current_node, visited_nodes, queue, path):
    G = nx.Graph(romania_map)
    pos = nx.spring_layout(G)
    plt.figure(figsize=(10, 8))

    nx.draw(G, pos, with_labels=True, node_size=3000, node_color='skyblue')
    
    nx.draw_networkx_nodes(G, pos, nodelist=[current_node], node_color='yellow', node_size=3000)

    nx.draw_networkx_nodes(G, pos, nodelist=visited_nodes, node_color='lightgreen', node_size=3000)

    nx.draw_networkx_nodes(G, pos, nodelist=queue, node_color='lightblue', node_size=3000)

    nx.draw_networkx_edges(G, pos, edgelist=path, edge_color='r', width=3)

    plt.title("Romania Map BFS Visualization")
    plt.show()

# Breadth First Search Algorithm
def bfs_algorithm(source, destination):
    visited = {source: None}
    queue = [source]
    path = []
    while queue:
        current_node = queue.pop(0)
        visited_nodes = list(visited.keys())
        if current_node == destination:
            # Reconstruct path
            node = destination
            while node is not None:
                path.insert(0, node)
                node = visited[node]
            display_map(current_node, visited_nodes, queue, list(zip(path[:-1], path[1:])))
            return
        for neighbor, _ in romania_map[current_node].items():
            if neighbor not in visited:
                visited[neighbor] = current_node
                queue.append(neighbor)
        display_map(current_node, visited_nodes, queue, list(zip(path[:-1], path[1:])))

# Start GUI event loop
root.mainloop()
