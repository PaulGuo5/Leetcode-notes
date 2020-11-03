class Solution {
public:
    int numTeams(vector<int>& rating) {
        unordered_map<int, int> greater;
        unordered_map<int, int> less;
        int size = rating.size();
        int ans = 0;
        
        for (int i=0;i<size-1;i++)
            for (int j=i+1;j<size;j++) {
                if (rating[i] < rating[j]) {
                    greater[i] += 1;
                }
                else {
                    less[i] += 1;
                }
            }
        
        for (int i=0;i<size-2;i++)
            for (int j=i+1;j<size;j++) {
                if (rating[i] < rating[j]) {
                    ans += greater[j];
                }
                else {
                    ans += less[j];
                }
            }
        return ans;
    }
};
