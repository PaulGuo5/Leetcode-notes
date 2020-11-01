class Solution {
public:
    vector<double> calcEquation(vector<vector<string>>& equations, vector<double>& values, vector<vector<string>>& queries) {
        unordered_map<string, unordered_map<string, double>> graph;
        const int size = equations.size();
        vector<double> ans;
        
        for (int i=0; i<size; i++) {
            string first = equations[i][0];
            string second = equations[i][1];
            graph[first][second] = 1.0*values[i];
            graph[second][first] = 1.0/values[i];
        }
        
        for (auto p: queries) {
            if (!graph.count(p[0]) || !graph.count(p[1])) {
                ans.push_back(-1.0);
                continue;
            }
            unordered_set<string> visited;
            ans.push_back(dfs(graph, visited, p[0], p[1]));
        }
        return ans;
    }
private:
    double dfs(unordered_map<string, unordered_map<string, double>>& graph, unordered_set<string>& visited, string i, string j) {
        if (i==j) return 1.0;
        for (auto p: graph[i]) {
            string tmp = p.first;
            double tmp_val = p.second;
            if (visited.count(tmp)) continue;
            visited.insert(tmp);
            double val = dfs(graph, visited, tmp, j);
            if (val != -1.0) return val*tmp_val;
        }
        return -1.0;
    } 
};
