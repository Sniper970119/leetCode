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
    def buildTree(self, preorder, inorder):
        """
        :type preorder: List[int]
        :type inorder: List[int]
        :rtype: TreeNode
        """

        def iter_node(temp_pre_order, temp_in_order):
            if len(temp_in_order) == 0:
                return
            if len(temp_in_order) == 1:
                return TreeNode(temp_pre_order[0])
            root_idx = temp_in_order.index(temp_pre_order[0])
            root = TreeNode(temp_pre_order[0])
            root.left = iter_node(temp_pre_order[1:], temp_in_order[:root_idx])
            root.right = iter_node(temp_pre_order[root_idx + 1:], temp_in_order[root_idx + 1:])
            return root

        root = iter_node(preorder, inorder)
        return root


if __name__ == '__main__':
    preorder = [3, 9, 20, 15, 7]
    inorder = [9, 3, 15, 20, 7]
    # preorder = [1, 2, 3, 4, 5]
    # inorder = [3, 2, 1, 4, 5]
    print(Solution().buildTree(preorder, inorder))
