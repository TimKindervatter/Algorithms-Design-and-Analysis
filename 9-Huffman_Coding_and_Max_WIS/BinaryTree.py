class BinaryTree:
    def __init__(self, left=None, right=None, root=None):
        self.root = root
        self.left = left
        self.right = right

    def insert(self, subtree):
        assert(isinstance(subtree, BinaryTree)), "The inserted object must be a binary tree."
        if subtree.root < self.root:
            if self.left == None:
                self.left = subtree
            else:
                self.left.insert(subtree)
        elif subtree.root > self.root:
            if self.right == None:
                self.right = subtree
            else:
                self.right.insert(subtree)
        
    @property
    def max_depth(self):
        if self.left == None and self.right == None:
            return 0
        elif self.left == None:
            return self.right.max_depth + 1
        elif self.right == None:
            return self.left.max_depth + 1
        else:
            return max(self.left.max_depth, self.right.max_depth) + 1

    @property
    def min_depth(self):
        if self.left == None and self.right == None:
            return 0
        elif self.left == None:
            return self.right.min_depth + 1
        elif self.right == None:
            return self.left.min_depth + 1
        else:
            return min(self.left.min_depth, self.right.min_depth) + 1

    def __str__(self):
        return '\n'.join(self.indented())

    def indented(self, k=0):
        indented = []
        for b in [self.left, self.right]:
            if b == None:
                continue
            for line in b.indented(k + 1):
                indented.append('  ' + line)
        return [str(self.root)] + indented

    def __lt__(self, other):
        return False