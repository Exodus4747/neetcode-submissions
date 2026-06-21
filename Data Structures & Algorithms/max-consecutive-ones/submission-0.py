class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        Max_cons = 0
        cons = 0
        for i in (nums):
            
            if i != 1:
                cons = 0
            else:
                cons+= 1
            if cons > Max_cons:
                Max_cons = cons
        return Max_cons