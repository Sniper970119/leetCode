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
    def levelOrderBottom(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if root is None:
            return []
        queue = [root]
        res = [[root.val]]
        while len(queue) > 0:
            temp_list = []
            temp_queue = queue[:]
            for each in temp_queue:
                if each.left is not None and each.left.val is not None:
                    temp_list.append(each.left.val)
                    queue.append(each.left)
                if each.right is not None and each.right.val is not None:
                    temp_list.append(each.right.val)
                    queue.append(each.right)
                    pass
                queue.pop(0)
            res.append(temp_list)
        res = res[:-1]
        return res[::-1]
        pass


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
    print(Solution().levelOrderBottom(root))
