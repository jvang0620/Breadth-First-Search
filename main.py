import random
from collections import deque

class SearchTree:
    def __init__(self, value):
        # Constructor method for initializing a SearchTree node
        # Parameters:
        #   - value: The value to be stored in the node
        self.value = value  # Store the value in the node
        self.left = None    # Initialize the pointer to the left child node to None
        self.right = None   # Initialize the pointer to the right child node to None


def build_search_tree(tree_size):
    # Generate a random permutation of numbers from 1 to tree_size
    numbers = list(range(1, tree_size + 1))
    random.shuffle(numbers)  # Shuffle the numbers to create a random order

    # Build the search tree with nodes labeled from 1 to tree_size
    def build_tree(numbers):
        if not numbers:
            return None
        mid = len(numbers) // 2
        root = SearchTree(numbers[mid])  # Create a root node with the middle number
        root.left = build_tree(numbers[:mid])  # Recursively build left subtree with the first half of numbers
        root.right = build_tree(numbers[mid + 1:])  # Recursively build right subtree with the second half of numbers
        return root

    return build_tree(numbers)

def bfs_shortest_path(search_tree_root, start, target):
    if search_tree_root is None:
        return None

    visited = set()
    queue = deque([(search_tree_root, [search_tree_root.value])])  # Initialize queue with root node and its path

    while queue:
        node, path = queue.popleft()  # Dequeue a node and its path

        if node.value == target:
            return path  # If target found, return the path

        visited.add(node.value)

        if node.left and node.left.value not in visited:
            queue.append((node.left, path + [node.left.value]))  # Enqueue left child with extended path
        if node.right and node.right.value not in visited:
            queue.append((node.right, path + [node.right.value]))  # Enqueue right child with extended path

    return None

def print_tree(root, level=0, prefix=''):
    if root is None:
        return

    print(" " * (level * 4) + prefix + str(root.value))
    print_tree(root.left, level + 1, "L: ")  # Print left subtree with increased indentation
    print_tree(root.right, level + 1, "R: ")  # Print right subtree with increased indentation

# Ask the user for the number of nodes in the tree
tree_size = int(input("Enter the number of nodes in the tree: "))
search_tree_root = build_search_tree(tree_size)

# Ask the user for the number to search for, starting point, and ending point
number_to_search = int(input("\nEnter the number to search for (1 - {}): ".format(tree_size)))
start_point = int(input("Enter the starting point of the search (1 - {}): ".format(tree_size)))
end_point = int(input("Enter the ending point of the search (1 - {}): ".format(tree_size)))

# Validate user input
if (number_to_search < 1 or number_to_search > tree_size or
        start_point < 1 or start_point > tree_size or
        end_point < 1 or end_point > tree_size):
    print("Invalid input. Please enter numbers between 1 and {}.".format(tree_size))
elif start_point == end_point:
    print("Starting and ending points are the same.")
else:
    # Print the search tree
    print("\nSearch Tree:")
    print_tree(search_tree_root)

    # Find the shortest path from the starting point to the ending point including the number to search for
    shortest_path_start_to_end = bfs_shortest_path(search_tree_root, start_point, end_point)
    shortest_path_number_to_end = bfs_shortest_path(search_tree_root, start_point, number_to_search)
    shortest_path_number_to_end += bfs_shortest_path(search_tree_root, number_to_search, end_point)[1:]

    if shortest_path_start_to_end and shortest_path_number_to_end:
        print("\nShortest path from", start_point, "to", end_point, "passing through", number_to_search, ":",
              ' -> '.join(map(str, shortest_path_number_to_end)))
    else:
        print("\nNo path found from", start_point, "to", end_point, "passing through", number_to_search, ".")
