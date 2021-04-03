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
        ┃CREATE BY SNIPER┣┓
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
        tag = ['a', 'e', 'i', 'o', 'u']
        left, right = 0, len(s) - 1
        list_s = list(s)
        while left <= right:
            if list_s[left].lower() not in tag:
                left += 1
            elif list_s[left].lower() in tag and list_s[right].lower() in tag:
                list_s[left], list_s[right] = list_s[right], list_s[left]
                right -= 1
                left += 1
            elif list_s[right].lower() not in tag:
                right -= 1
        return ''.join(list_s)


if __name__ == '__main__':
    s = 'hello'
    s = 'leetcode'
    s = 'ai'
    print(Solution().reverseVowels(s))
