# solutio using two pointers  
class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        l , r = 0 , 0
        d = {}
        while r < len(nums):
            for idx,num in enumerate(nums):
                if not d.get(num):
                    d[nums[r]] = [1,r] 
                    r += 1
                else:
                    d[nums[r]][0] += 1
                    l = d[nums[r]][1]
                    if r - l <= k:
                        return True
                    else:
                        d[nums[r]][1] = r
                        r += 1
        return False
