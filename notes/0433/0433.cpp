class Solution {
public:
    int minMutation(string start, string end, vector<string>& bank) {
        queue<string> q;
        int size = bank.size();
        unordered_set<string> s(bank.begin(), bank.end());
        unordered_set<string> visited;
        const string gen[4] = {"A","C","G","T"};
        
        q.push(start);
        int steps = 0;
        while (!q.empty() && visited.size() < size) {
            steps += 1;
            int q_size = q.size();
            while (q_size--) {
                string cur = q.front();q.pop();
                for (int i=0; i<cur.size(); i++) {
                    for (string j: gen) {
                        if (cur.substr(i, 1)==j) continue;
                        string tmp = cur.substr(0, i)+j+cur.substr(i+1);
                        if (visited.count(tmp) || !s.count(tmp)) {
                            continue;
                        }
                        if (tmp == end) return steps;
                        visited.insert(tmp);
                        q.push(tmp);
                    }
                }
                
            }
        }
        return -1;
    }
};
