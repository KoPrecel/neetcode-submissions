class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        res = []

        for i in range(len(intervals)):
            curr = intervals[i]
            currStart = curr[0]
            currEnd = curr[1]
            newStart = newInterval[0]
            newEnd = newInterval[1]

            if newStart > currEnd:
                res.append(curr)
                continue
            
            elif currStart <= newEnd:
                newInterval = self.merge(curr, newInterval)
                continue

            else:
                res.append(newInterval)
                return res + intervals[i:]

        res.append(newInterval)

        return res


    def merge(self, interval_one: List[List[int]], interval_two: List[List[int]]):
        start = min(interval_one[0], interval_two[0])
        end = max(interval_one[1], interval_two[1])
        return [start, end]