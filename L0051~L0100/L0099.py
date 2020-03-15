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
    def recoverTree(self, root):
        """
        :type root: TreeNode
        :rtype: None Do not return anything, modify root in-place instead.
        """

        self.tmp = None
        self.w1 = self.w2 = None

        def morris(root):
            cur = root
            while cur:
                if cur.left:
                    pre = cur.left
                    while pre.right and pre.right != cur:
                        pre = pre.right
                    if not pre.right:
                        pre.right = cur
                        cur = cur.left
                        continue
                    else:
                        pre.right = None
                if self.tmp and cur.val < self.tmp.val:
                    if not self.w1:
                        self.w1 = self.tmp
                    self.w2 = cur

                self.tmp = cur
                cur = cur.right

        morris(root)
        self.w1.val ^= self.w2.val
        self.w2.val ^= self.w1.val
        self.w1.val ^= self.w2.val
        pass


if __name__ == '__main__':
    print(Solution().recoverTree(1))
