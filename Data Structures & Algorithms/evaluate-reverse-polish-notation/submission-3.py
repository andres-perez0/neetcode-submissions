class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stk = []

        for n in tokens:
            if n.isnumeric():
                stk.append(int(n))
            elif n[0] == "-" and len(n) > 1:
                stk.append(int(n))
            elif n == "+":
                val_1 = stk.pop()
                val_2 = stk.pop()
                stk.append(val_1 + val_2)
            elif n == "-":
                val_1 = stk.pop()
                val_2 = stk.pop()
                stk.append(val_2 - val_1)
            elif n == "*":
                val_1 = stk.pop()
                val_2 = stk.pop()
                stk.append(val_1 * val_2)
            elif n == "/":
                val_1 = stk.pop()
                val_2 = stk.pop()
                stk.append(int(val_2 / val_1))

        return stk.pop()