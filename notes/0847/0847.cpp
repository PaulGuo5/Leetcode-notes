class Solution {
public:
    int shortestPathLength(vector<vector<int>>& graph) {
        if (graph.empty()) return 0;
        
        queue<pair<int, int>> q;
        // unordered_set<string> visited;
        int size = graph.size();
        vector<vector<int>> visited(size, vector<int>(1 << size));
        const int kAns = (1 << size) - 1;
        
        for (int i=0; i<size; i++) q.push({i, 1<<i});
        int step = 0;
        while (!q.empty()) {
            int q_size = q.size();
            while(q_size--) {
                auto cur_pair = q.front(); q.pop();
                int cur = cur_pair.first;
                int state = cur_pair.second;
                if (state == kAns) return step;
                // string key = to_string(cur)+to_string(state);
                // if (visited.count(key)) continue;
                // visited.insert(key);
                if (visited[cur][state]) continue;
                visited[cur][state] = 1;
                for (int nei: graph[cur]) {
                    q.push({nei, (1 << nei)|state});
                }
            }
            step += 1;
        }
        return -1;
    }
};
