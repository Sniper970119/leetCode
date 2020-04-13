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
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: List[str]
        """
        if not s:
            return []
        _len, wordDict = len(s), set(wordDict)
        _min, _max = 2147483647, -2147483648
        for word in wordDict:
            _min = min(_min, len(word))
            _max = max(_max, len(word))

        def dfs(start):  # 返回s[start:]能由字典构成的所有句子
            if start not in memo:
                res = []
                for i in range(_min, min(_max, _len - start) + 1):
                    if s[start: start + i] in wordDict:
                        res.extend(list(map(lambda x: s[start: start + i] + ' ' + x, dfs(start + i))))
                memo[start] = res
            return memo[start]

        memo = {_len: ['']}
        return list(map(lambda x: x[:-1], dfs(0)))


if __name__ == '__main__':
    s = "catsanddog"
    wordDict = ["cat", "cats", "and", "sand", "dog"]
    print(Solution().wordBreak(s, wordDict))
