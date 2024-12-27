from node import Node


def recursive_find(node: Node, search_key: int):
    """
    Function to find Node which data is equal search_key.
    if Node is equal to None, it returns  tuple (False, None)
    if Node's data is equal to search_key, it returns tuple (True, Node)
    if Node's data is greater than search_key, it calls recursive_find function with left Node
    if Node's data is less than search_key, it calls recursive_find function with right Node
    """

    if node is None:
        return False, None
    else:
        if node.data == search_key:
            return True, node
        elif node.data > search_key:
            return recursive_find(node.left, search_key)
        else:
            return recursive_find(node.right, search_key)


def recursive_insert(node: Node, new_value: int):
    """
    Function to insert new value to Binary Tree.
    if new_value is existed in Binary Tree, it prints message
    else creates new Node with new_value data
    """

    if node.data > new_value:
        if node.left is not None:
            recursive_insert(node.left, new_value)
        else:
            node.left = Node(new_value, node)
    elif node.data < new_value:
        if node.right is not None:
            recursive_insert(node.right, new_value)
        else:
            node.right = Node(new_value, node)
    else:
        print(f"Node with {new_value} value is already taken!")


def find_left_node(node: Node):
    """
    Function to find successor
    Returns Node
    """

    if node.left is None:
        return node
    return find_left_node(node.left)


def recursive_inorder(node: Node):
    """
    Function to convert Binary Tree to In-Order Traversal (Sorted list)
    Returns list of sorted Binary Tree values
    """

    tree_list = []
    if node:
        tree_list = recursive_inorder(node.left)
        tree_list.append(node.data)
        tree_list = tree_list + recursive_inorder(node.right)
    return tree_list


def recursive_preorder(node: Node):
    """
    Function to convert Binary Tree to Pre-Order Traversal
    Returns list in Pre-Order Traversal
    """

    tree_list = []
    if node:
        tree_list.append(node.data)
        tree_list = tree_list + recursive_preorder(node.left)
        tree_list = tree_list + recursive_preorder(node.right)
    return tree_list


def recursive_postorder(node: Node):
    """
    Function to convert Binary Tree to Post-Order Traversal
    Returns list in Post-Order Traversal
    """

    tree_list = []
    if node:
        tree_list = recursive_postorder(node.left)
        tree_list = tree_list + recursive_postorder(node.right)
        tree_list.append(node.data)
    return tree_list


def recursive_height(node: Node):
    # Check if the binary tree is empty
    if node is None:
        # If TRUE return 0
        return 0
        # Recursively call height of each node
    left_height = recursive_height(node.left)
    right_height = recursive_height(node.right)

    # Return max(leftHeight, rightHeight) at each iteration
    return max(left_height, right_height) + 1


class BinaryTree:
    def __init__(self, root: int):
        self.root = Node(root, None)

    def height(self):
        return recursive_height(self.root)

    def find(self, search_data: int):
        return recursive_find(self.root, search_data)

    def insert(self, new_data: int):
        recursive_insert(self.root, new_data)

    def delete(self, deleted_data: int):
        # Find Node with deleted_data value
        deleted_node = recursive_find(self.root, deleted_data)

        # If Node doesn't have children
        if deleted_node.left is None and deleted_node.right is None:
            if deleted_node.data > deleted_node.parent.data:
                deleted_node.parent.right = None
            else:
                deleted_node.parent.left = None
        # If Node has right children but doesn't have left
        elif deleted_node.left is None and deleted_node.right is not None:
            if deleted_node.data > deleted_node.parent.data:
                deleted_node.parent.right = deleted_node.right
            else:
                deleted_node.parent.left = deleted_node.right
        # If Node has left children but doesn't have right
        elif deleted_node.left is not None and deleted_node.right is None:
            if deleted_node.data > deleted_node.parent.data:
                deleted_node.parent.right = deleted_node.left
            else:
                deleted_node.parent.left = deleted_node.left
        # If Node has 2 children (left and right)
        else:
            # find successor and successor will be the node instead the deleted_node
            del_node_right = deleted_node.right
            successor = find_left_node(del_node_right)
            deleted_node.data = successor.data
            deleted_node.left.parent = successor
            deleted_node.right.parent = successor
            if successor.right:
                successor.parent.left = successor.right
            else:  # delete successor
                successor.parent.left = None

    def inorder(self):
        return recursive_inorder(self.root)

    def preorder(self):
        return recursive_preorder(self.root)

    def postorder(self):
        return recursive_postorder(self.root)

    def show_tree(self):
        n_levels = self.height()
        width = pow(2, n_levels + 1)

        location = [(self.root, 0, width, 'c')]
        levels = []

        while location:
            node, level, x, align = location.pop(0)
            if len(levels) <= level:
                levels.append([])

            levels[level].append([node, level, x, align])
            seg = width // (pow(2, level + 1))
            if node:
                location.append((node.left, level + 1, x - seg, 'l'))
                location.append((node.right, level + 1, x + seg, 'r'))

        for i, level in enumerate(levels):
            pre = 0
            pre_line = 0
            pre_value = ""
            line_str = ''
            pstr = ''
            prev_index_r = 0
            seg = width // (pow(2, i + 1))
            for n in level:
                if n[0]:
                    val_str = str(n[0].data)
                else:
                    val_str = str(n[0])
                if n[3] == 'r':
                    line_str += ' ' * (n[2] - pre_line - 1 - seg - seg // 2) + '¯' * (seg + seg // 2) + '\\'
                    pre_line = n[2]
                    index_ = line_str.find('\\', prev_index_r) + 2
                    prev_index_r = index_ + 1
                    pstr += ' ' * (index_ - pre) + val_str
                elif n[3] == 'l':
                    line_str += ' ' * (n[2] - pre_line - 1) + '/' + '¯' * (seg + seg // 2)
                    pre_line = n[2] + seg + seg // 2
                    index_ = line_str[prev_index_r:].find('/')
                    if len(pre_value) > 2:
                        index_ -= len(pre_value[2:])
                    pstr += val_str.rjust(index_)
                else:
                    pstr += ' ' * (n[2] - pre - len(val_str)) + val_str  # correct the potition acording to the number size
                pre = n[2]
                pre_value = val_str
            print(line_str)
            print(pstr)
