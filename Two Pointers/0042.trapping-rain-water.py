class Solution:
    def trap(self, height: List[int]) -> int:
        lmax = [height[0]]
        for i in range(1, len(height)) :
            lmax.append(max(lmax[-1], height[i]))
        rmax = [0] * len(height)
        rmax[-1] = height[-1]
        for i in range(1, len(height)) : 
            rmax[-1 - i] = max(rmax[0 - i], height[-1 - i])
        return sum(min(lmax[i], rmax[i]) - height[i] for i in range(len(height)))

'''
解析：
我的解法本质为动态规划DP
维护每个位置自身以左的最大值与自身以右的最大值，可知雨水必然在这其中
时间复杂度与空间复杂度均为on
事实上，本题也在2025FALL Intro to Computation其中的Timed Assignment 4 第四题出现

而在leetcode官方题解则给出了使用双指针将空间复杂度进一步优化的解法
使用left与right记录指针移动，leftmax与rightmax维护左右最值

class Solution:
    def trap(self, height: List[int]) -> int:
        ans = 0
        left, right = 0, len(height) - 1
        leftMax = rightMax = 0

        while left < right:
            leftMax = max(leftMax, height[left])
            rightMax = max(rightMax, height[right])
            if height[left] < height[right]:
                ans += leftMax - height[left]
                left += 1
            else:
                ans += rightMax - height[right]
                right -= 1
        
        return ans

作者：力扣官方题解
链接：https://leetcode.cn/problems/trapping-rain-water/solutions/692342/jie-yu-shui-by-leetcode-solution-tuvc/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
'''
