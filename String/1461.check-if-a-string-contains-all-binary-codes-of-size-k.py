class Solution:
    def hasAllCodes(self, s: str, k: int) -> bool:
        st = set()
        n = len(s)
        cnt = 0
        for i in range(0, n-k+1):
            substr = s[i: i+k]
            if substr not in st:
                cnt += 1
                st.add(substr)
        return cnt == pow(2, k)

'''
暴力枚举，考察所有长度为 k 的字串，最后看总数是否为 2^k

时间复杂度 O(nk) 空间复杂度 O(nk)
'''
