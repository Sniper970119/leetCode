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
    def numDistinct(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: int
        """
        def back(ii, t_flag):
            nums = 0
            if len(t_flag) == 0:
                res_list.append(s_flag[:])
                return 1
            for i in range(ii, len(s)):
                if t_flag[0] == s[i] and s_flag[i] == 0:
                    if len(t_flag) > 1:
                        temp_t_flag = t_flag[1:]
                    else:
                        temp_t_flag = []
                    s_flag[i] = 1
                    nums += back(i, temp_t_flag[:])
                    s_flag[i] = 0
            return nums

        res_list = []
        s_flag = [0 for _ in range(len(s))]
        t_flag = t[:]
        nums = back(0, t_flag)
        return nums
        pass

    # def numDistinct(self, s: str, t: str) -> int:
    #     n1 = len(s)
    #     n2 = len(t)
    #     dp = [[0] * (n1 + 1) for _ in range(n2 + 1)]
    #     for j in range(n1 + 1):
    #         dp[0][j] = 1
    #     for i in range(1, n2 + 1):
    #         for j in range(1, n1 + 1):
    #             if t[i - 1] == s[j - 1]:
    #                 dp[i][j] = dp[i - 1][j - 1] + dp[i][j - 1]
    #             else:
    #                 dp[i][j] = dp[i][j - 1]
    #     # print(dp)
    #     return dp[-1][-1]



if __name__ == '__main__':
    S = "rabbbit"
    T = "rabbit"
    S = "babgbag"
    T = "bag"
    print(Solution().numDistinct(S, T))
