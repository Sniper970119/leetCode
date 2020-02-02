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
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        # 检查横排
        for i in range(9):
            flag = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
            for j in range(9):
                if board[i][j] is not '.':
                    if board[i][j] in flag:
                        flag.remove(board[i][j])
                    else:
                        return False
        # 检查竖排
        for i in range(9):
            flag = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
            for j in range(9):
                if board[j][i] is not '.':
                    if board[j][i] in flag:
                        flag.remove(board[j][i])
                    else:
                        return False
        # 检查3*3
        for i in range(0, 9, 3):
            for j in range(0, 9, 3):
                flag = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
                for x in range(i, i + 3):
                    for y in range(j, j + 3):
                        if board[x][y] is not '.':
                            if board[x][y] in flag:
                                flag.remove(board[x][y])
                            else:
                                return False
        return True


if __name__ == '__main__':
    board = [["5", "3", ".", ".", "7", ".", ".", ".", "."], ["6", ".", ".", "1", "9", "5", ".", ".", "."],
             [".", "9", "8", ".", ".", ".", ".", "6", "."], ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
             ["4", ".", ".", "8", ".", "3", ".", ".", "1"], ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
             [".", "6", ".", ".", ".", ".", "2", "8", "."], [".", ".", ".", "4", "1", "9", ".", ".", "5"],
             [".", ".", ".", ".", "8", ".", ".", "7", "9"]]

    print(Solution().isValidSudoku(board))
