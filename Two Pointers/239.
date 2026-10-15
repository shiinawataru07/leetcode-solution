class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        q = collections.deque()
        ans = list()
        for idx in range(len(nums)):
            while q and nums[idx] >= nums[q[-1]]:
                q.pop()
            q.append(idx)
            if idx - q[0] >= k:
                q.popleft()
            if idx >= k - 1:
                ans.append(nums[q[0]])
        return ans



'''
单调队列模板题，用单调队列维护窗口内的值即可

时间复杂度 O(n) 空间复杂度 O(min(U, k)) 其中 U 为 nums 中不同的元素个数
'''
