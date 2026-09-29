class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()
    
        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            
            st, end = i+1, len(nums)-1
            while st < end:
                current = nums[st] + nums[end]

                if current > -nums[i]:
                    end -= 1
                elif current < -nums[i]:
                    st += 1
                else:
                    res.append([nums[i], nums[st], nums[end]])

                    st += 1
                    end -= 1
                
                    while st < end and nums[st] == nums[st-1]:
                        st += 1
        return res
