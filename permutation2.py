#https://leetcode.com/problems/permutations-ii/


class Solution:
    def permuteUnique(self, nums):
      final_result = []
      if len(nums) ==1 : return [[1]]
      if len(nums) ==2 : return [nums,nums[::-1]] if nums != nums[::-1] else [nums]
      else:
        first = nums[0]
        rest = nums[1:]
        rest_perm = self.permuteUnique(rest)
        
        for i in rest_perm:
          for k in range(len(i)+1):
            comb = i[:k]+[first]+i[k:]
            if comb not in final_result: final_result.append(comb)             
        return final_result


obj = Solution()
obj.permuteUnique([12,4,56,3])
