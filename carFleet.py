class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        pairs = [(p, s) for p, s in zip(position, speed)]
        pairs.sort(key = lambda x: x[0], reverse = True)
        
        stack = []
        for p, s in pairs:
            if not (stack and ((target - p) / s) <= stack[-1]):
                stack.append((target - p) / s) 
        
        return len(stack)