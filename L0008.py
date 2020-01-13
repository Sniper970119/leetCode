# -*- coding:utf-8 -*-
class Solution(object):
    def myAtoi(self, str):
        """
        :type str: str
        :rtype: int
        """
        import re
        return max(min(int(*re.findall('^[\+\-]?\d+', str.lstrip())), 2**31 - 1), -2**31)


if __name__ == '__main__':
    s = '  -4193 with words'
    print(Solution().myAtoi(s))
    pass
