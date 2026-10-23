class Solution:
    def permute(self, nums: list[int]) -> list[list[int]]:
        res = []
        n = len(nums)
        stk = [([], [False] * n)]
        while stk:
            path, used = stk.pop()
            if len(path) == n:
                res.append(path)
                continue
            for i in range(n-1, -1, -1):
                if not used[i]:
                    new_used = used[:]
                    new_used[i] = True
                    stk.append((path + [nums[i]], new_used))
        return res

'''
用一个栈来模拟进行回溯，使用 used 数组来标记哪些元素已经被使用过，递归地生成所有排列。
'''
