class Solution {
public:
    vector<int> anagramMappings(vector<int>& A, vector<int>& B) {
        vector<int> ans;
        unordered_map<int, int> m;
        for(int i=0; i<B.size(); i++) {
            m[B[i]] = i;
        }
        for(auto n: A) {
            ans.push_back(m[n]);
        }
        return ans;
    }
};
