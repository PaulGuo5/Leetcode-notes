class Solution {
public:
    int shortestBridge(vector<vector<int>>& A) {
        queue<pair<int,int>> island;
        int m = A.size(), n = A[0].size();
        int steps = 0;
        const vector<pair<int, int>> dirs = {{0,1},{0,-1},{1,0},{-1,0}};
        
        for (int i=0; i<m; i++) 
            for (int j=0; j<n; j++) {
                if (island.empty()){
                    dfs(A, island, i, j, m ,n);
                }
            }
        while(!island.empty()) {
            int i_size = island.size();
            while (i_size--) {
                auto p = island.front(); island.pop();
                int x = p.first, y = p.second;
                for (auto d: dirs) {
                    int nx = x+d.first, ny = y+d.second;
                    if (0<=nx && nx < m && 0<=ny && ny < n && A[nx][ny] != -1) {
                        if (A[nx][ny] == 1) return steps;
                        A[nx][ny] = -1;
                        island.push({nx, ny});
                    }
                }
            }
            steps++;
        }
        return steps;
    }
private:
    void dfs(vector<vector<int>>& A, queue<pair<int,int>>& ans, int i, int j, int m, int n) {
        if (0<=i && i<m && 0<=j && j<n && A[i][j] == 1) {
            A[i][j] = -1;
            ans.push({i, j});
            dfs(A, ans, i+1, j, m ,n);
            dfs(A, ans, i-1, j, m ,n);
            dfs(A, ans, i, j+1, m ,n);
            dfs(A, ans, i, j-1, m ,n);
        }
    }
};
