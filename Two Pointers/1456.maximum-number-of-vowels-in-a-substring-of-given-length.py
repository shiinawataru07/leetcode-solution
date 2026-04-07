class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        left = 0
        right = k
        st = set('aeiou')
        cnt = 0
        for i in range(left, right) :
            if s[i] in st : 
                cnt += 1
        res = cnt
        while right < len(s) :
            if s[right] in st : 
                cnt += 1
            right += 1
            if s[left] in st : cnt -= 1
            left += 1
            res = max(res, cnt)
        return res


'''
解析：
使用滑动窗口来判断每个窗口内的元音数目
只需处理进窗口与出窗口的是否为元音即可
'''
