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


class MinStack(object):

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.min = None
        self.stack = []

    def push(self, x):
        """
        :type x: int
        :rtype: None
        """
        if self.min is None:
            self.min = x
        else:
            self.min = min(x, self.min)
        self.stack.insert(0, x)
        print()

    def pop(self):
        """
        :rtype: None
        """
        if len(self.stack) > 0:
            pop_num = self.stack.pop(0)
            if pop_num == self.min:
                if len(self.stack) > 0:
                    self.min = min(self.stack)
                else:
                    self.min = None
            return pop_num
        else:
            return

    def top(self):
        """
        :rtype: int
        """
        if len(self.stack) > 0:
            return self.stack[0]
        else:
            return

    def getMin(self):
        """
        :rtype: int
        """
        return self.min


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()

if __name__ == '__main__':
    obj = MinStack()
    obj.push(-2)
    obj.push(0)
    obj.push(-1)
    print(obj.getMin())
    print(obj.top())
    print(obj.pop())
    print(obj.getMin())

    pass
