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
    def uniquePathsWithObstacles(self, obstacleGrid):
        """
        :type obstacleGrid: List[List[int]]
        :rtype: int
        """

        def is_available(x, y):
            """
            验证当前位置是否可达
            :param x:
            :param y:
            :return:
            """
            if x < len(obstacleGrid) and y < len(obstacleGrid[0]) and obstacleGrid[x][y] == 0:
                return True
            else:
                return False

        def dfs(x, y):
            """
            深度优先遍历
            :param x:
            :param y:
            :return:
            """
            if x == len(obstacleGrid) - 1 and y == len(obstacleGrid[0]) - 1:
                return 1
            res = 0
            for ii, jj in [(0, 1), (1, 0)]:
                if is_available(x + ii, y + jj):
                    res += dfs(x + ii, y + jj)
            return res

        # if len(obstacleGrid) == 1:
        #     if sum(obstacleGrid[0]) >= 1:
        #         return 0
        #     return 1
        if obstacleGrid[0][0] == 1:
            return 0
        res = dfs(0, 0)
        return res

    def uni(self, obstacleGrid):
        m, n = len(obstacleGrid[0]), len(obstacleGrid)
        dp = [1] + [0] * m
        for i in range(0, n):
            for j in range(0, m):
                dp[j] = 0 if obstacleGrid[i][j] else dp[j] + dp[j - 1]
        return dp[-2]


if __name__ == '__main__':
    obta = [
        [0, 0, 0],
        [0, 1, 0],
        [0, 0, 0]
    ]
    # print(Solution().uniquePathsWithObstacles(obta))
    print(Solution().uni(obta))
