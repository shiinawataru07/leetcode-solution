class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        n = len(nums)
        nums.sort()
        myset = set()
        myset.add(nums[0])
        resset = set()
        res = list()
        for left in range(1, n - 1) :
            for right in range(left + 1, n) :
                if 0 - nums[left] - nums[right] in myset and (0 - nums[left] - nums[right], nums[left], nums[right]) not in resset :
                    res.append([0 - nums[left] - nums[right], nums[left], nums[right]])
                    resset.add((0 - nums[left] - nums[right], nums[left], nums[right]))
            myset.add(nums[left])
        return res
        
  '''
  解析：
  个人解法，空间复杂度略差，主要使用了哈希表与双重循环的指针分别代表第二个数和第三个数
  第一个数计入hashmap
  主要问题在于去重需要应用大量的set(tuple)因此空间开销大
  
  官方题解：
  class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        nums.sort()
        ans = list()
        
        # 枚举 a
        for first in range(n):
            # 需要和上一次枚举的数不相同
            if first > 0 and nums[first] == nums[first - 1]:
                continue
            # c 对应的指针初始指向数组的最右端
            third = n - 1
            target = -nums[first]
            # 枚举 b
            for second in range(first + 1, n):
                # 需要和上一次枚举的数不相同
                if second > first + 1 and nums[second] == nums[second - 1]:
                    continue
                # 需要保证 b 的指针在 c 的指针的左侧
                while second < third and nums[second] + nums[third] > target:
                    third -= 1
                # 如果指针重合，随着 b 后续的增加
                # 就不会有满足 a+b+c=0 并且 b<c 的 c 了，可以退出循环
                if second == third:
                    break
                if nums[second] + nums[third] == target:
                    ans.append([nums[first], nums[second], nums[third]])
        
        return ans

作者：力扣官方题解
链接：https://leetcode.cn/problems/3sum/solutions/284681/san-shu-zhi-he-by-leetcode-solution/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。

使用逻辑进行去重，更为巧妙，节省了集合的开销
此处双指针时间复杂度均为on2
'''
