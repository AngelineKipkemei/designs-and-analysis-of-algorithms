class QueueWithReorganization:
    def __init__(self):
        self.queue = []
        self.operation_count = 0  # Track number of operations
        self.reorganization_interval = 5  # Move elements to front every 5 operations

    # Enqueue operation
    def enqueue(self, value):
        self.queue.append(value)
        self.operation_count += 1
        # Occasionally move elements to the front
        if self.operation_count % self.reorganization_interval == 0:
            self.move_elements_to_front()

    # Dequeue operation
    def dequeue(self):
        if len(self.queue) == 0:
            return None  # Queue is empty
        self.operation_count += 1
        return self.queue.pop(0)

    # Move elements to the front of the queue
    def move_elements_to_front(self):
        if len(self.queue) > 1:
            self.queue = [self.queue[-1]] + self.queue[:-1]  # Move the last element to the front
        print("Reorganization: All elements moved to the front.")

    # Get the current state of the queue
    def get_queue(self):
        return self.queue

    # Compute the amortized cost per operation
    def compute_amortized_cost(self, total_operations):
        # Since the reorganization happens every 'reorganization_interval' operations
        total_cost = total_operations  # Enqueue and Dequeue operations are O(1)
        total_cost += (total_operations // self.reorganization_interval) * len(self.queue)  # Reorganization cost
        return total_cost / total_operations

# Simulate the queue and compute amortized cost
queue = QueueWithReorganization()

# Add some elements to the queue
for i in range(15):
    queue.enqueue(i)

# Dequeue some elements
for _ in range(5):
    queue.dequeue()

# Compute and display the amortized cost
total_operations = 20  # 15 enqueues + 5 dequeues
amortized_cost = queue.compute_amortized_cost(total_operations)

print("Final Queue State:", queue.get_queue())
print("Amortized Cost per Operation:", amortized_cost)
