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
    def diffWaysToCompute(self, input):
        """
        :type input: str
        :rtype: List[int]
        """
        res = []
        ops = {'+': lambda x, y: x + y, '-': lambda x, y: x - y, '*': lambda x, y: x * y}
        for idx in range(1, len(input) - 1):
            if input[idx] in ops.keys():
                for left in self.diffWaysToCompute(input[:idx]):
                    for right in self.diffWaysToCompute(input[idx + 1:]):
                        res.append(ops[input[idx]](left, right))
        if not res:
            res.append(int(input))
        return res


if __name__ == '__main__':
    input = '2*3-4*5'
    print(Solution().diffWaysToCompute(input))
