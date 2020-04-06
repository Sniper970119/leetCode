# -*- c'O',ding:utf-8 -*-

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
    def solve(self, board):
        """
        :type board: List[List[str]]
        :rtype: None Do not return anything, modify board in-place instead.
        """
        if not board: return
        row = len(board)
        col = len(board[0])
        if row < 3 or col < 3: return

        def dfs(i, j):
            """
            dfs
            :param i:
            :param j:
            :return:
            """
            if i < 0 or j < 0 or i >= row or j >= col or board[i][j] != 'O':
                return
            board[i][j] = '#'
            dfs(i - 1, j)
            dfs(i + 1, j)
            dfs(i, j - 1)
            dfs(i, j + 1)

        for i in range(row):
            dfs(i, 0)
            dfs(i, col - 1)

        for i in range(col):
            dfs(0, i)
            dfs(row - 1, i)

        for i in range(0, row):
            for j in range(0, col):
                if board[i][j] == 'O':
                    board[i][j] = 'X'
                if board[i][j] == '#':
                    board[i][j] = 'O'
        return board


if __name__ == '__main__':
    board = [
        ['X', 'X', 'X', 'X'],
        ['X', 'O', 'O', 'X'],
        ['X', 'X', 'O', 'X'],
        ['X', 'O', 'X', 'X'],
    ]
    board = [["O", "X", "X", "O", "X"],
             ["X", "O", "O", "X", "O"],
             ["X", "O", "X", "O", "X"],
             ["O", "X", "O", "O", "O"],
             ["X", "X", "O", "X", "O"]]
    print(Solution().solve(board))
