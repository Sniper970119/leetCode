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
    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """
        n = len(board)
        m = len(board[0])

        def dfs(i, j, index):
            mp[i][j] = False
            if index == len(word):
                return True
            for ii, jj in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                if 0 <= i + ii < n and 0 <= j + jj < m and board[i + ii][j + jj] == word[index] and mp[i + ii][j + jj]:
                    if dfs(i + ii, j + jj, index + 1):
                        return True
            mp[i][j] = True
            return False

        for i in range(n):
            for j in range(m):
                if board[i][j] == word[0]:
                    mp = [[True] * m for i in range(n)]
                    if dfs(i, j, 1):
                        return True
        return False


if __name__ == '__main__':
    board = [
        ['A', 'B', 'C', 'E'],
        ['S', 'F', 'C', 'S'],
        ['A', 'D', 'E', 'E']
    ]
    word = 'ABCB'
    print(Solution().exist(board, word))
