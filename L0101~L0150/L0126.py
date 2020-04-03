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
from collections import defaultdict


class Solution(object):
    def ladderLength(self, beginWord, endWord, wordList):
        """
        :type beginWord: str
        :type endWord: str
        :type wordList: List[str]
        :rtype: int
        """

        def check_word(word_one, word_two):
            """
            单词检查，是否只有一个不重复的字母
            :param word_one:
            :param word_two:
            :return:
            """
            if len(word_one) != len(word_two):
                return False
            flag = False
            for i in range(len(word_two)):
                if word_one[i] != word_two[i] and flag is False:
                    flag = True
                elif word_one[i] != word_two[i]:
                    return False
            return True

        def dfs(cur_word, flag=None):
            """
            深度优先遍历
            :return:
            """
            if flag is None:
                flag = [False for _ in range(len(wordList))]
            if cur_word == endWord:
                temp = [beginWord]
                for i in range(len(wordList)):
                    if flag[i] is True:
                        temp.append(wordList[i])
                res.append(temp)
                return
            for i in range(len(wordList)):
                if flag[i] is False:
                    flag[i] = True
                    if check_word(cur_word, wordList[i]):
                        dfs(wordList[i], flag[:])
                    flag[i] = False
            pass

        if endWord not in wordList or not endWord or not beginWord or not wordList:
            return []

        res = []
        dfs(beginWord)
        min_len = float('inf')
        for each in res:
            if len(each) < min_len:
                min_len = len(each)
        res_fin = []
        for each in res:
            if len(each) == min_len:
                res_fin.append(each)
        return res_fin


if __name__ == '__main__':
    beginWord = "hit"
    endWord = "cog"
    wordList = ["hot", "dot", "dog", "lot", "log", "cog"]
    print(Solution().ladderLength(beginWord, endWord, wordList))
