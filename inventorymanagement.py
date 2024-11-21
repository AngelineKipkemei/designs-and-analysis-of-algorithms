def min_inventory_cost(demand, ordering_cost, holding_cost, shortage_cost):
    n = len(demand)
    dp = [[float('inf')] * (max(demand) + 1) for _ in range(n)]

    # Base case: No inventory left at the end
    for i in range(max(demand) + 1):
        dp[n-1][i] = shortage_cost * i

    # Fill the DP table
    for t in range(n-2, -1, -1):
        for i in range(max(demand) + 1):
            min_cost = float('inf')
            for q in range(max(demand) + 1):
                cost = ordering_cost * (q > 0) + holding_cost * max(0, i + q - demand[t]) + shortage_cost * max(0, demand[t] - i - q) + dp[t+1][max(0, i + q - demand[t])]
                min_cost = min(min_cost, cost)
            dp[t][i] = min_cost

    return dp[0][0]

# Example usage
demand = [10, 15, 20]
ordering_cost = 50
holding_cost = 2
shortage_cost = 10

min_cost = min_inventory_cost(demand, ordering_cost, holding_cost, shortage_cost)
print("Minimum inventory cost:", min_cost)