# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


from collections import deque
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        queue = deque([root])
        res = []
        
        while queue:
            level = []
            for i in range(len(queue)):
                s = queue.popleft()
                if s:
                    level.append(s.val)
                    queue.append(s.left)
                    queue.append(s.right)
            if level:
                res.append(level)
        return res