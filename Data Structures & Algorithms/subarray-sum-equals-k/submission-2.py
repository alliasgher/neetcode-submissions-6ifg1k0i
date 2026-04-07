class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:

        mydict = {0:1}
        summ = 0
        res = 0

        for num in nums:
            summ += num

            if summ-k in mydict:
                res += mydict[summ-k]
            mydict[summ] = mydict.get(summ,0) +1
        return res
            
        