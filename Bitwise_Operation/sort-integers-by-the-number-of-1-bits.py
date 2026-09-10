class Solution:
    def sortByBits(self, arr: List[int]) -> List[int]:
        def cnt1(x) -> int:
            cnt = 0
            while x:
                x &= x - 1
                cnt += 1
            return cnt
        return sorted(arr, key=lambda x: (cnt1(x), x))

'''
我们可以使用 x &= x - 1 来去除 x 最右侧的 1，从而统计出 x 的二进制表示中 1 的个数。
然后我们可以使用 Python 的 sorted 函数对数组进行排序，排序的关键字是一个元组，元组的第一个元素是 1 的个数，
第二个元素是数字本身，这样就可以实现按照 1 的个数排序，如果 1 的个数相同，则按照数字本身排序。

时间复杂度O(nlogn) 空间复杂度O(n)
'''
