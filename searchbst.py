class Solution:
    def searchBST(self, root: TreeNode | None, val: int) -> TreeNode | None:
        def sbst(node,val):
            if node is None:
                return None
            if node.val==val:
                return node
            if node.val<val:
                return sbst(node.right,val)
            else:
                return sbst(node.left,val)
        return sbst(root,val)
