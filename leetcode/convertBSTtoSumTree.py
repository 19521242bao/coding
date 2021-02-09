
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def bstToGst(self, root: TreeNode) -> TreeNode:
        def Summore(root,cur):
            if root is  None:
                return cur
            root.val+=Summore(root.right,cur)
            return Summore(root.left,root.val)
        Summore(root,0)
        return root