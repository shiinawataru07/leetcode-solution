class Solution {
public:
    bool repeatedSubstringPattern(string s) {
        int n = s.length();
        vector<int> pi(n);
        for(int i = 1; i < n; ++i){
            int j = pi[i - 1];
            while(j > 0 && s[i] != s[j]) j = pi[j - 1];
            if(s[i] == s[j]) ++j;
            pi[i] = j;
        }
        int period = n - pi[n - 1];
        return 0 < pi[n - 1] && n % period == 0;
    }
};

///
求出 lps 数组 pi，求字符串周期
时间复杂度 O(n) 空间复杂度 O(n)
///
