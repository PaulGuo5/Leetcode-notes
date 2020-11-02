class Solution {
public:
    bool isBipartite(vector<vector<int>>& graph) {
        int size = graph.size();
        queue<int> q;
        vector<int> color(size, 0);
        
        for (int i=0; i<size; i++) {
            if (color[i]) continue;
            color[i] = 1;
            q.push(i);
            while (!q.empty()) {
                int cur = q.front(); q.pop();
                for (auto nei: graph[cur]) {
                    if (!color[nei]) {
                        color[nei] = -color[cur];
                        q.push(nei);
                    }
                    else if (color[nei] == color[cur]) {
                        return false;
                    }
                }
            }
        }
        return true;
    }
};

