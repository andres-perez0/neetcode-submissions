class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n = len(temperatures)
        temperature_list = [0] * n
        stk = []

        for i in range(n):
            if len(stk) == 0:
                stk.append((temperatures[i], i))
                continue

            while len(stk) > 0 and stk[-1][0] < temperatures[i]:
                top = stk.pop() # (val, index)
                if top[0] < temperatures[i]:
                    # curr top val < curr temp 
                    temperature_list[top[1]] = i - top[1]
                else:
                    stk.append(top)

            stk.append((temperatures[i], i))

        return temperature_list