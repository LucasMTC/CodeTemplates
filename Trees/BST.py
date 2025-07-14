"""
struct Node {
  int data
  Node left
  Node right
}

class BinarySearchTree {
  private:
    Node root

  public:
    int min() // returns the minimum value in the BST.  O(logn) time.
    int max() // returns the maximum value in the BST.  O(logn) time.
    bool contains(int val) // returns a boolean indicating whether val is present in the
                              BST.  O(logn) time.
    void insert(int val) // creates a new Node with data val in the appropriate location.
                            For simplicity, do not allow duplicates. If val is already
                            present, insert is a no-op. O(logn) time.
    void delete(int val) // deletes the Node with data val, if it exists. O(logn) time.
}
"""

class Node:
    def __init__(self, val, left_node = None, right_node = None):
        self.val = val
        self.left = left_node
        self.right = right_node

class BST:
    def __init__(self, root:Node):
        self.__root = root

    def min(self) -> int:
        curr = self.__root
        while curr.left:
            curr = curr.left
        return curr.val

    def max(self) -> int:
        curr = self.__root
        while curr.right:
            curr = curr.right
        return curr.val

    def contains(self, val) -> bool:
        curr = self.__root
        while curr:
            if val > curr.val:
                curr = curr.right
            elif val < curr.val:
                curr = curr.left
            else:
                return True
        return False

    def insert(self, val) -> None:
        curr = self.__root
        while curr:
            if val > curr.val:
                if curr.right:
                    curr = curr.right
                else:
                    curr.right = Node(val)
                    return
            elif val < curr.val:
                if curr.left:
                    curr = curr.left
                else:
                    curr.left = Node(val)
                    return
            else:
                return

    def delete(self, val) -> None:
        def deleteNode(node, val) -> Node|None:
            if not node:
                return None
            if node.val > val:
                node.left = deleteNode(node.left, val)
            elif node.val < val:
                node.right = deleteNode(node.right, val)
            else:
                if not node.right:
                    return node.left
                elif not node.left:
                    return node.right
                else:
                    curr = node.right
                    while curr.left:
                        curr = curr.left
                    node.val = curr.val
                    node.right = deleteNode(node.right, curr.val)
            return node

        if self.contains(val):
            self.__root = deleteNode(self.__root, val)

    def preOrderTraversal(self):
        def traverse(node):
            if not node:
                return
            print(node.val)
            traverse(node.left)
            traverse(node.right)
        traverse(self.__root)

if __name__ == "__main__":
    root = Node(5)
    tree = BST(root)
    for num in [2, 1, 4, 3, 10, 9, 8, 12, 15, 13]:
        tree.insert(num)
    assert tree.min() == 1
    assert tree.max() == 15
    assert tree.contains(5) == True
    tree.preOrderTraversal()
    tree.delete(5)
    assert tree.contains(5) == False
    print()
    tree.preOrderTraversal()