class Solution:
        # @param {integer[]} nums
        # @return {integer[]}
        def productExceptSelf(self, nums):
            p = 1
            n = len(nums)
            output = []
            for i in range(0,n):
                output.append(p)
                p = p * nums[i]
                print(output)
            print("="*20)
            p = 1
            for i in range(n-1,-1,-1):
                output[i] = output[i] * p
                p = p * nums[i]
                print(output)
            return output

sol = Solution()
print(sol.productExceptSelf([1,2,3,4]))