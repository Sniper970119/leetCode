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
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        res = ListNode(None)
        point = res
        while len(lists) > 0:
            min_val = None
            for each in lists:
                if each is None:
                    # lists.remove(each)
                    continue
                if min_val is None or each.val < min_val.val:
                    min_val = each
            if min_val is None:
                return res.next

            point.next = min_val
            point = point.next
            for i in range(len(lists)):
                if lists[i] is not None and lists[i].val == min_val.val:
                    print(min_val.val)
                    lists[i] = lists[i].next
                    break
        return res.next

    def mergeKLists1(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        from queue import PriorityQueue
        head = point = ListNode(0)
        q = PriorityQueue()
        for each in lists:
            while each is not None:
                q.put(each.val)
                each = each.next
        while not q.empty():
            val = q.get()
            point.next = ListNode(val)
            point = point.next
        return head.next


if __name__ == '__main__':
    n1 = ListNode(1)
    n2 = ListNode(4)
    n3 = ListNode(5)
    n4 = ListNode(1)
    n5 = ListNode(3)
    n6 = ListNode(4)
    n7 = ListNode(2)
    n8 = ListNode(6)
    n1.next = n2
    n2.next = n3
    n4.next = n5
    n5.next = n6
    n7.next = n8
    lists = [n1, n4, n7]
    print(Solution().mergeKLists1(lists))
