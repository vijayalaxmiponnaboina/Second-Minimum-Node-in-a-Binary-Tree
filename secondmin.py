# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findSecondMinimumValue(self, root: TreeNode | None) -> int:
        values=set()
        def inorder(root):
            if root is None:
                return
            inorder(root.left)
            values.add(root.val)
            inorder(root.right)
        inorder(root)
        sorted_values=sorted(values)
        if len(sorted_values)==1:
            return -1
        else:
            return sorted_values[1]
