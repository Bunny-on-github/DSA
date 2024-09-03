class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        start = 0
        end = len(nums) - 1 
        vals = 0
        for num in nums:
            if num == val:
                vals +=1
        k = len(nums) - vals
        while end > start:
            if nums[end] == val:
                end -= 1
                continue
            if nums[start] == val:
                nums[start] , nums[end] = nums[end],nums[start]
                end -= 1
            start += 1
        return k

