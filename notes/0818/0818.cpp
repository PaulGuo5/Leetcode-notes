class Solution {
public:
    int racecar(int target) {
        unordered_set<string> visited;
        queue<pair<int, int>> q;
        int steps = 0;
        
        q.push({0, 1});
        visited.insert("0_1");
        visited.insert("0_-1");
        
        while (!q.empty()) {
            int q_size = q.size();
            while(q_size--) {
                auto p = q.front();q.pop();
                int pos = p.first, speed = p.second;
                
                // A
                int pos1 = pos+speed;
                int speed1 = speed*2;
                if (pos1 == target) return steps+1;
                if (pos1>0 && pos1 < 2*target) q.push({pos1, speed1});
                
                //B
                int pos2 = pos;
                int speed2 = speed>0? -1: 1;
                string tmp = to_string(pos2)+"_"+to_string(speed2);
                if (!visited.count(tmp)) {
                    visited.insert(tmp);
                    q.push({pos2, speed2});
                }
            }
            steps++;
        }
        return -1;
    }
};
