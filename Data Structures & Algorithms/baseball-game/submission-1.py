class Solution:
    def calPoints(self, operations: List[str]) -> int:
        record = []
        for op in operations:
            if op.isnumeric():
                record.append(int(op))
            elif op[0] == '-':
                record.append(int(op))
            elif op == '+':
                # add previous two
                first_val = record[-1]
                second_val = record[-2]

                third_val = first_val + second_val
                record.append(third_val)
            elif op == 'D':
                #double previous score
                first_val = record[-1]
                second_val = 2 * first_val
                record.append(second_val)

            elif op == 'C':
                # append score
                record.pop()

        return sum(record)