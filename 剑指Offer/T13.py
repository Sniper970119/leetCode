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


class Solution:
    def movingCount(self, m: int, n: int, k: int) -> int:

        def judge(x, y):
            str_x = str(x)
            str_y = str(y)
            sum = 0
            for each in str_x:
                sum += int(each)
            for each in str_y:
                sum += int(each)
            if sum <= k:
                return True
            return False

        def dfs(x, y, res):
            for ii, jj in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
                if 0 <= x + ii < m and 0 <= y + jj < n and init_map[x + ii][y + jj] == 0 and judge(x + ii, y + jj):
                    init_map[x + ii][y + jj] = 1
                    res = dfs(x + ii, y + jj, res + 1)
            return res

        init_map = [[0 for _ in range(n)] for _ in range(m)]
        init_map[0][0] = 1
        res_output = dfs(0, 0, 1)
        return res_output


if __name__ == '__main__':
    m = 2
    n = 3
    k = 1
    print(Solution().movingCount(m, n, k))
