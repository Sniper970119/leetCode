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
    def getPermutation(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: str
        """

        def back(i, flag_list, temp_list=[]):
            """
            回溯
            :return:
            """
            if i == n:
                output.append(temp_list)
                return
            for j in range(len(flag_list)):
                if flag_list[j] != 0:
                    flag_list[j] = 0
                    temp_list.append(j + 1)
                    back(i + 1, flag_list[:], temp_list[:])
                    flag_list[j] = 1
                    temp_list = temp_list[:-1]

        output = []
        flag_list = [1 for _ in range(n)]
        back(0, flag_list)
        res = ''
        for each in output[k-1]:
            res = res+str(each)
        return res

    # chs = [*map(str, range(1, 10))]
    # factor = [1, 1, 2, 6, 24, 120, 720, 5040, 40320, 362880]
    # k -= 1
    # ans = ''
    # for i in range(n - 1, -1, -1):
    #     j, k = divmod(k, factor[i])
    #     ans += chs.pop(j)
    # return ans


if __name__ == '__main__':
    n = 3
    k = 3
    print(Solution().getPermutation(n, k))
