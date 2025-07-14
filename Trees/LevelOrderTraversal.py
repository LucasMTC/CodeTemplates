from collections import deque

class Node:
    def __init__(self, val, left_node=None, right_node=None):
        self.val = val
        self.left = left_node
        self.right = right_node

def levelOrderTraversalRecursive(root):
    def bfs(queue):
        if not queue:
            return
        node = queue.popleft()
        print(node.val)
        if node.left:
            queue.append(node.left)
        if node.right:
            queue.append(node.right)
        bfs(queue) 
    
    if root:
        bfs(deque([root]))


def levelOrderTraversalIterative(root):
    queue = deque()
    queue.append(root)

    while queue:
        for _ in range(len(queue)):
            curr = queue.popleft()
            print(curr.val)
            if curr.left:
                queue.append(curr.left)
            if curr.right:
                queue.append(curr.right)

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
    print("Level Order Traversal with a recursive method:")
    levelOrderTraversalRecursive(tree)
    print()
    levelOrderTraversalRecursive(BST)
    print()
    print("Level Order Traversal with an iterative method:")
    levelOrderTraversalIterative(tree)
    print()
    levelOrderTraversalIterative(BST)