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
    def buildTree(self, inorder, postorder):
        """
        :type inorder: List[int]
        :type postorder: List[int]
        :rtype: TreeNode
        """

        def iter_node(temp_inorder, temp_postorder):
            if len(temp_inorder) == 0 or len(temp_postorder)==0:
                return None
            if len(temp_inorder) == 1:
                return TreeNode(temp_postorder[-1])
            root_idx = temp_inorder.index(temp_postorder[-1])
            root = TreeNode(temp_postorder[-1])
            root.right = iter_node(temp_inorder[root_idx + 1:], temp_postorder[root_idx:-1])
            root.left = iter_node(temp_inorder[:root_idx], temp_postorder[:root_idx])
            return root

        root = iter_node(inorder, postorder)
        return root


if __name__ == '__main__':
    inorder = [9, 3, 15, 20, 7]
    postorder = [9, 15, 7, 20, 3]
    inorder = [1,2,3,4]
    postorder = [2,1,4,3]
    print(Solution().buildTree(inorder, postorder))
