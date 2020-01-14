# -*- coding:utf-8 -*-
class Solution(object):
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        if len(p) <= 0:
            return len(s) <= 0
        match = len(s) > 0 and (s[0] == p[0] or p[0] == '.')
        if len(p) > 1 and p[1] == '*':
            # 对应*是无用的（也就是0次）   和    *是有用的
            return self.isMatch(s, p[2:]) or (match and self.isMatch(s[1:], p))
        else:
            return match and self.isMatch(s[1:], p[1:])


if __name__ == '__main__':
    s = 'aaa'
    p = 'ab*a*c*a'
    s = 'mississippi'
    p = 'mis*is*p*.'
    print(Solution().isMatch(s, p))
