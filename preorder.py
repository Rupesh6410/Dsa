class Solution:
    def preorderTraversal(self, root: TreeNode | None) -> list[int]:
        ans=[]
        def pre(root):
            if root is None:
                return
            ans.append(root.val)
            pre(root.left)
            pre(root.right)

        pre(root)
        return ans
