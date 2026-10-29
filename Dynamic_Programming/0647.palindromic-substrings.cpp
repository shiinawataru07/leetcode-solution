class Solution {
public:
    int countSubstrings(string s) {
        int n = s.length();
        vector<vector<bool>> valid(n, vector<bool>(n, false));
        for(int i = 0; i < n; ++i) valid[i][i] = true;
        for(int end = 1; end < n; ++end)
            for(int start = 0; start < end; ++start)
                valid[start][end] = (start + 1 == end || valid[start+1][end-1]) && s[start] == s[end];
        int ans = 0;
        for(int i = 0; i < n; ++i)
            for(int j = 0; j < n; ++j)
                ans += valid[i][j];
        return ans;
    }
};

/*
动态规划来考虑回文子串，记录每个子串是否回文
转移方程为 dp[i][j] = dp[i+1][j-1] && s[i] == s[j]
时间复杂度 O(n^2) 空间复杂度 O(n^2)
可以使用 manacher 优化
*/
