class Solution:
    def getIndexes(self, index: int, m:int) -> tuple[int, int]:
        row     = index // m
        column  = index % m
        return (row, column)

    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if not matrix:
            return False
            
        m = len(matrix[0]) # columns
        n = len(matrix)    # rows
        l = 0
        r = (m * n) - 1

        while l <= r:
            mid = (l + r) // 2

            (m_r, m_c) = self.getIndexes(mid, m)

            if matrix[m_r][m_c] == target:
                return True
            if matrix[m_r][m_c] < target:
                l = mid + 1
            else:
                r = mid - 1

        return False