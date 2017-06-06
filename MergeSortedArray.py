class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: void Do not return anything, modify nums1 in-place instead.
        """
        if len(nums1) == 0:
            nums1.extend(nums2)
        else:
            for i in range(n):
                for j in range(len(nums1)):
                    if nums2[i] >= nums1[j]:
                        if j == len(nums1) - 1:
                            nums1.append(nums2[i])
                        else:
                            continue
                    else:
                        nums1.insert(j, nums2[i])
                        break
                    
        x = len(nums1) - m
        while x > 1:
            nums1.pop()
            x -= 1

        return None
