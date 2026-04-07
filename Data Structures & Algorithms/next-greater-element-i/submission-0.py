class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:

        stack = []
        dic = {}

        for num in nums2:
            while stack and num > stack[-1]:
                val = stack.pop()
                dic[val] = num
            
            stack.append(num)
        
        output = []

        for num in nums1:
            if num in dic:
                output.append(dic[num])
            else:
                output.append(-1)

        return output
        