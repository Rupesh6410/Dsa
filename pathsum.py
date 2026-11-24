class Solution:
    def hasPathSum(self, root: TreeNode | None, targetSum: int) -> bool:
        def summ(node,Sum,target):
            res=False
            if node is None:
                return False
            Sum+=node.val
            if node.left is None and node.right is None:
                if Sum==target:
                    res=True
                    return res
            left=summ(node.left,Sum,target)
            right=summ(node.right,Sum,target)
            return left or right
        return summ(root,0,targetSum)
            
