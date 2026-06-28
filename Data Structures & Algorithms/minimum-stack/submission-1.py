class MinStack:

    def __init__(self):
        self.stk = []
        self.min_val = None
        
    def push(self, val: int) -> None:
        if self.min_val == None:
            self.min_val = val
        else:
            if val < self.min_val:
                self.min_val = val

        self.stk.append(val)

    def pop(self) -> None:
        if len(self.stk) == 1:
            self.min_val = None

        popped_val = self.stk.pop()
        if popped_val == self.min_val:
            self.min_val = min(self.stk)

    def top(self) -> int:
        return self.stk[-1]

    def getMin(self) -> int:
        return self.min_val
