class Node:
    def __init__(self, val, left_node=None, right_node=None):
        self.val = val
        self.left = left_node
        self.right = right_node

def postOrderTraversalRecursive(root):
    if not root:
        return
    postOrderTraversalRecursive(root.left)
    postOrderTraversalRecursive(root.right)
    print(root.val)

def postOrderTraversalIterative(root):
    stack = []
    last_visited = None
    curr = root

    while stack or curr:
        if curr:
            stack.append(curr)
            curr = curr.left
        else:
            peek = stack[-1]
            if peek.right and last_visited != peek.right:
                curr = peek.right
            else:
                print(peek.val)
                last_visited = stack.pop()

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
    print("Post Order Traversal with a recursive method:")
    postOrderTraversalRecursive(tree)
    print()
    postOrderTraversalRecursive(BST)
    print()
    print("Post Order Traversal with an iterative method:")
    postOrderTraversalIterative(tree)
    print()
    postOrderTraversalIterative(BST)