class Solution {
public:
    vector<int> pathInZigZagTree(int label) {
        int level = 0;
        int num = label;
        
        while (num > 0) {
            level++;
            num /= 2;
        }
        vector<int> ans;
        while (label > 0) {
            ans.push_back(label);
            int max = pow(2, level)-1;
            int min = pow(2, level-1);
            label = (max+min-label)/2;
            level--;
        }
        vector<int> res(ans.rbegin(), ans.rend());
        return res;
        
    }
};
