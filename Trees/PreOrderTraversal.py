class Node:
    def __init__(self, val, left_node=None, right_node=None):
        self.val = val
        self.left = left_node
        self.right = right_node

def preOrderTraversalRecursive(root):
    if not root:
        return
    print(root.val)
    preOrderTraversalRecursive(root.left)
    preOrderTraversalRecursive(root.right)

def preOrderTraversalIterative(root):
    stack = [root]
    while stack:
        curr = stack.pop()
        print(curr.val)
        if curr.right:
            stack.append(curr.right)
        if curr.left:
            stack.append(curr.left)
        

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
    print("Pre Order Traversal with a recursive method:")
    preOrderTraversalRecursive(tree)
    print()
    preOrderTraversalRecursive(BST)
    print()
    print("Pre Order Traversal with an iterative method:")
    preOrderTraversalIterative(tree)
    print()
    preOrderTraversalIterative(BST)