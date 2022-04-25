# tc = O(n*2)
# sc = O(1)

class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        
        n = len(matrix)
#    transpose the matrix
        
        for i in range(n):
            for j in range(i):
                matrix[i][j],matrix[j][i] = matrix[j][i],matrix[i][j]
                
        print(matrix)
        
    


#    reverse every row      
        for row in matrix:
            i = 0
            j = n-1
            while i < j:
                row[i],row[j] = row[j],row[i]
                i += 1
                j -= 1
        
        return matrix
