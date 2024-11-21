import networkx as nx

def calculate_degree_centrality(graph):
    """Calculate degree centrality for each node in the graph."""
    centrality = nx.degree_centrality(graph)
    return centrality

def display_centrality(centrality):
    """Display degree centrality in a readable format."""
    print("Degree Centrality:")
    for node, value in sorted(centrality.items(), key=lambda x: x[1], reverse=True):
        print(f"Intersection {node}: {value:.4f}")

if __name__ == "__main__":
    # Create a traffic network graph
    traffic_graph = nx.DiGraph()  # Directed graph for one-way roads
    # Add nodes (intersections) and edges (roads)
    traffic_graph.add_edges_from([
        ("A", "B"), ("A", "C"), ("B", "C"), ("C", "D"),
        ("D", "E"), ("E", "F"), ("F", "C"), ("B", "E")
    ])

    # Calculate degree centrality
    degree_centrality = calculate_degree_centrality(traffic_graph)

    # Display the results
    display_centrality(degree_centrality)
