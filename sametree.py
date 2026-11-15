class Solution:
    def isSameTree(self, p: TreeNode | None, q: TreeNode | None) -> bool:
        def issame(p , q ):
            if p is None and q is None:
                return True
            if p is None or q is None:
                return False
            if p.val!= q.val:
                return False

            return issame(p.left,q.left) and issame(p.right,q.right)
        return issame(p,q)
