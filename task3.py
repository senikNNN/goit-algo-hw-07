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

def sum_of_values(root):
    if root is None:
        return 0
    return root.val + sum_of_values(root.left) + sum_of_values(root.right)

root = TreeNode(20)
root = insert(root, 10)
root = insert(root, 30)
root = insert(root, 5)
root = insert(root, 15)
root = insert(root, 25)
root = insert(root, 35)

total_sum = sum_of_values(root)
print(f"Сума всіх значень у дереві: {total_sum}")
