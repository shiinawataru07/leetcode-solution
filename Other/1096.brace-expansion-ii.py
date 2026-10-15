class Solution:
    def braceExpansionII(self, expression: str) -> list[str]:
        def parse(left: int, right: int) -> set[str]:
            res = set()
            cur = {""}
            i = left
            while i <= right:
                if expression[i] == '{':
                    left_cnt = 1
                    right_cnt = 0
                    pos = i
                    i += 1
                    while left_cnt > right_cnt:
                        if expression[i] == '{':
                            left_cnt += 1
                        if expression[i] == '}':
                            right_cnt += 1
                        i += 1
                    part = parse(pos+1, i-2)
                    cur = set(a + b for a in cur for b in part)
                elif expression[i] == ',':
                    res |= cur
                    cur = {""}
                    i += 1
                else:
                    cur = set(a + expression[i] for a in cur)
                    i += 1
            return res | cur
        return sorted(parse(0, len(expression)-1))

'''
使用递归解析花括号表达式，通过集合的**并集和笛卡尔积（字符串拼接）**实现展开。
定义 parse(left, right)，返回表达式区间 [left, right] 展开后得到的字符串集合。
维护两个集合：
- res：已经完成的并集结果，初始化为空集合。
- cur：当前连续表达式的拼接结果，初始化为 {""}，作为字符串拼接的单位元。
从左到右遍历表达式，根据当前字符执行不同操作：
1. 遇到 {：通过计数匹配对应的 }，递归解析花括号内部的表达式，得到集合 part，然后将 cur 与 part 做笛卡尔积并拼接字符串。
2. 遇到 ,：说明当前拼接项结束，将 cur 并入 res，再将 cur 重置为 {""}。
3. 遇到普通字母：将该字母拼接到 cur 中的每个字符串后面。
遍历结束后，返回 res | cur，最后将结果排序。

'''
