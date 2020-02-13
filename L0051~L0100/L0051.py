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
    def solveNQueens(self, n):
        """
        :type n: int
        :rtype: List[List[str]]
        """

        def check(i, j, temp_dir):
            for x in range(n):
                # 检查横竖
                if temp_dir[x][j] is 'Q' or temp_dir[i][x] is 'Q':
                    return False
                # 检查右上斜线
                if i + x < n and j - x >= 0:
                    if temp_dir[i + x][j - x] is 'Q':
                        return False
                # 检查左下斜线
                if i - x >= 0 and j + x < n:
                    if temp_dir[i - x][j + x] is 'Q':
                        return False
                # 检查左上斜线
                if i - x >= 0 and j - x >= 0:
                    if temp_dir[i - x][j - x] is 'Q':
                        return False
                # 检查右下斜线
                if i + x < n and j + x < n:
                    if temp_dir[i + x][j + x] is 'Q':
                        return False
            return True

        def back(x, from_x_idx, temp_dir):
            if x == n:
                import copy
                res.append(copy.deepcopy(temp_dir))
                return
            if from_x_idx > n - 1:
                return
            for i in range(from_x_idx, n):
                for j in range(n):
                    if temp_dir[i][j] is not 'Q' and check(i, j, temp_dir):
                        temp_dir[i][j] = 'Q'
                        back(x + 1, i + 1, temp_dir[:])
                        temp_dir[i][j] = '.'

        res = []
        init_map = [['.' for _ in range(n)] for _ in range(n)]
        back(0, 0, init_map)
        res_final = []
        for i in range(len(res)):
            temp_res = []
            for j in range(n):
                temp_res.append("".join(res[i][j]))
            res_final.append(temp_res)
        return res_final


if __name__ == '__main__':
    n = 8
    print(Solution().solveNQueens(n))
