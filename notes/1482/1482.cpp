class Solution {
public:
    int minDays(vector<int>& A, int m, int k) {
        int n = A.size(), left = 1, right;
        
        if (m * k > n) return -1;
        right = *max_element(A.begin(), A.end());
        
        while (left <= right) {
            int mid = left+(right-left) / 2, flow = 0, bouq = 0;
            for (int j = 0; j < n; ++j) {
                if (A[j] > mid) {
                    flow = 0;
                } 
                else if (flow+1 >= k) {
                    bouq++;
                    flow = 0;
                }
                else if (flow+1 < k) {
                    flow += 1;
                }
                
            }
            if (bouq < m) {
                left = mid + 1;
            } else {
                right = mid - 1;
            }
        }
        return left;
    }
};
