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
    def minPathSum(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        dp = [0] * (len(grid[0]) + 1)
        for i in range(len(grid[0])):
            dp[i] = grid[0][i] + dp[i - 1]
        dp[-1] = float('inf')
        for i in range(1, len(grid)):
            for j in range(len(grid[0])):
                dp[j] = min(dp[j - 1] + grid[i][j], dp[j] + grid[i][j])
        return dp[-2]


if __name__ == '__main__':
    grid = [
        [1, 3, 1],
        [1, 5, 1],
        [4, 2, 1]
    ]
    grid = [[1, 2, 5], [3, 2, 1]]
    print(Solution().minPathSum(grid))
