class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        def lcabst(node,p,q):
            if node is None:
                return None
            if node==p or node==q:
                return node
            if node.val<p.val:
                return lcabst(node.right,p,q)
            elif node.val>q.val:
                return lcabst(node.left,p,q)
            else:
                ans=node
                return ans
        if p.val<q.val:
            return lcabst(root,p,q)
        else:
            return lcabst(root,q,p)
