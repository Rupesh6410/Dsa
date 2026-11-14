from collections import deque
class Solution:
    def levelOrder(self, root: TreeNode | None) -> list[list[int]]:
        q=deque()
        if root:
            q.append(root)
        res=[]
        while q:
            size=len(q)
            ans=[]
            for i in range(size):
                node=q.popleft()
                ans.append(node.val)
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            res.append(ans)
        return res
