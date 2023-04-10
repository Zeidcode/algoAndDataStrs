class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def find_max(root):

    if not root:
        return None

    max_val = root.value
    left_max = find_max(root.left)
    right_max = find_max(root.right)

    if left_max and left_max > max_val:
        max_val = left_max
    if right_max and right_max > max_val:
        max_val = right_max

    return max_val

def count_leaves(root):

    if not root:
        return 0
    elif not root.left and not root.right:
        return 1
    else:
        return count_leaves(root.left) + count_leaves(root.right)


root = Node(4)
root.left = Node(2)
root.right = Node(6)
root.left.left = Node(1)
root.left.right = Node(3)
root.right.left = Node(5)
root.right.right = Node(7)

# Find the maximum element
max_val = find_max(root)
print(max_val)
# Count the number of leaves
num_leaves = count_leaves(root)
print(num_leaves)