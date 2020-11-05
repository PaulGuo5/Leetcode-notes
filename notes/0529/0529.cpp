class Solution {
public:
    vector<vector<char>> updateBoard(vector<vector<char>>& board, vector<int>& click) {
        int x = click[0], y = click[1];
        if (board[x][y] == 'M'){
            board[x][y] = 'X';
            return board;
        }
        int m = board.size(), n = board[0].size();
        dfs(board, x, y, m, n);
        return board;
    }
private:
    vector<pair<int, int>> dirs = {{0,1},{0,-1},{1,0},{-1,0},{1,1},{-1,-1},{-1,1},{1,-1}};
    bool check(int x, int y, int m, int n) {
        if (0<=x && x<m && 0<=y && y< n) return true;
        return false;
    }
    void dfs(vector<vector<char>>& board, int x, int y, int m, int n) {
        if (!check(x, y, m, n)) return;
        if (board[x][y] == 'E') {
            int count = 0;
            for (auto d: dirs) {
                int nx = d.first+x, ny = d.second+y;
                if (check(nx, ny, m, n) && board[nx][ny] == 'M') count += 1;
            }
            if (count > 0) {
                board[x][y] = '0'+count;
            }
            else {
                board[x][y] = 'B';
                for (auto d: dirs) {
                    int nx = d.first+x, ny = d.second+y;
                    dfs(board, nx, ny, m, n);
                }
            }
        }
    }
};
