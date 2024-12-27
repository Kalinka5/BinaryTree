from binary_tree import BinaryTree

binary_tree = BinaryTree(35)

binary_tree.insert(29)
binary_tree.insert(60)
binary_tree.insert(18)
binary_tree.insert(32)
binary_tree.insert(12)
binary_tree.insert(20)
binary_tree.insert(31)
binary_tree.insert(34)
binary_tree.insert(30)
binary_tree.insert(33)
binary_tree.insert(45)
binary_tree.insert(90)
binary_tree.insert(70)
binary_tree.insert(120)
binary_tree.insert(80)

print(f"Height of binary tree: {binary_tree.height()}")

binary_tree.show_tree()

print(f"In-order Traversal: {binary_tree.inorder()}")
print(f"Pre-order Traversal: {binary_tree.preorder()}")
print(f"Post-order Traversal: {binary_tree.postorder()}")
