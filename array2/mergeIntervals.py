# tc = nlogn + n
# sc = n

class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        
#         sorting intervals acc to index 0
        intervals.sort(key = lambda x : x[0])
        
        # print(intervals)
        
        check = intervals[0]
        res = []
        for pair in intervals:
            if pair[0] <= check[1]:
                check[1] = max(check[1],pair[1])
            else:
                res.append(check)
                check = pair
        res.append(check)
        return res
