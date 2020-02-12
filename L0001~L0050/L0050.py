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
    def myPow(self, x, n):
        """
        :type x: float
        :type n: int
        :rtype: float
        """
        if n == 0:
            return 1.0
        n_negative = False
        if n < 0:
            n = -n
            n_negative = True
        flag = 1
        times = 0
        while 2 * flag <= n:
            flag = flag << 1
            times += 1
        # 尝试判断下一个和当前哪一个离n更近
        n_is_nearly = True
        if flag * 2 - n < n - flag:
            n_is_nearly = False
        sum = x
        for i in range(times):
            sum *= sum
        if n_is_nearly:
            for i in range(n - flag):
                sum *= x
        else:
            sum *= sum
            for i in range(2 * flag - n):
                sum /= x
        return sum if n_negative is False else 1.0 / sum

    def myPow1(self, x, n):
        """
        :type x: float
        :type n: int
        :rtype: float
        """
        i = n
        if i < 0: i = -i
        res = 1
        while i != 0:
            if i % 2 != 0: res *= x
            x *= x
            i = i // 2
        return res if n > 0 else 1 / res

if __name__ == '__main__':
    x = 0.00001
    n = 2147483647
    print(Solution().myPow(x, n))
