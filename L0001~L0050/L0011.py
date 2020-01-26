# -*- coding:utf-8 -*-

class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        weights = [[0 for _ in range(len(height))] for _ in range(len(height))]
        for i in range(1, len(weights)):
            for j in range(len(weights) - i):
                for k in range(j, j + i):
                    if min(height[j], height[j + i]) * i < max(weights[j][k], weights[k][j + i]):
                        weights[j][j + i] = max(weights[j][k], weights[k][j + i])
                    else:
                        weights[j][j + i] = min(height[j], height[j + i]) * i
        return max(max(row) for row in weights)




if __name__ == '__main__':
    height = [1, 8, 6, 2, 5, 4, 8, 3, 7]
    print(Solution().maxArea(height))
