class Solution {
public:
    int minLength(string s) {
        int pos = 0;
        for(char ch : s){
            if(pos > 0 && ((s[pos-1]=='A' && ch == 'B') || (s[pos-1]=='C' && ch == 'D'))) {
                --pos;
            }else {
                s[pos++] = ch;
            }
        }
        return pos;
    }
};

'''
用一个栈指针 pos 来维护目前存放字符的栈，每当符合删除条件时就弹出，否则就压入
时间复杂度 O(n) 空间复杂度 O(1)
'''
