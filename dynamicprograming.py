import sys

def supply_chain_min_cost(cost_matrix, source, destination):
    """
    Compute the minimum supply chain cost using dynamic programming.

    :param cost_matrix: 2D list where cost_matrix[i][j] represents the cost from node i to node j.
    :param source: Starting node (index).
    :param destination: Ending node (index).
    :return: Minimum cost to reach the destination from the source.
    """
    # Number of nodes
    n = len(cost_matrix)
    
    # Initialize DP array: min_cost[j] represents the minimum cost to reach node j
    min_cost = [sys.maxsize] * n
    min_cost[source] = 0  # Cost to reach source is zero
    
    # Dynamic programming to calculate minimum costs
    for _ in range(n - 1):  # At most, there are n-1 iterations for relaxation
        for i in range(n):
            for j in range(n):
                if cost_matrix[i][j] != sys.maxsize:  # If there is a valid edge
                    min_cost[j] = min(min_cost[j], min_cost[i] + cost_matrix[i][j])
    
    return min_cost[destination]

# Example usage
if __name__ == "__main__":
    # Example supply chain cost matrix (directed graph):
    # cost_matrix[i][j] represents the cost from node i to node j
    # sys.maxsize indicates no direct connection between nodes
    cost_matrix = [
        [0, 4, 2, sys.maxsize],
        [sys.maxsize, 0, 1, 3],
        [sys.maxsize, sys.maxsize, 0, 5],
        [sys.maxsize, sys.maxsize, sys.maxsize, 0]
    ]
    
    source = 0  # Starting node (e.g., S)
    destination = 3  # Ending node (e.g., D)
    
    min_cost = supply_chain_min_cost(cost_matrix, source, destination)
    
    if min_cost == sys.maxsize:
        print("No valid path from source to destination.")
    else:
        print(f"The minimum supply chain cost from node {source} to node {destination} is: {min_cost}")
