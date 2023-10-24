class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []

        for i in asteroids:
            if i > 0:  # if positive moving asteroid, add to list
                stack.append(i)
            else:
                while (
                    stack and stack[-1] > 0 and abs(stack[-1]) < abs(i)
                ):  # while we have a stack, and the top of the stack is positive and the top of the stack is less than the incoming asteroid, remove the asteroid
                    stack.pop()
                if (
                    len(stack) == 0 or stack[-1] < 0
                ):  # if the stack is empty or the top of the stack is negative (asteroid moving left) then append incoming asteroid
                    stack.append(i)
                elif abs(stack[-1]) == abs(
                    i
                ):  # otherwise if the incoming asteroid is of the saeme value as the top of the stack, remove both
                    stack.pop()
        return stack
