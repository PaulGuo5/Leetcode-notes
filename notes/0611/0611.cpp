class Solution {
public:
    int triangleNumber(vector<int>& nums) {
        int size = nums.size();
        if (size < 3) return 0;
        sort(nums.rbegin(), nums.rend());
        int ans = 0;
        
        for(int c=0; c<size-2; c++) {
            int b = c+1;
            int a = size-1;
            while(b < a) {
                if (nums[a]+nums[b] > nums[c]) {
                    ans += a-b;
                    b++;
                }
                else a--;
            }
        }
        return ans;
    }
};
