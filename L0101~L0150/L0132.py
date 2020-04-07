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
    def minCut(self, s):
        """
        :type s: str
        :rtype: int
        """
        size = len(s)
        if size < 2:
            return 0

        dp = [i for i in range(size)]
        check_palindrome = [[False for _ in range(size)] for _ in range(size)]

        for right in range(size):
            for left in range(right + 1):
                # 判断当前位置是不是回文串，长度不足2（aa）或者 xabax 格式
                if s[left] == s[right] and (right - left <= 2 or check_palindrome[left + 1][right - 1]):
                    check_palindrome[left][right] = True

        for i in range(1, size):
            if check_palindrome[0][i]:
                dp[i] = 0
                continue
            # 枚举分割点
            dp[i] = min([dp[j] + 1 for j in range(i) if check_palindrome[j + 1][i]])

        return dp[size - 1]


if __name__ == '__main__':
    s = 'aab'
    print(Solution().minCut(s))
