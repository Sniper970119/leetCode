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
    def validPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        if len(s) < 2:
            return True
        can_jump = True
        left, right = 0, len(s) - 1
        while left <= right:
            if s[left] == s[right]:
                left += 1
                right -= 1
            elif self.verify(s[left + 1: right+1]) or self.verify(s[left: right]):
                return True
            else:
                return False
        return True

    def verify(self, s):
        """
        直接判断是否为回文串
        :param s:
        :return:
        """
        if len(s) % 2 == 0:
            mid = int(len(s) / 2)
            if s[:mid] == s[mid:][::-1]:
                return True
            else:
                return False
        else:
            mid = len(s) // 2
            if s[:mid] == s[mid + 1:][::-1]:
                return True
            else:
                return False


if __name__ == '__main__':
    s = 'abba'
    s = "tcaac"
    s = "cbbcc"
    s = "aguokepatgbnvfqmgmlcupuufxoohdfpgjdmysgvhmvffcnqxjjxqncffvmhvgsymdjgpfdhooxfuupuculmgmqfvnbgtapekouga"
    print(Solution().validPalindrome(s))
    # print(Solution().verify(s))
