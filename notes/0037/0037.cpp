class Solution {
public:
    void solveSudoku(vector<vector<char>>& board) {
        vector<vector<int>> row(9, vector<int>(10));
        vector<vector<int>> col(9, vector<int>(10));
        vector<vector<int>> box(9, vector<int>(10));
        
        for (int i=0; i<9; i++) 
            for (int j=0; j<9; j++) {
                if (board[i][j] != '.') {
                    row[i][board[i][j]-'0'] = 1;
                    col[j][board[i][j]-'0'] = 1;
                    box[3*(i/3)+j/3][board[i][j]-'0'] = 1;
                }
            }
        
        dfs(board, 0, 0, row, col, box);
    }
private:
    
    bool dfs(vector<vector<char>>& board, int i, int j, vector<vector<int>>& row, vector<vector<int>>& col, vector<vector<int>>& box) {
        if (i == 9) return true;
        
        int nxt_j = (j+1) % 9;
        int nxt_i = (nxt_j == 0) ? (i + 1) : i;
        
        if (board[i][j] != '.') return dfs(board, nxt_i, nxt_j, row, col, box);
        
        for (int n=1; n<10; n++){
            if (!row[i][n] && !col[j][n] && !box[i/3*3+j/3][n]) {
                row[i][n] = 1;
                col[j][n] = 1;
                box[i/3*3+j/3][n] = 1;
                board[i][j] = '0'+n;
                if (dfs(board, nxt_i, nxt_j, row, col, box)) return true;
                board[i][j] = '.';
                row[i][n] = 0;
                col[j][n] = 0;
                box[i/3*3+j/3][n] = 0;
            }
        }
        return false;
    }
};
