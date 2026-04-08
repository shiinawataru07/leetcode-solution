class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        cnt = 0
        mysum = sum(arr[0:k])
        if mysum >= k * threshold :
            cnt += 1
        left = 0
        right = k
        while right < len(arr) :
            mysum += arr[right]
            right += 1
            mysum -= arr[left]
            left += 1
            if mysum >= k * threshold :
                cnt += 1
        return cnt


'''
解析：
维护定长滑动窗口，每次检测每个窗口是否满足要求并计数
'''
