class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:

        remindex = {}
        summ = 0

        for i, num in enumerate(nums):
            if i == 0:
                summ += num
                rem = summ%k
                remindex[rem] = i
                continue
            else:
                summ += num
                rem = summ%k
                if rem == 0:
                    return True
                if rem in remindex:
                    if i - remindex[rem] >=2:
                        return True
                else:
                    remindex[rem] = i

                
        return False
        