class Solution {
public:
    vector<string> wordBreak(string s, vector<string>& wordDict) {
        int size = s.size();
        unordered_set<string> words(wordDict.begin(), wordDict.end());
        vector<int> dp(size+1, 0);
        dp[0] = 1;
        unordered_map<int, unordered_set<int>> graph;
        for(int i=1; i<=size; i++) {
            for (int j=0; j<i; j++) {
                if (dp[j] && words.count(s.substr(j,i-j))) {
                    dp[i] = 1;
                    graph[i].insert(j);
                }
            }
        }
        
        string path = "";
        dfs(size, path, s, graph);
        return ans;
    }
private:
    vector<string> ans;
    void dfs(int pos, string path, const string& s, unordered_map<int, unordered_set<int>>& graph) {
        if (pos == 0) ans.push_back(path);
        for (int i: graph[pos]) {
            string tmp = path;
            path = s.substr(i, pos-i);
            if (!tmp.empty()) path = path + " " + tmp;
            dfs(i, path, s, graph);
            path = tmp;
        }
    }
};
