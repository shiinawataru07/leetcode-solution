class Solution:
    def minArrivalsToDiscard(self, arrivals: List[int], w: int, m: int) -> int:
        res = 0 # 记录总共被丢弃的物品数量
        cnt = collections.defaultdict(int) # 记录在窗口内,每个物品的数量
        for right, x in enumerate(arrivals) :
            left = right - w + 1
            # left记录窗口最左位置
            # right记录窗口最右位置
            if cnt[x] == m : # 如果right将破界则需要丢弃
                arrivals[right] = 0
                '关键改动: 其未来要离开窗口，所以需要修改以免未来离开窗口影响'
                res += 1
            else :
                cnt[x] += 1
            if left < 0 : # 窗口长度不足时continue
                continue
            cnt[arrivals[left]] -= 1 # left退出窗口
        return res
