# -*- coding:utf-8 -*-

"""
      ┏┛ ┻━━━━━┛ ┻┓
      ┃　　　　　　 ┃
      ┃　　　━　　　┃
      ┃　┳┛　  ┗┳　┃
      ┃　　　　　　 ┃
      ┃　　　┻　　　┃
      ┃　　　　　　 ┃
      ┗━┓　　　┏━━━┛
        ┃　　　┃   神兽保佑
        ┃　　　┃   代码无BUG！
        ┃　　　┗━━━━━━━━━┓
        ┃　　　　　　　    ┣┓
        ┃　　　　         ┏┛
        ┗━┓ ┓ ┏━━━┳ ┓ ┏━┛
          ┃ ┫ ┫   ┃ ┫ ┫
          ┗━┻━┛   ┗━┻━┛
"""


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def zigzagLevelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        res = []
        if not root:
            return []

        def dfs(root, level):
            if len(res) == level:
                res.append([])

            if level % 2:
                res[level].insert(0, root.val)
            else:
                res[level].append(root.val)

            if root.left:
                dfs(root.left, level + 1)
            if root.right:
                dfs(root.right, level + 1)

        dfs(root, 0)
        return res


if __name__ == '__main__':
    root = TreeNode(3)
    n1 = TreeNode(9)
    n2 = TreeNode(20)
    n3 = TreeNode(None)
    n4 = TreeNode(None)
    n5 = TreeNode(15)
    n6 = TreeNode(7)
    root.left = n1
    root.right = n2
    n1.left = n3
    n1.right = n3
    n2.left = n5
    n2.right = n6
    print(Solution().zigzagLevelOrder(root))
