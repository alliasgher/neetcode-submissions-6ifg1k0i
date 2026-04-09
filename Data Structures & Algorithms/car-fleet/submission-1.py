class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:

        num = 0
        new = []

        for i in range(len(position)):
            new.append([position[i], speed[i]])

        new.sort(reverse=True)

        stack = []
        for pos, speed in new:
            time = (target - pos) / speed
            if not stack:
                stack.append(time) #no cars forward
                continue
            if time <= stack[-1]:
                continue       #becomes a part of forward fleet
            else:
                stack.append(time)      #new fleet

        return len(stack)



        


        