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
    def solveSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: None Do not return anything, modify board in-place instead.
        """

        def check(x, y, s):
            """
            检查当前输入是否合法
            :param x:
            :param y:
            :param s:
            :return:
            """
            # 检查横竖
            for i in range(9):
                if board[x][i] == s or board[i][y] == s:
                    return False
            # 检查3*3
            for i in range(3):
                for j in range(3):
                    if board[x // 3 * 3 + i][y // 3 * 3 + j] == s:
                        return False
            return True

        def find_s(cur_idx):
            """
            回朔寻找合适的s
            :param cur_idx:
            :return:
            """
            if cur_idx == 81:
                return True

            # 确定x y
            x, y = cur_idx // 9, cur_idx % 9
            if board[x][y] != '.':
                return find_s(cur_idx + 1)
            for i in range(1, 10):
                str_s = str(i)
                if check(x, y, str_s):
                    board[x][y] = str_s
                    if find_s(cur_idx + 1):
                        return True
                    # 检查不通过，需要回朔，因此将这个位置恢复为空
                    board[x][y] = '.'
            return False

        return find_s(0)
        pass


if __name__ == '__main__':
    board = [["5", "3", ".", ".", "7", ".", ".", ".", "."], ["6", ".", ".", "1", "9", "5", ".", ".", "."],
             [".", "9", "8", ".", ".", ".", ".", "6", "."], ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
             ["4", ".", ".", "8", ".", "3", ".", ".", "1"], ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
             [".", "6", ".", ".", ".", ".", "2", "8", "."], [".", ".", ".", "4", "1", "9", ".", ".", "5"],
             [".", ".", ".", ".", "8", ".", ".", "7", "9"]]
    print(Solution().solveSudoku(board))
