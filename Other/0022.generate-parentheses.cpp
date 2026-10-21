class Solution {
public:
    vector<string> generateParenthesis(int n) {
        vector<string> ans;
        stack<string> stk;
        stk.push("(");
        while(!stk.empty()) {
            string cur = stk.top(); stk.pop();
            int cnt = 0;
            for(char c : cur) if(c == '(') ++cnt;
            if(cnt == n){
                cur += ')';
                if(cur.length() == n << 1) ans.push_back(cur);
                else stk.push(cur);
            }else{
                if(cur.length() == cnt << 1) stk.push(cur + '(');
                else{
                    stk.push(cur + '(');
                    stk.push(cur + ')');
                }
            }
        }
        return ans;
    }
};

'''
用一个栈 stk 来进行回溯生成所有合法括号序列即可
'''
