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
from collections import deque
import functools


class Solution(object):
    class Solution:
        @functools.lru_cache(None)
        def isScramble(self, s1: str, s2: str) -> bool:
            if s1 == s2:
                return True
            if sorted(s1) != sorted(s2):
                return False
            for i in range(1, len(s1)):
                if self.isScramble(s1[:i], s2[:i]) and self.isScramble(s1[i:], s2[i:]):
                    return True
                if self.isScramble(s1[:i], s2[-i:]) and self.isScramble(s1[i:], s2[:-i]):
                    return True
            return False

    def isScramble1(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: bool
        """
        n = len(s1)
        dp = [0 for _ in range(n + 2)]
        if s1 == s2:
            return True
        split = 0
        for i in range(n):
            for j in range(n):
                if s1[j] == s2[i]:
                    if dp[j] == dp[j + 1] == dp[j + 2] == 0:
                        dp = [0 for _ in range(n + 2)]
                        split += 1
                    dp[j + 1] = max(dp[j], max(dp[j + 1], dp[j + 2])) + 1
                    dp[j] = 0
                    dp[j + 2] = 0
        return split < n
        pass


if __name__ == '__main__':
    s1 = 'great'
    s2 = 'rgeat'
    s1 = 'ab'
    s2 = 'bb'
    print(Solution().isScramble(s1, s2))
