class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        if target in nums:
            return nums.index(target)
        else:
            i = 0
            while i < len(nums):
                if target > nums[i]:
                    i += 1
                    continue
                else:
                    nums.insert(i, target)
                    return nums.index(target)
            if i == len(nums):
                nums.append(target)
                return nums.index(target)
