class Tree:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


def print_in_order(root):
    if root:
        print_in_order(root.left)
        print(root.val, end=' ')
        print_in_order(root.right)


def print_pre_order(root):
    if root:
        print(root.val, end=' ')
        print_pre_order(root.left)
        print_pre_order(root.right)


def print_post_order(root):
    if root:
        print_post_order(root.left)
        print_post_order(root.right)
        print(root.val, end=' ')


root = Tree(1)
root.left = Tree(2)
root.right = Tree(3)
root.left.left = Tree(4)
root.left.right = Tree(5)
print("\nPre order Traversal")
print_pre_order(root)
print("\nInorder traversal")
print_in_order(root)
print("\nPost order traversal")
print_post_order(root)
