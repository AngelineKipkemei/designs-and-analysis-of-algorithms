from collections import defaultdict

class SocialNetwork:
    def __init__(self):
        self.graph = defaultdict(list)  # Adjacency list representation

    def add_friendship(self, user1, user2):
        """Add a bidirectional friendship between two users."""
        self.graph[user1].append(user2)
        self.graph[user2].append(user1)

    def mutual_friends(self, user1, user2):
        """Find mutual friends between two users."""
        if user1 not in self.graph or user2 not in self.graph:
            return []  # No mutual friends if either user doesn't exist
        
        # Retrieve neighbors of both users
        friends_of_user1 = set(self.graph[user1])
        friends_of_user2 = set(self.graph[user2])

        # Find mutual friends
        return list(friends_of_user1.intersection(friends_of_user2))

# Example Usage
if __name__ == "__main__":
    # Create social network
    network = SocialNetwork()
    network.add_friendship("Alice", "Bob")
    network.add_friendship("Alice", "Charlie")
    network.add_friendship("Bob", "Charlie")
    network.add_friendship("Bob", "David")
    network.add_friendship("Charlie", "David")
    network.add_friendship("Eve", "Frank")

    # Find mutual friends
    user1, user2 = "Alice", "Bob"
    mutuals = network.mutual_friends(user1, user2)
    print(f"Mutual friends between {user1} and {user2}: {mutuals}")
