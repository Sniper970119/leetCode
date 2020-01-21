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
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        if head is None:
            return
        node = head
        link_list_len = 0
        while node is not None:
            link_list_len += 1
            node = node.next
        if link_list_len < n:
            return head
        if link_list_len == n:
            return head.next
        node = head
        pre = node
        for i in range(link_list_len - n):
            pre = node
            node = node.next
        pre.next = node.next
        return head


if __name__ == '__main__':
    n5 = ListNode(5)
    n4 = ListNode(4)
    n3 = ListNode(3)
    n2 = ListNode(2)
    head = ListNode(1)
    head.next = n2
    n2.next = n3
    n3.next = n4
    n4.next = n5
    print(Solution().removeNthFromEnd(head, 1))
