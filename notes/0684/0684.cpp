// class Solution {
// public:
//     vector<int> findRedundantConnection(vector<vector<int>>& edges) {
//         const int N = edges.size();
//         vector<int> tree(N+1, -1);
        
//         for (auto p: edges) {
//             int root_a = findRoot(p[0], tree);
//             int root_b = findRoot(p[1], tree);
//             if (root_a == root_b) return p;
//             tree[root_b] = root_a;
//         }
//         return {};
//     }
// private:
//     int findRoot(int x, vector<int>& tree) {
//         if (tree[x]==-1) return x;
//         int root = findRoot(tree[x], tree);
//         tree[x] = root;
//         return root;
//     }
// };
class Solution {
public:
    vector<int> findRedundantConnection(vector<vector<int>>& edges) {
        unordered_map<int, unordered_set<int>> m;
        for (auto e: edges) {
            if (m.count(e[0]) && m.count(e[1])) {
                if (bfs(e[0], e[1], m)) return e;
            }
            m[e[0]].insert(e[1]);
            m[e[1]].insert(e[0]);
        }
        return {};
    }
private:
    bool bfs(int a, int b, unordered_map<int, unordered_set<int>>& m) {
        queue<int> q;
        unordered_set<int> visited;
        
        q.push(a);
        visited.insert(a);
        while (!q.empty()) {
            int cur = q.front(); q.pop();
            if (cur == b) return true;
            for (auto nei: m[cur]) {
                if (!visited.count(nei)) {
                    visited.insert(nei);
                    q.push(nei);
                }
            }
        }
        return false;
    }
};
