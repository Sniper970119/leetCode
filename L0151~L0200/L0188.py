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
    def maxProfit(self, k, prices):
        """
        :type k: int
        :type prices: List[int]
        :rtype: int
        """
        if prices == [] or k == 0:
            return 0
        if k >= 10000000:
            profit = 0
            for i in range(1, len(prices)):
                tmp = prices[i] - prices[i - 1]
                if tmp > 0: profit += tmp
            return profit
        dp = [[[0 for _ in range(k + 1)] for _ in range(2)] for _ in range(len(prices))]
        dp[0][0][0] = 0
        dp[0][1][0] = -prices[0]
        for i in range(k):
            dp[0][0][i + 1] = float('-inf')
            dp[0][1][i + 1] = float('-inf')
        for i in range(1, len(prices)):
            # 没卖过没买过
            dp[i][0][0] = 0
            # 卖过k次,当前不持股
            for j in range(1, k + 1):
                dp[i][0][j] = max(dp[i - 1][0][j], dp[i - 1][1][j - 1] + prices[i])
            # 卖过k次，当前持股
            for j in range(1, k + 1):
                dp[i][1][j - 1] = max(dp[i - 1][1][j - 1], dp[i - 1][0][j - 1] - prices[i])
            dp[i][1][-1] = float('-inf')
        return max(max(dp[-1][0]), 0)
        pass


if __name__ == '__main__':
    k = 2
    prices = [3, 2, 6, 5, 0, 3]
    print(Solution().maxProfit(k, prices))
