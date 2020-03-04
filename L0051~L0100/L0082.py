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
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        ph = ListNode(0)
        ph.next = head
        p = ph
        while p:  # p 是当前处理的节点的前一个节点，只有保存前一个节点才有办法删掉当前节点
            if not p.next: break
            q = p.next  # q 是当前处理的节点
            r = q.next
            while r:  # 使用 r 往后查找是否有与当前节点（q）重复的节点
                if r.val != q.val:
                    break
                r = r.next
            if r != q.next:  # 如果有重复的，删除这些节点
                p.next = r
            else:
                p = p.next
        return ph.next
