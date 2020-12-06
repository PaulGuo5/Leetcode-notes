class Solution {
public:
    int kthFactor(int n, int k) {
        int res;
        for(res=1; res<=n; res++) {
            if (n%res == 0) {
                k--;
            }
            if (k==0) return res;
        }
        return k == 0? res: -1;
    }
};
