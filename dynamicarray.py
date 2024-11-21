class DynamicArray:
    def __init__(self):
        self.array = [None]  # Start with capacity of 1
        self.capacity = 1
        self.size = 0
        self.total_cost = 0  # To calculate amortized cost

    def insert(self, value):
        # Resize if needed
        if self.size == self.capacity:
            self._resize()

        # Insert value
        self.array[self.size] = value
        self.size += 1
        self.total_cost += 1  # Increment for insertion cost

    def _resize(self):
        # Double the capacity
        new_capacity = self.capacity * 2
        new_array = [None] * new_capacity

        # Copy elements
        for i in range(self.size):
            new_array[i] = self.array[i]
            self.total_cost += 1  # Increment for copying cost

        self.array = new_array
        self.capacity = new_capacity

    def get_amortized_cost(self):
        return self.total_cost / self.size if self.size > 0 else 0

# Example usage
if __name__ == "__main__":
    posts = DynamicArray()
    num_insertions = 10
    for i in range(1, num_insertions + 1):
        posts.insert(f"Post {i}")
        print(f"Inserted: Post {i}, Current Capacity: {posts.capacity}")

    print(f"Amortized Cost per Insertion: {posts.get_amortized_cost():.2f}")
