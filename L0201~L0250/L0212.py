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
    def findWords(self, board, words):
        """
        :type board: List[List[str]]
        :type words: List[str]
        :rtype: List[str]
        """
        res = []

        def find_letter(i, j, idx, word, source_word, found_loc):
            base_dir = ['x+', 'x-', 'y+', 'y-']
            if len(word) == 0:
                res.append(source_word)
                return
            target_letter = word[0]
            for each in base_dir:
                # if each in found_dir:
                #     continue
                if each == 'x+' and i < len(board) - 1:
                    if (i + 1, j) in found_loc:
                        continue
                    if board[i + 1][j] == target_letter:
                        found_loc.append((i + 1, j))
                        find_letter(i + 1, j, idx + 1, word[1:], source_word, found_loc)
                        found_loc.pop()
                if each == 'x-' and i > 0:
                    if (i - 1, j) in found_loc:
                        continue
                    if board[i - 1][j] == target_letter:
                        found_loc.append((i - 1, j))
                        find_letter(i - 1, j, idx + 1, word[1:], source_word, found_loc)
                        found_loc.pop()
                if each == 'y+' and j < len(board[0]) - 1:
                    if (i, j + 1) in found_loc:
                        continue
                    if board[i][j + 1] == target_letter:
                        found_loc.append((i, j + 1))
                        find_letter(i, j + 1, idx + 1, word[1:], source_word, found_loc)
                        found_loc.pop()
                if each == 'y-' and j > 0:
                    if (i, j - 1) in found_loc:
                        continue
                    if board[i][j - 1] == target_letter:
                        found_loc.append((i, j - 1))
                        find_letter(i, j - 1, idx + 1, word[1:], source_word, found_loc)
                        found_loc.pop()

        for each in words:
            for i in range(len(board)):
                for j in range(len(board[0])):
                    if each[0] == board[i][j]:
                        find_letter(i, j, 0, each[1:], each, [(i, j)])
        return list(set(res))


if __name__ == '__main__':
    words = ["oath", "pea", "eat", "rain"]
    board = [
        ['o', 'a', 'a', 'n'],
        ['e', 't', 'a', 'e'],
        ['i', 'h', 'k', 'r'],
        ['i', 'f', 'l', 'v']
    ]
    board = [["a", 'b']]
    words = ["ab"]
    print(Solution().findWords(board, words))
