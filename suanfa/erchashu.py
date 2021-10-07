class BinarySearchTree:
    def __init__(self):
        self.tree = None

    def insert(self, value):
        if self.tree is None:
            new_tree = self.node(value)
            self.tree = new_tree
            return
        else:
            p = self.tree
            while p is not None:
                if value < p.data:
                    if p.left is None:
                        p.left = self.node(value)
                        return
                    p = p.left
                if value > p.data:
                    if p.right is None:
                        p.right = self.node(value)
                        return
                    p = p.right

    def find(self, value):
        if self.tree is None:
            return None
        else:
            p = self.tree
            while p is not None:
                if value < p.data:
                    p = p.left
                elif value > p.data:
                    p = p.right
                else:
                    return p

    def delete(self, value):
        if self.tree is None:
            return False
        else:
            p = self.tree
            q = None
            while p is not None and value != p.data:
                q = p
                if value < p.data:
                    p = p.left
                elif value > p.data:
                    p = p.right
            if p is None:
                return None

            if p.left is not None and p.right is not None:
                tmp_p = p.right
                tmp_q = p
                while tmp_p.left is not None:
                    tmp_q = tmp_p
                    tmp_p = p.left
                p.data = tmp_p.data
                p = tmp_p
                q = tmp_q


            if p.left is not None:
                child = p.left
            elif p.right is not None:
                child = p.right
            else:
                child = None

            if q is None:
                self.tree = child
            elif q.left is p:
                q.left = child
            elif q.right is p:
                q.right = child

    def pre_order(self, node):
        if node is None:
            return None
        print(node.data)
        self.pre_order(node.left)
        self.pre_order(node.right)

    def in_order(self, node):
        if node is None:
            return None
        self.in_order(node.left)
        print(node.data)
        self.in_order(node.right)

    def post_order(self, node):
        if node is None:
            return None
        self.post_order(node.left)
        self.post_order(node.right)
        print(node.data)

    class node:
        def __init__(self, data):
            self.left = None
            self.data = data
            self.right = None


def test_binary_search_tree():
    binary_search_tree = BinarySearchTree()
    data = [1, 10, 20, 40, 13]
    for i in data:
        binary_search_tree.insert(i)
    assert 20 == binary_search_tree.find(20).data
    binary_search_tree.delete(20)
    assert binary_search_tree.find(20) is None
    # 1 10 40 13
    binary_search_tree.pre_order(binary_search_tree.tree)
    print("-----------------------")
    # 1 10 13 40
    binary_search_tree.in_order(binary_search_tree.tree)
    print("-----------------------")
    # 13 40 10 1
    binary_search_tree.post_order(binary_search_tree.tree)


if __name__ == '__main__':
    test_binary_search_tree()
