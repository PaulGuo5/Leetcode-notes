class Solution {
public:
    int maxPower(string s) {
        if (s=="") return 0;
        int ans = 0;
        int i = 0;
        while (i<s.size()) {
            int tmp = 0;
            int j = i;
            while (j<s.size() && s[j] == s[i]) {
                tmp++;
                j++;
            }
            ans = max(tmp, ans);
            i = i==j?j:i+1;
        }
        return ans;
    }
};
