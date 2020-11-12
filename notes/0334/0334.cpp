class Solution {
public:
    bool increasingTriplet(vector<int>& nums) {
        int size = nums.size();
        if (size < 3) return false;
        int c1 = INT_MAX, c2 = INT_MAX;
        for (auto n: nums) {
            if (n <= c1) {
                c1 = n;
            }
            else if (n <= c2) {
                c2 = n;
            }
            else {
                return true;
            }
        }
        return false;
    }
};
