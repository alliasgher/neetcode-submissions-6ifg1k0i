class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:

        num = 0
        new = []

        for i in range(len(position)):
            new.append([position[i], speed[i]])

        new.sort(reverse=True)

        stack = []
        for pos, speed in new:
            print(pos, speed)
            time = (target - pos) / speed
            if not stack:
                stack.append(time)
                continue
            if time <= stack[-1]:
                continue
            else:
                stack.append(time)
            print(stack)

        return len(stack)



        


        