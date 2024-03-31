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

class BFSVisualizationApp:
    def __init__(self, master):
        self.master = master
        master.title("Romania Map BFS Visualization")

        self.canvas = tk.Canvas(master, width=800, height=600)
        self.canvas.pack()

        self.source_label = ttk.Label(master, text="Select Source:")
        self.source_label.pack()
        self.source_var = tk.StringVar()
        self.source_dropdown = ttk.Combobox(master, textvariable=self.source_var)
        self.source_dropdown['values'] = tuple(romania_map.keys())
        self.source_dropdown.pack()

        self.destination_label = ttk.Label(master, text="Select Destination:")
        self.destination_label.pack()
        self.destination_var = tk.StringVar()
        self.destination_dropdown = ttk.Combobox(master, textvariable=self.destination_var)
        self.destination_dropdown['values'] = tuple(romania_map.keys())
        self.destination_dropdown.pack()

        self.submit_button = ttk.Button(master, text="Submit", command=self.submit)
        self.submit_button.pack()

        self.G = nx.Graph(romania_map)
        self.pos = node_positions.copy()

        self.queue_text = tk.StringVar()
        self.queue_text.set("")
        self.queue_label = ttk.Label(master, text="Queue:")
        self.queue_label.pack()
        self.queue_display = ttk.Label(master, textvariable=self.queue_text)
        self.queue_display.pack()

        self.visited_nodes_text = tk.StringVar()
        self.visited_nodes_text.set("")
        self.visited_nodes_label = ttk.Label(master, text="Visited Nodes:")
        self.visited_nodes_label.pack()
        self.visited_nodes_display = ttk.Label(master, textvariable=self.visited_nodes_text)
        self.visited_nodes_display.pack()

        self.path = []
        self.current_node = None
        self.visited = None
        self.queue = None

    def submit(self):
        source = self.source_var.get()
        destination = self.destination_var.get()
        self.traverse_bfs(source, destination)

    def update_canvas(self):
        self.canvas.delete("all")
        plt.figure(figsize=(8, 6))

        nx.draw(self.G, self.pos, with_labels=True, node_size=3000, node_color='skyblue')

        nx.draw_networkx_nodes(self.G, self.pos, nodelist=[node for node in self.visited.keys()], node_color='lightgreen', node_size=3000)

        nx.draw_networkx_nodes(self.G, self.pos, nodelist=[node for node in self.queue if node != self.current_node], node_color='orange', node_size=3000)

        nx.draw_networkx_nodes(self.G, self.pos, nodelist=[self.current_node], node_color='yellow', node_size=3000)

        nx.draw_networkx_edges(self.G, self.pos, edgelist=list(zip(self.path[:-1], self.path[1:])), edge_color='r', width=3, alpha=0.5)

        plt.title("Romania Map BFS Visualization")

        plt.tight_layout()
        plt.savefig("current_map.png")
        plt.close()

        current_map = tk.PhotoImage(file="current_map.png")
        self.canvas.create_image(0, 0, anchor="nw", image=current_map)
        self.canvas.image = current_map

        # Update the labels
        self.queue_text.set(", ".join(self.queue))
        # self.visited_nodes_text.set(", ".join(self.visited.keys()))
        visited_minus_queue = [node for node in self.visited.keys() if node not in self.queue]
        print(visited_minus_queue)
        self.visited_nodes_text.set(", ".join(visited_minus_queue))


        self.master.update()



    def next_step(self):
        if self.queue:
            self.current_node = self.queue.pop(0)
            if self.current_node == self.destination_var.get():
                node = self.current_node
                while node is not None:
                    self.path.insert(0, node)
                    node = self.visited[node]
                self.update_canvas()
                messagebox.showinfo("Destination Reached", "You have reached the destination!")
            else:
                for neighbor, _ in romania_map[self.current_node].items():
                    if neighbor not in self.visited:
                        self.visited[neighbor] = self.current_node
                        self.queue.append(neighbor)
                self.update_canvas()
        else:
            messagebox.showinfo("Destination Unreachable", "You can't reach to destination!")

    def traverse_bfs(self, source, destination):
        self.visited = {source: None}
        self.queue = [source]
        self.path = []
        self.current_node = source
        self.update_canvas()

        self.master.queue_button = ttk.Button(self.master, text="Next", command=self.next_step)
        self.master.queue_button.pack()

root = tk.Tk()
app = BFSVisualizationApp(root)
root.mainloop()
