class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        pre = []
        pre_temp = 1
        post = []
        post_temp = 1
        ans = []
        len_of_nums = len(nums)
        
        for idx in range(len_of_nums):
            pre_temp *= nums[idx]
            pre.append(pre_temp)
            
            post_temp *= nums[len_of_nums - 1 - idx]
            post.insert(0,post_temp)
            
        ans.append(post[1])
        if len_of_nums > 2:    
            for idx in range(1, len_of_nums-1):
                ans.append(pre[idx-1]*post[idx+1])
        ans.append(pre[len_of_nums-2])
        
        return ans
        
        
        
        
            