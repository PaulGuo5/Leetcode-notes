class Solution {
public:
    vector<string> invalidTransactions(vector<string>& transactions) {
        unordered_map<string, vector<vector<string>>> m;
        unordered_set<string> res;
        for(auto t: transactions) {
            stringstream ss(t);
            vector<string> s(4);
            int i=0;
            while(getline(ss, s[i++], ','));
            
            if(stoi(s[2])> 1000) res.insert(t);
            for (auto j: m[s[0]]) {
                if (j[3] != s[3] && abs(stoi(j[1])-stoi(s[1]))<=60) {
                    res.insert(t);
                    res.insert(j[0]+","+j[1]+","+j[2]+","+j[3]);
                }
            }
            m[s[0]].push_back({s[0],s[1],s[2],s[3]});
        }
        vector<string> ans (res.begin(), res.end());
        return ans;
    }
};
