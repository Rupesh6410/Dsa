class Solution:
    def invertTree(self, root: TreeNode | None) -> TreeNode | None:
        if root is None:
            return None
        def invt(node):
            if node is None:
                return
            node.left , node.right = node.right , node.left
            invt(node.left)
            invt(node.right)
        invt(root)
        return root
            
