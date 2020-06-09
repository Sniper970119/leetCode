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


class Solution(object):
    def calculate(self, s):
        """
        :type s: str
        :rtype: int
        """
        return eval(s)
        # stack = []
        # handle = []
        # for each in s:
        #     if each == ' ':
        #         break
        #     if each in ['+', '-', '*', '/']:
        #         handle.append(each)
        #     else:
        #         stack.append(each)
        # pass


if __name__ == '__main__':
    s = '3+2*2'
    print(Solution().calculate(s))
