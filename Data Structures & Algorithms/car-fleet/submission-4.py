class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        pos_and_spe = sorted(zip(position, speed), key=lambda x: -x[0])

        # print(pos_and_spe)
        step_stk = []
        for i, n in enumerate(position):
            steps = ((target-pos_and_spe[i][0]) / pos_and_spe[i][1])
            # print(steps)
            if i == 0: 
                # print("first item")
                step_stk.append(steps)
                continue
            
            top = step_stk[-1]
            # print(f"top: {top} <= steps: {steps}")
            if top >= steps:  
                # print("steps caught up")    
                continue
            else:
                step_stk.append(steps)
            # print(step_stk)
            # so if a car can only form a fleet with the ahead of it,
            # then we need to check if our current car is fast enough to 
            # catch up to the cars ahead
            # so this is whether the number of steps is less the item in the front of it
            
            # so for (5, 1) to not be caught up 
            # if would need to be place 
            # t.0 ( 3,3) t.1 ( 6,3) t.2 ( 9,3) t.3 (12,3)
            # t.0 (10,1) t.1 (11,1) t.2 (12,1)    


        return len(step_stk)