class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
        self.level = None


class BST:
    def __init__(self):
        self.root = None

    def create(self, val):
        if self.root == None:
            self.root = Node(val)
        else:
            current = self.root
            while True:
                if val < current.val:
                    if current.left is not None:
                        current = current.left
                    else:
                        current.left = Node(val)
                        break
                elif val > current.val:
                    if current.right is not None:
                        current = current.right
                    else:
                        current.right = Node(val)
                        break
                else:
                    break

    def in_order(self, root):
        if root:
            self.in_order(root.left)
            print(root.val, end=" ")
            self.in_order(root.right)

    def find_height(self, root):
        if root is None:
            return 0
        else:
            lh = self.find_height(root.left)
            rh = self.find_height(root.right)
        if lh > rh:
            return lh + 1
        else:
            return rh + 1


tree = BST()
arr = list(map(int, input().split()))
for element in arr:
    tree.create(element)
tree.in_order(tree.root)
print("\n",tree.find_height(tree.root))
