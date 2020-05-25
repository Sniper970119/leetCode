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
    def findOrder(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: List[int]
        """
        res_list = []
        remove_list = []

        def find():
            out_dgree = [0 for _ in range(numCourses)]
            for i in range(len(res_list)):
                out_dgree[res_list[i]] = float('inf')
            for i in range(len(prerequisites)):
                x, y = prerequisites[i]
                if i in remove_list:
                    continue
                out_dgree[x] += 1
            first_zero = -1
            for i in range(len(out_dgree)):
                if out_dgree[i] == 0:
                    first_zero = i
                    break
            if first_zero == -1:
                if len(res_list) == numCourses:
                    return True
                return False
            res_list.append(first_zero)
            for i in range(len(prerequisites)):
                x, y = prerequisites[i]
                if y == first_zero:
                    remove_list.append(i)
                    # prerequisites.remove(each)
            if find():
                return True
            else:
                return False
            pass

        if find():
            return res_list
        else:
            return []


if __name__ == '__main__':
    num, pre = 4, [[1, 0], [2, 0], [3, 1], [3, 2]]
    num, pre = 2, [[0, 1]]
    print(Solution().findOrder(num, pre))
    pass
