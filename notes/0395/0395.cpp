class Solution {
public:
    int longestSubstring(string s, int k) {
        return helper(s, k, 0, s.size());
    }
private:
    int helper(string s, int k, int start, int end) {
        vector<int> count(26, 0);
        for (int i=start; i<end; i++) {
            count[s[i]-'a'] ++;
        }
        for (int mid=start; mid < end; mid++) {
            if (count[s[mid]-'a'] >= k) continue;
            int nextMid = mid+1;
            while (nextMid < end && count[s[nextMid]-'a'] < k) nextMid++;
            return max(helper(s, k, start, mid), helper(s, k, nextMid, end));
        }
        return end-start;
    }
};
