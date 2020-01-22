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


class Solution(object):
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        if l1 is None and l2 is None:
            return
        if l1 is None or l2 is None:
            return l1 if l2 is None else l2
        if l1.val > l2.val:
            return self.mergeTwoLists(l2, l1)
        res = ListNode(l1.val)
        node = res
        l1 = l1.next
        while l1 is not None and l2 is not None:
            if l1.val < l2.val:
                node.next = l1
                l1 = l1.next
            else:
                node.next = l2
                l2 = l2.next
            node = node.next
        while l1 is not None:
            node.next = l1
            l1 = l1.next
            node = node.next

        while l2 is not None:
            node.next = l2
            l2 = l2.next
            node = node.next

        return res


if __name__ == '__main__':
    l1 = ListNode(-9)
    l2 = ListNode(3)
    # l3 = ListNode(4)
    l1.next = l2
    # l2.next = l3
    ll1 = ListNode(5)
    ll2 = ListNode(7)
    # ll3 = ListNode(4)
    ll1.next = ll2
    # ll2.next = ll3
    print(Solution().mergeTwoLists(l1, ll1))
