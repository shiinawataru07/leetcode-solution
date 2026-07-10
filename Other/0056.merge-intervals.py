class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        sorted_arr = sorted(intervals, key=lambda lst: lst[0])
        ans = list()
        l, r = sorted_arr[0]
        for start, end in sorted_arr[1:]:
            if r < start:
                ans.append([l, r])
                l, r = start, end
            else:
                r = max(r, end)
        ans.append([l, r])
        return ans


'''
将区间按起始排序，遍历一遍，发现能合并就合并
'''
