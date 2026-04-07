class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        output = [0 for _ in range(len(temperatures))] 
        stack = []

        for i, num in enumerate(temperatures):
            if i == 0:
                stack.append([num, i])
                continue
            
            while stack and num > stack[-1][0]:
                x,y = stack.pop()
                output[y] = i-y

            stack.append([num, i])
        
        return output
        