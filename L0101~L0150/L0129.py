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
    def sumNumbers(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """

        def dfs(temp_root, current_numb):
            """
            dfs
            :param temp_root:
            :return:
            """
            temp_res = 0
            current_numb.append(str(temp_root.val))
            if temp_root.right is None and temp_root.left is None:
                temp_res += int(''.join(current_numb))
                return temp_res
            if temp_root.left is not None:
                temp_res += dfs(temp_root.left, current_numb[:])
            if temp_root.right is not None:
                temp_res += dfs(temp_root.right, current_numb[:])
            return temp_res
        if root is None:
            return 0
        return dfs(root, [])


if __name__ == '__main__':
    root = TreeNode(4)
    node1 = TreeNode(9)
    node2 = TreeNode(0)
    node3 = TreeNode(5)
    node4 = TreeNode(1)
    root.left = node1
    root.right = node2
    node1.left = node3
    node1.right = node4
    print(Solution().sumNumbers(root))
