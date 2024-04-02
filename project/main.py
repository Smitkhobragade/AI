import tkinter as tk
from tkinter import ttk
import networkx as nx
import matplotlib.pyplot as plt
import tkinter.messagebox as messagebox

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

node_positions = {
    'Arad': (2, 1.75),
    'Zerind': (2, 3),
    'Oradea': (1.85, 4),
    'Timisoara': (0, 1),
    'Lugoj': (0, 3),
    'Mehadia': (-0.1, 6.03),
    'Drobeta': (4, 5),
    'Craiova': (6, 5),
    'Rimnicu Vilcea': (6, 3),
    'Sibiu': (4, 3),
    'Fagaras': (4, 1),
    'Pitesti': (8, 3),
    'Bucharest': (8, 1),
    'Giurgiu': (10, 1),
    'Urziceni': (10, 3),
    'Hirsova': (12, 3),
    'Eforie': (12, 5),
    'Vaslui': (10, 5),
    'Iasi': (10, 7),
    'Neamt': (8, 7)
}

root = tk.Tk()
root.title("Romania Map BFS Visualization")

canvas = tk.Canvas(root, width=800, height=600)
canvas.pack()

source_label = ttk.Label(root, text="Select Source:")
source_label.pack()
source_var = tk.StringVar()
source_dropdown = ttk.Combobox(root, textvariable=source_var)
source_dropdown['values'] = tuple(romania_map.keys())
source_dropdown.pack()

destination_label = ttk.Label(root, text="Select Destination:")
destination_label.pack()
destination_var = tk.StringVar()
destination_dropdown = ttk.Combobox(root, textvariable=destination_var)
destination_dropdown['values'] = tuple(romania_map.keys())
destination_dropdown.pack()

def submit():
    source = source_var.get()
    destination = destination_var.get()
    traverse_bfs(source, destination)

submit_button = ttk.Button(root, text="Submit", command=submit)
submit_button.pack()

def traverse_bfs(source, destination):
    G = nx.Graph(romania_map)
    pos = node_positions.copy()

    visited = {source: None}
    queue = [source]
    path = []

    def update_canvas():
        nonlocal queue_text, visited_nodes_text
        canvas.delete("all")
        plt.figure(figsize=(8, 6))

        nx.draw(G, pos, with_labels=True, node_size=3000, node_color='skyblue')

        nx.draw_networkx_nodes(G, pos, nodelist=list(visited.keys()), node_color='lightgreen', node_size=3000)

        nx.draw_networkx_nodes(G, pos, nodelist=[node for node in queue if node != current_node], node_color='orange', node_size=3000)

        nx.draw_networkx_nodes(G, pos, nodelist=[current_node], node_color='yellow', node_size=3000)

        nx.draw_networkx_edges(G, pos, edgelist=list(zip(path[:-1], path[1:])), edge_color='r', width=3, alpha=0.5)

        plt.title("Romania Map BFS Visualization")

        plt.tight_layout()
        plt.savefig("current_map.png")
        plt.close()

        current_map = tk.PhotoImage(file="current_map.png")
        canvas.create_image(0, 0, anchor="nw", image=current_map)
        canvas.image = current_map
        
        # Update the labels
        queue_text.set("Queue: " + ", ".join(queue))
        # visited_nodes_text.set("Visited Nodes: " + ", ".join(visited.keys()))
        visited_minus_queue = [node for node in visited.keys() if node not in queue]
        print(visited_minus_queue)
        visited_nodes_text.set(", ".join(visited_minus_queue))
        root.update()


    def next_step():
        nonlocal path, current_node, visited_nodes, queue
        if queue:
            current_node = queue.pop(0)
            visited_nodes = list(visited.keys())
            if current_node == destination:
                node = current_node
                while node is not None:
                    path.insert(0, node)
                    node = visited[node]
                update_canvas()
                messagebox.showinfo("Destination Reached", "You have reached the destination!")
            else:
                for neighbor, _ in romania_map[current_node].items():
                    if neighbor not in visited:
                        visited[neighbor] = current_node
                        queue.append(neighbor)
                update_canvas()
        else:
            messagebox.showinfo("Destination Unreachable", "You can't reach to destination!")


    current_node = source
    visited_nodes = [source]
    queue_label = ttk.Label(root, text="Queue:")
    queue_label.pack()

    queue_text = tk.StringVar()
    queue_text.set("")
    queue_display = ttk.Label(root, textvariable=queue_text)
    queue_display.pack()

    visited_nodes_label = ttk.Label(root, text="Visited Nodes:")
    visited_nodes_label.pack()

    visited_nodes_text = tk.StringVar()
    visited_nodes_text.set("")
    visited_nodes_display = ttk.Label(root, textvariable=visited_nodes_text)
    visited_nodes_display.pack()

    next_step_button = ttk.Button(root, text="Next", command=next_step)
    next_step_button.pack()

root.mainloop()
