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
    def shortestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        length = len(s)
        if length == 0:
            return ""
        rs = s[::-1]
        i = 0
        while True:
            if rs[i:] == s[:length - i]:
                break
            i += 1
        return rs[:i] + s


if __name__ == '__main__':
    # s = 'aacecaaa'
    s = 'abcd'
    r = 'aaacecaaa'
    print(Solution().shortestPalindrome(s))
