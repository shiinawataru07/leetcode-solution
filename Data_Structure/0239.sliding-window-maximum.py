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
单调队列模板题，维护一个单调递减的队列，并且控制队列一定在窗口内即可
'''
