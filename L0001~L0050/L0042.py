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
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        n = len(height)
        if n <= 2:
            return 0
        left = 0
        right = n - 1
        sum = 0
        while left < right:
            if height[left] != 0 and height[right] != 0:
                min_flag = min(height[left], height[right])
                for i in range(left, right + 1):
                    if height[i] < min_flag:
                        sum += min_flag - height[i]
                        height[i] = min_flag
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1
        return sum



if __name__ == '__main__':
    height = [0, 1, 0]
    print(Solution().trap(height))
