class Solution {
public:
    Solution(vector<int>& w) {
        int pre = 0;
        for(auto n: w) {
            pre += n;
            preSum.push_back(pre);
        }
    }
    
    int binarySearch(int n) {
        int lo=0, hi=preSum.size()-1;
        while(lo<=hi) {
            int mid = lo+(hi-lo)/2;
            if (preSum[mid] == n) return mid;
            else if (preSum[mid] < n) lo = mid+1;
            else hi = mid-1;
        }
        return lo;
    }
    
    int pickIndex() {
        int n = random()%preSum.back()+1;
        return binarySearch(n);
    }
private:
    vector<int> preSum;
};

/**
 * Your Solution object will be instantiated and called as such:
 * Solution* obj = new Solution(w);
 * int param_1 = obj->pickIndex();
 */
