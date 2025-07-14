class Node:
    def __init__(self, val, left_node=None, right_node=None):
        self.val = val
        self.left = left_node
        self.right = right_node

def inOrderTraversalRecursive(root):
    if not root:
        return
    inOrderTraversalRecursive(root.left)
    print(root.val)
    inOrderTraversalRecursive(root.right)

def inOrderTraversalIterative(root):
    stack = []
    curr = root
    while stack or curr:
        while curr:
            stack.append(curr)
            curr = curr.left
        curr = stack.pop()
        print(curr.val)
        curr = curr.right

if __name__ == "__main__":
    tree = Node(1,
    Node(2,
        Node(4,
            Node(8),
            Node(9)
        ),
        Node(5,
            Node(10),
            Node(11)
        )
    ),
    Node(3,
        Node(6,
            Node(12),
            Node(13)
        ),
        Node(7,
            Node(14),
            Node(15))
        )
    )
    BST = Node(8, Node(4, Node(2, Node(1), Node(3)), Node(6, Node(5), Node(7))), Node(12, Node(10, Node(9), Node(11)), Node(14, Node(13), Node(15))))
    print("In Order Traversal with a recursive method:")
    inOrderTraversalRecursive(tree)
    print()
    inOrderTraversalRecursive(BST)
    print()
    print("In Order Traversal with an iterative method:")
    inOrderTraversalIterative(tree)
    print()
    inOrderTraversalIterative(BST)