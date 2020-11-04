class Solution {
public:
    vector<vector<int>> highFive(vector<vector<int>>& items) {
        unordered_map <int, vector<int>> m;
        vector<vector<int>> ans;
        for (auto p: items) {
            int id = p[0], score = p[1];
            m[id].push_back(score);
        }
        
        for(auto p: m) {
            int id = p.first;
            vector<int> scores = p.second;
            sort(scores.begin(), scores.end(), greater<int>());
            vector<int> tmp(scores.begin(), scores.begin()+5);
            int sum = accumulate(tmp.begin(), tmp.end(), 0);
            int avg = sum/tmp.size();
            ans.push_back({id, avg});
        }
        sort(ans.begin(), ans.end());
        return ans;
    }
};
