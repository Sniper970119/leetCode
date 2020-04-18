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
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def sortList(self, head: ListNode) -> ListNode:
        def merge(l1, l2):
            r = ListNode(0)
            tmp = r
            while l1 and l2:
                if l1.val > l2.val:
                    tmp.next = l2
                    l2 = l2.next
                else:
                    tmp.next = l1
                    l1 = l1.next
                tmp = tmp.next
            while l1:
                tmp.next = l1
                l1 = l1.next
                tmp = tmp.next
            while l2:
                tmp.next = l2
                l2 = l2.next
                tmp = tmp.next
            return r.next, tmp

        k = 1
        cur = head
        while True:
            breakFlag = True
            H = ListNode(0)
            T = H
            th = cur  # tmp head
            count = 1  # tmp 的长度初始化为1
            tmpList = []
            while cur:
                if count == k:
                    tc = cur
                    cur = cur.next
                    tc.next = None
                    tmpList.append(th)
                    th = cur
                    count = 1
                    breakFlag = False
                else:
                    cur = cur.next
                    count += 1
                if len(tmpList) == 2:
                    h, t = merge(tmpList[0], tmpList[1])
                    T.next = h
                    T = t
                    tmpList = []
            if th:
                tmpList.append(th)

            if len(tmpList) == 2:
                h, t = merge(tmpList[0], tmpList[1])
                T.next = h
            elif len(tmpList) == 1:
                h, t = merge(tmpList[0], None)
                T.next = h
            cur = H.next
            if breakFlag is True:
                return cur
            k *= 2


if __name__ == '__main__':
    pass
