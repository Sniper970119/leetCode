# -*- coding:utf-8 -*-

class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        ll1 = []
        while l1 != None:
            ll1.append(l1.val)
            l1 = l1.next
        ll2 = []
        while l2 != None:
            ll2.append(l2.val)
            l2 = l2.next
        input1 = ''
        for i in range(len(ll1) - 1, -1, -1):
            input1 = input1 + (str(ll1[i]))
        input2 = ''
        for i in range(len(ll2) - 1, -1, -1):
            input2 = input2 + (str(ll2[i]))
        sum_ = str(int(input1) + int(input2))
        return_list = []
        r1 = ListNode(int(sum_[-1]))
        r = r1
        for i in range(len(str(sum_)) - 2, -1, -1):
            return_list.append(int(sum_[i:i + 1]))
            temp = ListNode(int(sum_[i:i + 1]))
            r.next = temp
            r = r.next
        return r1

    def addTwoNumbers1(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        re = ListNode(0)
        r = re
        # 进位，也就是计算个位如果大于10，需要进1位，保存这个1
        carry = 0
        # 如果任意一个不是None
        while (l1 or l2):
            # 取值
            x = l1.val if l1 else 0
            y = l2.val if l2 else 0
            # 计算当前位   上一个的进位+两个数
            s = carry + x + y
            # 计算当前位的进位
            carry = s // 10
            # 初始化并连接当前点
            r.next = ListNode(s % 10)
            r = r.next
            # 向下遍历
            if (l1 != None): l1 = l1.next
            if (l2 != None): l2 = l2.next
        # 全处理完成后进行最后的处理（最大位的进位）
        if (carry > 0):
            r.next = ListNode(1)
        return re.next


if __name__ == '__main__':
    n1 = ListNode(2)
    n2 = ListNode(4)
    n3 = ListNode(3)
    n4 = ListNode(5)
    n5 = ListNode(6)
    n6 = ListNode(4)
    n1.next = n2
    n2.next = n3
    n4.next = n5
    n5.next = n6
    print(Solution().addTwoNumbers1(n1, n4))
