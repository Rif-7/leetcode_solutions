class Solution:
    def asteroidCollision(self, asteroids):
        stack = []
        for a in asteroids:
            if stack and stack[-1] > 0 and a < 0:
                flag = True
                while stack:
                    if stack[-1] > 0 and a < 0:
                        if abs(a) < abs(stack[-1]):
                            flag = False
                            break
                        elif abs(stack[-1]) < abs(a):
                            stack.pop()
                        else:
                            flag = False
                            stack.pop()
                            break
                    
                    else:
                        break
                if flag:
                    stack.append(a)
            
            else:
                stack.append(a)
        return stack
        