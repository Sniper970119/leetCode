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
    def divide(self, dividend, divisor):
        """
        :type dividend: int
        :type divisor: int
        :rtype: int
        """
        negative = False
        res = 0
        count = 0
        if divisor < 0 < dividend:
            negative = True
        if dividend < 0 < divisor:
            negative = True
        dividend = abs(dividend)
        divisor = abs(divisor)
        while dividend >= divisor:
            count += 1
            divisor <<= 1
        while count > 0:
            count -= 1
            divisor >>= 1
            res <<= 1
            if dividend >= divisor:
                res += 1
                dividend -= divisor
        if negative:
            res = -res
        return res if -(1 << 31) <= res <= (1 << 31)-1 else (1 << 31) - 1


if __name__ == '__main__':
    dividend = -2147483648
    divisor = 1
    # dividend = 10
    # divisor = 3
    print(Solution().divide(dividend, divisor))
