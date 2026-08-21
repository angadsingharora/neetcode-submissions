class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        #binary search by lowest/highest eleemnt across rows
        #binary search the row itself?
        ROWS = len(matrix)
        COLS = len(matrix[0])

        top = 0
        bot = ROWS - 1

        while top <= bot:
            midRow = (top + bot)//2
            if target > matrix[midRow][-1]:
                top = midRow+1
            elif target < matrix[midRow][0]:
                bot = midRow - 1
            else:
                break
        if not (top<=bot):
            return False
        
        row = (top+bot) // 2
        l = 0
        r = COLS-1
        while l<=r:
            m = (l+r)//2
            if target>matrix[row][m]:
                l = m+1
            elif target<matrix[row][m]:
                r =  m-1
            else:
                return True
        return False
            