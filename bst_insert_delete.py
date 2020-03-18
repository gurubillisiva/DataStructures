class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


class BST:
    def __init__(self):
        self.root = None

    def in_order(self, root):
        if root:
            self.in_order(root.left)
            print(root.data, end=" ")
            self.in_order(root.right)

    def create(self, data):
        if self.root is None:
            self.root = Node(data)
        else:
            current = self.root
            while True:
                if data < current.data:
                    if current.left is not None:
                        current = current.left
                    else:
                        current.left = Node(data)
                        break
                elif data > current.data:
                    if current.right is not None:
                        current = current.right
                    else:
                        current.right = Node(data)
                        break
                else:
                    break

    def insert(self, root, data):
        if root is None:
            return Node(data)
        if data < root.data:
            root.left = self.insert(root.left, data)
        else:
            root.right = self.insert(root.right, data)
        return root

    def find_height(self, root):
        if root is None:
            return 0
        else:
            left_height = self.find_height(root.left)
            right_height = self.find_height(root.right)
        if left_height > right_height:
            return 1 + left_height
        else:
            return 1 + right_height

    def minValueNode(self, root):
        current = root
        while current.left is not None:
            current = current.left
        return current

    def delete(self, root, data):
        if root is None:
            return root
        if data < root.data:
            root.left = self.delete(root.left, data)
        elif data > root.data:
            root.data = self.delete(root.right, data)
        else:
            if root.left is None:
                temp = root.right
                root = None
                return temp
            elif root.right is None:
                temp = root.left
                root = None
                return temp
            tmp = self.minValueNode(root.right)
            root.data = tmp.data
            root.right = self.delete(root.right, tmp.data)
        return root


tree = BST()
arr = list(map(int, input().split()))
for data in arr:
    tree.create(data)
tree.in_order(tree.root)
print("\nHeight of the tre is", tree.find_height(tree.root))
choice = 0
while choice is not 5:
    choice = int(input("Enter your choice\n1.Insert 2. Delete 5. Exit"))
    if choice == 1:
        data = int(input("Enter value to insert"))
        tree.insert(tree.root, data)
        print("after insertion")
        tree.in_order(tree.root)
    elif choice == 2:
        data = int(input("Enter value to delete"))
        tree.delete(tree.root, data)
        print("After deletion")
        tree.in_order(tree.root)
    else:
        break
