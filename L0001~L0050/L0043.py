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
    def multiply(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        if num1 == '0' or num2 == '0':
            return "0"
        m, n = len(num1), len(num2)
        res = [0 for _ in range(m + n)]
        for i in range(m - 1, -1, -1):
            for j in range(n - 1, -1, -1):
                x, y = int(num1[i]), int(num2[j])
                res[i + j + 1] += x * y % 10
                res[i + j] += x * y // 10  # 进位
        print(res)
        # [8, 17, 26, 19, 10, 1] -> [9, 9, 8, 0, 0, 1]
        # 从后往前遍历, 处理进位
        for i in range(m + n - 1, 0, -1):
            carry = res[i] // 10
            # if carry:
            res[i] = res[i] % 10
            res[i - 1] += carry
        ans = ''.join([str(x) for x in res]).lstrip('0')
        return ans


if __name__ == '__main__':
    num1 = '123'
    num2 = '456'
    print(Solution().multiply(num1, num2))
