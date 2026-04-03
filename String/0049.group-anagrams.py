class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        d = defaultdict(list)
        for s in strs :
            cnt = [0] * 26
            for ch in s :
                cnt[ord(ch) - ord("a")] += 1
            d[tuple(cnt)].append(s)
        return list(d.values())

'''
解析：使用计数法创建哈希，时间复杂度优于排序
'''
