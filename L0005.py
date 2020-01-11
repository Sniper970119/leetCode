# -*- coding:utf-8 -*-

class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        # 左右走的长度
        flag = 0
        # 回文字开始位置
        start = 0
        for i in range(len(s)):
            if i - flag >= 1 and s[i - flag - 1:i + 2] == s[i - flag - 1:i + 2][::-1]:
                start = i - flag - 1
                flag += 2
                continue
            if i - flag >= 0 and s[i - flag:i + 2] == s[i - flag:i + 2][::-1]:
                start = i - flag
                flag += 1
        return s[start:start + flag + 1]


if __name__ == '__main__':
    # s = 'ccc'
    # s = 'babab'
    s = 'ababd'
    print(Solution().longestPalindrome(s))
