# -*- coding:utf-8 -*-
class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        if x < (-2 ** 31) or x > (2 ** 31 - 1):
            return 0
        if x < 0:
            str_x = str(-x)
            res = -int(str_x[::-1])
            if res < (-2 ** 31) or res > (2 ** 31 - 1):
                return 0
            return -int(str_x[::-1])
        str_x = str(x)
        res = int(str_x[::-1])
        if res < (-2 ** 31) or res > (2 ** 31 - 1):
            return 0
        return res


if __name__ == '__main__':
    x = 1534236469
    print(Solution().reverse(x))
