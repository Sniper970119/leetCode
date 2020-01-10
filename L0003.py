# -*- coding:utf-8 -*-
class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        st = {}
        i, ans = 0, 0
        for j in range(len(s)):
            if s[j] in st:
                i = max(st[s[j]], i)
            ans = max(ans, j - i + 1)
            st[s[j]] = j + 1
        return ans

    def lengthOfLongestSubstring1(self, s):
        """
        :type s: str
        :rtype: int
        """
        st = {}
        i, ans = -1, 0
        for j in range(len(s)):
            if s[j] in st:
                i = max(st[s[j]], i)
            ans = max(ans, j - i)
            st[s[j]] = j
        return ans


if __name__ == '__main__':
    str1 = 'abcabcbb'
    print(Solution().lengthOfLongestSubstring1(str1))
