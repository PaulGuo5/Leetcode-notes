class Leaderboard {
public:
    Leaderboard() {
        
    }
    
    void addScore(int playerId, int score) {
        if (s.count({m[playerId], playerId})) s.erase({m[playerId], playerId});
        m[playerId] += score;
        s.insert({m[playerId], playerId});
    }
    
    int top(int K) {
        int res = 0;
        for (auto it = s.rbegin(); it != s.rend() && K-->0; it++) {
            res += it->first;
        }
        return res;
    }
    
    void reset(int playerId) {
        s.erase({m[playerId], playerId});
        m[playerId] = 0;
    }
private:
    set<pair<int, int>> s;
    unordered_map<int, int> m;
};

/**
 * Your Leaderboard object will be instantiated and called as such:
 * Leaderboard* obj = new Leaderboard();
 * obj->addScore(playerId,score);
 * int param_2 = obj->top(K);
 * obj->reset(playerId);
 */
