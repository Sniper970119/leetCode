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
    def partition(self, s):
        """
        :type s: str
        :rtype: List[List[str]]
        """
        a = [[s[0]]]
        for i in range(1, len(s)):
            for j in a[:len(a)]:
                if len(j) > 1 and s[i] == j[-2]:
                    a.append(j[:-2] + [j[-2] + j[-1] + s[i]])
                if s[i] == j[-1]:
                    a.append(j[:-1] + [s[i] * 2])
                j.append(s[i])
        return a


if __name__ == '__main__':
    s = 'aab'
    print(Solution().partition(s))
