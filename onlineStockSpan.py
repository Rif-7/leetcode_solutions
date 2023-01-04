class StockSpanner:

    def __init__(self):
        self.stack = []

    def next(self, price: int) -> int:
        stack = self.stack
        if not stack:
            stack.append((price, 1))
            return 1
        
        span = 1
        if stack[-1][0] <= price:
            span += stack[-1][1]
            i = len(stack) - stack[-1][1] - 1
            while i >= 0:
                if stack[i][0] <= price:
                    span += stack[i][1]
                    i -= stack[i][1]
                else:
                    break
        stack.append((price, span))
        return span


class StockSpanner:

    def __init__(self):
        self.stack = []

    def next(self, price: int) -> int:
        stack = self.stack
        span = 1
        while stack and stack[-1][0] <= price:
            span += stack.pop()[1]
        stack.append((price, span))
        return span
            
