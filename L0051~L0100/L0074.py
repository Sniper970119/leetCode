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
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        if len(matrix) == 0 or len(matrix[0]) == 0:
            return False
        target_list_idx = 0
        for i in range(len(matrix)):
            if matrix[i][0] > target:
                break
            target_list_idx = i
        target_list_len = len(matrix[target_list_idx])
        left = 0
        right = target_list_len - 1
        while left <= right:
            if left < 0 or right > target_list_len - 1:
                return False
            mid = int((left + right) / 2)
            nub = matrix[target_list_idx][mid]
            if nub == target:
                return True
            elif nub < target:
                left = mid + 1
            else:
                right = mid - 1
        return False


if __name__ == '__main__':
    matrix = [
        [1, 3, 5, 7],
        [10, 11, 16, 20],
        [23, 30, 34, 50]
    ]
    target =3
    matrix = [[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 50]]
    # print(len(matrix))
    # print(len(matrix[0]))
    print(Solution().searchMatrix(matrix, target))
