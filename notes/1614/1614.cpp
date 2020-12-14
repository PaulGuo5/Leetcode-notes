class Solution {
public:
    int maxDepth(string s) {
        int res = 0;
        int depth = 0;
        for (char c: s) {
            if (c == '(') {
                depth++;
                res = max(res, depth);
            }
            else if (c==')') {
                depth--;
            }
        }
        return res;
    }
};
