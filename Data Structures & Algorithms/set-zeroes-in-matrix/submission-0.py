class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        R,C=len(matrix),len(matrix[0])
        rowZero=False
        for i in range(R):
            for j in range(C):
                if matrix[i][j]==0:
                    matrix[0][j]=0
                    if i>0:
                        matrix[i][0]=0
                    else:
                        rowZero=True
        for r in range(1,R):
            for c in range(1,C):
                if matrix[r][0]==0 or matrix[0][c]==0:
                    matrix[r][c]=0

        if matrix[0][0]==0:
            for r in range(R):
                matrix[r][0]=0
        if rowZero:
            for c in range(C):
                matrix[0][c]=0    
        