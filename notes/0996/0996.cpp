class Solution {
public:
    int numSquarefulPerms(vector<int>& A) {
        sort(A.begin(), A.end());
        vector<int> path;
        vector<int> visited(A.size(), 0);
        int ans = 0;
            
        dfs(A, ans, path, visited);
        return ans;
    }
private:
    void dfs(vector<int>& A, int& ans, vector<int>& path, vector<int>& visited) {
        if (path.size() == A.size()) {
            ans += 1;
            return;
        }
        for (int i=0; i<A.size(); i++) {
            if (i>0 && A[i] == A[i-1] && !visited[i-1]) continue;
            if (!visited[i] && (path.empty() || (!path.empty() && helper(path.back()+A[i])))) {
                visited[i] = 1;
                path.push_back(A[i]);
                dfs(A, ans, path, visited);
                visited[i] = 0;
                path.pop_back();
            }
        }
    }
    bool helper(int n) {
        int sq = sqrt(n);
        return n == sq*sq;
    }
};
