class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        a = [[1 for j in range(i)] for i in range(1,numRows+1)]
        print(a)
        
        for i in range(1,numRows):
            for j in range(1,i):
                print(i,j)
                a[i][j] = a[i-1][j-1] + a[i-1][j]
        return a
                    
                    
                    
                
