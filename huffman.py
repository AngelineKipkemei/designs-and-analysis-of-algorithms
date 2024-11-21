from heapq import heappush, heappop

class Node:
    def __init__(self, char, freq):
        self.char = char
        self.freq = freq
        self.left = None
        self.right = None

    def __lt__(self, other):
        return self.freq < other.freq

def huffman_encoding(char_freq):
    heap = [Node(char, freq) for char, freq in char_freq.items()]
    heapq.heapify(heap)

    while len(heap) > 1:
        left = heapq.heappop(heap)
        right = heapq.heappop(heap)
        node = Node(None, left.freq + right.freq)
        node.left = left
        node.right = right
        heapq.heappush(heap, node)

    root = heap[0]
    codes = {}
    
    def encode(node, code):
        if node is None:
            return
        if node.char is not None:
            codes[node.char] = code
        encode(node.left, code + '0')
        encode(node.right, code + '1')

    encode(root, '')
    return codes

# Example usage
char_freq = {'a': 5, 'b': 9, 'c': 12, 'd': 13, 'e': 16, 'f': 45}
codes = huffman_encoding(char_freq)
print(codes)