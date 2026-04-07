class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        # l,r = 0, len(numbers) -1

        # while l<r:
        #     if numbers[l] + numbers[r] > target:
        #         r-= 1
        #     elif numbers[l] + numbers[r] < target:
        #         l+= 1
        #     else:
        #         return [l+1,r+1]

        # return []


        #binary
        for i in range(len(numbers)):
            l,r = i+1, len(numbers) -1
            tmp = target - numbers[i]

            while l<=r:
                mid = (l+r) // 2
                if numbers[mid] == tmp:
                    return [i+1, mid+1]
                elif numbers[mid] > tmp:
                    r = mid-1
                else:
                    l = mid+1
        
        return []

    