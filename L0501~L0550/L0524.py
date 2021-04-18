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
    def findLongestWord(self, s, dictionary):
        """
        :type s: str
        :type dictionary: List[str]
        :rtype: str
        """
        dictionary = sorted(dictionary)
        points = [0 for _ in range(len(dictionary))]
        finish = [0 for _ in range(len(dictionary))]
        for each in s:
            for i in range(len(dictionary)):
                if finish[i] == 1:
                    continue
                if points[i] < len(dictionary[i]):
                    if dictionary[i][points[i]] == each:
                        points[i] += 1
                    if points[i] == len(dictionary[i]):
                        finish[i] = 1
                else:
                    finish[i] = 1
        max_idx = -1
        max_res = 0
        for i in range(len(dictionary)):
            if finish[i] == 1:
                if max_res < points[i]:
                    max_res = points[i]
                    max_idx = i
        return dictionary[max_idx] if max_idx != -1 else ''


if __name__ == '__main__':
    s = "abpcplea"
    d = ["ale", "apple", "monkey", "plea"]
    s = 'aaa'
    d = ['aaa', 'aa', 'a']
    print(Solution().findLongestWord(s, d))
