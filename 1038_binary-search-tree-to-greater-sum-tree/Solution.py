# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def bstToGst(self, root: TreeNode) -> TreeNode:
        if root:
            left = self.bstToGst(root.left) # First recur on the left side
            right = self.bstToGst(root.right) # Next recur on the right side
            if right:
                root.val += right.val

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