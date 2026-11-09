class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        res = []

        for i in range(len(intervals)):
            curr = intervals[i]
            currStart = curr[0]
            currEnd = curr[1]
            newStart = newInterval[0]
            newEnd = newInterval[1]
            
            if currEnd < newStart:
                res.append(curr)
                continue
            
            if currStart <= newEnd:
                newInterval = self.merge(curr, newInterval)
                continue
            
            else:
                res.append(newInterval)
                return res + intervals[i:]

        res.append(newInterval)

        return res


    def merge(self, interval_1: List[int], interval_2: List[int]):
        start = min(interval_1[0], interval_2[0])
        end = max(interval_1[1], interval_2[1])
        return [start, end]