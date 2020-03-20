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


# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def sortedListToBST(self, head):
        """
        :type head: ListNode
        :rtype: TreeNode
        """
        nums = []
        while head:
            nums.append(head.val)
            head = head.next

        def handle(temp_nums):
            if len(temp_nums) == 0:
                return None
            if len(temp_nums) == 1:
                return TreeNode(temp_nums[0])
            n = len(temp_nums) // 2
            root = TreeNode(temp_nums[n])
            root.left = handle(temp_nums[:n])
            root.right = handle(temp_nums[n + 1:])
            return root

        root = handle(nums)
        return root


if __name__ == '__main__':
    head = ListNode(-10)
    n1 = ListNode(-3)
    n2 = ListNode(0)
    n3 = ListNode(5)
    n4 = ListNode(9)
    head.next = n1
    n1.next = n2
    n2.next = n3
    n3.next = n4
    print(Solution().sortedListToBST(head))