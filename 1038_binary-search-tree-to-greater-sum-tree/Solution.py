# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def __init__(self):
        self.total = 0 # A cumulative sum of all the nodes

    def bstToGst(self, root: TreeNode) -> TreeNode:
        if root:
            self.bstToGst(root.right) # First recur on the left side
            self.total += root.val # Add to the cumulative sum total
            root.val = self.total # Set the node value to the current total
            self.bstToGst(root.left) # Next recur on the right side
        return root

# Testing

def printTree(root: TreeNode) -> None:
    if root:
        printTree(root.left)
        print(root.val,)
        printTree(root.right)

root = TreeNode(4)
root.left = TreeNode(1)
root.right = TreeNode(6)
root.left.left = TreeNode(0)
root.left.right = TreeNode(2)
root.right.left = TreeNode(5)
root.right.right = TreeNode(7)
root.left.right.right = TreeNode(3)
root.right.right.right = TreeNode(8)

S = Solution()

printTree(root)
print()
printTree(S.bstToGst(root))