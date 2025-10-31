class Solution:
    def carFleet(self, target: int, position: list[int], speed: list[int]) -> int:
        cars = sorted(zip(position, speed), reverse=True)
        stack = []

        for (position, speed) in cars:
            arrival = (target - position) / float(speed)

            if stack and arrival <= stack[-1]:
                continue
            else:
                stack.append(arrival)

        return len(stack)    

