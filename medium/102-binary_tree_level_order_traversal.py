from collections import deque

class Solution:
    def levelOrder(self, root: TreeNode | None) -> list[list[int]]:
        res = []

        if root is None:
            return res

        q = deque([root])

        while q:
            size = len(q)
            level = [] 

            for _ in range(size):
                node = q.popleft()
                level.append(node.val) 

                if node.left is not None:
                    q.append(node.left)

                if node.right is not None:
                    q.append(node.right)

            res.append(level)  

        return res
