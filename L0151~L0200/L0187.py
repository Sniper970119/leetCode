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


class Solution:
    def findRepeatedDnaSequences(self, s: str):
        dic = {'A': 0, 'C': 1, 'G': 2, 'T': 3}
        res = []
        hashmap = {}
        mask = 0
        for i in range(len(s) - 9):
            if i == 0:
                for j in range(i, i + 10):
                    mask = 4 * mask + dic[s[j]]  # 1
            else:
                mask = 4 * (mask - dic[s[i - 1]] * 4 ** 9) + dic[s[i + 9]]  # 2
            hashmap[mask] = hashmap.get(mask, 0) + 1
            if hashmap[mask] == 2:
                res.append(s[i:i + 10])
        return res


if __name__ == '__main__':
    s = "AAAAACCCCCAAAAACCCCCCAAAAAGGGTTT"
    print(Solution().findRepeatedDnaSequences(s))
