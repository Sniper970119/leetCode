# -*- coding:utf-8 -*-
class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        temp = [target - nums[i] for i in range(len(nums))]
        # 使用哈希map来缩短
        for i in range(len(nums)):
            flag = nums[i]
            for j in range(len(temp)):
                if temp[j] == flag and i != j:
                    return [i, j]

    def twoSum1(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        hashmap = {}
        for index, num in enumerate(nums):
            another_num = target - num
            if another_num in hashmap:
                return [hashmap[another_num], index]
            hashmap[num] = index
        return None


if __name__ == '__main__':
    nums = [2, 7, 11, 15]
    nums = [3, 2, 4]
    target = 6
    print(Solution().twoSum1(nums, target))
