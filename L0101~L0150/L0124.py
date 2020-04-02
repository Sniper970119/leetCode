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
    def maxPathSum(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """

        self.res = float('-inf')

        def dfs(root):
            if not root:
                return 0
            val = root.val
            sum_left = max(0, dfs(root.left))
            sum_right = max(0, dfs(root.right))

            node_sum = val + sum_left + sum_right
            self.res = max(self.res, node_sum)
            return max(sum_right, sum_left) + val

        dfs(root)
        return self.res


if __name__ == '__main__':
    root1 = TreeNode(1)
    node2 = TreeNode(2)
    node3 = TreeNode(3)
    root1.left = node2
    # root1.right = node3

    root2 = TreeNode(-10)
    node4 = TreeNode(9)
    node5 = TreeNode(20)
    node8 = TreeNode(15)
    node9 = TreeNode(7)
    root2.left = node4
    root2.right = node5
    node5.left = node8
    node5.right = node9

    root3 = TreeNode(1)
    node10 = TreeNode(-2)
    node11 = TreeNode(-3)
    node12 = TreeNode(1)
    node13 = TreeNode(3)
    node14 = TreeNode(-2)
    node15 = TreeNode(-1)
    root3.left = node10
    root3.right = node11
    node10.left = node12
    node10.right = node13
    node11.left = node14
    node12.left = node15

    print(Solution().maxPathSum(root2))
    pass
