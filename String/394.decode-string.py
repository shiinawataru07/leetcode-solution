class Solution:
    def decodeString(self, s: str) -> str:
        n = len(s)
        i = 0
        k = 0
        res = ""
        while i < n:
            if '0' <= s[i] <= '9':
                k = k * 10 + int(s[i])
            elif s[i] == '[':
                depth = 1
                i += 1
                pos = i
                while depth > 0:
                    if s[i] == '[':
                        depth += 1
                    if s[i] == ']':
                        depth -= 1
                    i += 1
                res = res + k * self.decodeString(s[pos: i-1])
                k = 0
                continue
            elif 'a' <= s[i] <= 'z':
                res += s[i]
            i += 1
        return res


'''
遍历字符串，遇到数字则累积倍数 k；
遇到 [ 时通过计数 depth 线性扫描找到匹配的 ]，截取括号内子串递归解码，将结果重复 k 次拼接到答案；
遇到字母直接拼接。每处理完一个括号组后重置 k，利用 continue 跳过末尾的 i+=1 避免越界。
'''
