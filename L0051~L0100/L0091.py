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
    def numDecodings(self, s):
        """
        :type s: str
        :rtype: int
        """

        size = len(s)
        # 特判
        if size == 0:
            return 0
        dp = [0] * (size + 1)
        dp[0] = 1
        for i in range(1, size + 1):
            t = int(s[i - 1])
            if t >= 1 and t <= 9:
                dp[i] += dp[i - 1]
            if i >= 2:
                t = int(s[i - 2]) * 10 + int(s[i - 1])
                if t >= 10 and t <= 26:
                    dp[i] += dp[i - 2]
        return dp[-1]


if __name__ == '__main__':
    s = "9371597631128776948387197132267188677349946742344217846154932859125134924241649584251978418763151253"
    # s = '001'
    print(Solution().numDecodings(s))
