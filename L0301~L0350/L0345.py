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
    def reverseVowels(self, s):
        """
        :type s: str
        :rtype: str
        """
        _s = []
        for each in s:
            _s.append(each)
        left = 0
        right = len(s) - 1
        while left <= right:
            if _s[left].lower() in ['a', 'e', 'i', 'o', 'u']:
                pass
            else:
                left += 1
                continue
            if _s[right].lower() in ['a', 'e', 'i', 'o', 'u']:
                _s[left], _s[right] = _s[right], _s[left]
                left += 1
                right -= 1
                pass
            else:
                right -= 1
        s = ''
        for each in _s:
            s += each
        return s


if __name__ == '__main__':
    s = 'hello'
    print(Solution().reverseVowels(s))
