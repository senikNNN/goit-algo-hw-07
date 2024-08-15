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

def find_max_value(root):
    current = root
    while current.right is not None:
        current = current.right
    return current.val

root = TreeNode(20)
root = insert(root, 10)
root = insert(root, 30)
root = insert(root, 5)
root = insert(root, 15)
root = insert(root, 25)
root = insert(root, 35)

max_value = find_max_value(root)
print(f"Найбільше значення в дереві: {max_value}")
