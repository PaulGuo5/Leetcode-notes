class Solution {
public:
    vector<int> maxSlidingWindow(vector<int>& nums, int k) {
        deque<int> deq;
        vector<int> ans;
        int size = nums.size();
        
        for (int i=0; i<size; i++) {
            while(!deq.empty() && nums[deq.back()] <= nums[i]) deq.pop_back();
            deq.push_back(i);
            if (i-k+1 >= 0) ans.push_back(nums[deq.front()]);
            if (i-k+1 >= deq.front()) deq.pop_front();
        }
        return ans;
    }
};
