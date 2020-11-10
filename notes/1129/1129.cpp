class Solution {
public:
    vector<int> shortestAlternatingPaths(int n, vector<vector<int>>& red_edges, vector<vector<int>>& blue_edges) {
        unordered_map<int, unordered_map<int,int>> r_graph;
        unordered_map<int, unordered_map<int,int>> b_graph;
        for(auto p: red_edges) {
            r_graph[p[0]][p[1]] = 1;
        }
        for(auto p: blue_edges) {
            b_graph[p[0]][p[1]] = 1;
        }
        
        queue<pair<int,int>> q;
        q.push({0, 1});
        q.push({0, -1});
        vector<int> ans(n, -1);
        unordered_set<int> seen_r;
        unordered_set<int> seen_b;
        seen_r.insert(0);
        seen_b.insert(0);
        int steps = 0;
        while(!q.empty()) {
            int q_size = q.size();
            while(q_size--) {
                auto p = q.front(); q.pop();
                int cur = p.first, color = p.second;
                ans[cur] = ans[cur]>=0 ? min(ans[cur], steps): steps;
                auto& graph = color>0 ? r_graph: b_graph;
                auto& seen = color>0 ? seen_r : seen_b;
                for (auto nxt : graph[cur]) {
                    if (seen.count(nxt.first)) continue;
                    seen.insert(nxt.first);
                    q.push({nxt.first, -1*color});
                }
            }
            steps++;
        }
        return ans;
    }
};
