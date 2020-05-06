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

from functools import cmp_to_key


def cmp(x1, x2):
    temp1 = x1 + x2
    temp2 = x2 + x1
    return -1 if int(temp1) >= int(temp2) else 1


class Solution:
    def largestNumber(self, nums):
        str_num = list(map(str, nums))
        str_num.sort(key=cmp_to_key(cmp))
        ans = "".join(str_num)
        idx = 0
        while idx < len(ans) and ans[idx] == '0':
            idx += 1
        return ans[idx:] if idx < len(ans) else '0'


if __name__ == '__main__':
    nums = [3, 30, 34, 5, 9]
    print(Solution().largestNumber(nums))
