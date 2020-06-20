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
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        s = []
        flag = head
        while flag is not None:
            s.append(flag.val)
            flag = flag.next
        len_s = len(s)
        if len_s % 2 == 0:
            mid = len_s // 2
            if s[:mid] == s[mid:][::-1]:
                return True
            else:
                return False
        else:
            mid = len_s // 2
            if s[:mid ] == s[mid + 1:][::-1]:
                return True
            else:
                return False
        pass


if __name__ == '__main__':
    n1 = ListNode(-1)
    n2 = ListNode(2)
    n5 = ListNode(3)
    n3 = ListNode(2)
    n4 = ListNode(-1)
    n1.next = n2
    n2.next = n5
    n5.next = n3
    n3.next = n4
    print(Solution().isPalindrome(n1))
