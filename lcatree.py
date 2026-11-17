class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        ans=None
        def lca(node,p,q):
            nonlocal ans
            Self=0
            if node is None:
                return 0
            if node==p or node==q:
                Self=1
            left=lca(node.left,p,q)
            right=lca(node.right,p,q)
            total=left+right+Self
            if total==2 and ans is None:
                ans=node
            return total
        lca(root,p,q)
        return ans
