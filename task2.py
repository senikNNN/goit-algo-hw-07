class TreeNode:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key

def insert(root, key):
    if root is None:
        return TreeNode(key)
    else:
        if root.val < key:
            root.right = insert(root.right, key)
        else:
            root.left = insert(root.left, key)
    return root

def find_min_value(root):
    current = root
    while current.left is not None:
        current = current.left
    return current.val

root = TreeNode(20)
root = insert(root, 10)
root = insert(root, 30)
root = insert(root, 5)
root = insert(root, 15)
root = insert(root, 25)
root = insert(root, 35)

min_value = find_min_value(root)
print(f"Найменше значення в дереві: {min_value}")
