class UndergroundSystem {
public:
    UndergroundSystem() {
        
    }
    
    void checkIn(int id, string stationName, int t) {
        m[id] = {stationName, t};
    }
    
    void checkOut(int id, string stationName, int t) {
        auto &[startSta, startTime] = m[id];
        auto &[total, cnt] = stats[startSta+">"+stationName];
        total += t - startTime;
        cnt += 1;
    }
    
    double getAverageTime(string startStation, string endStation) {
        auto [total, cnt] = stats[startStation+">"+endStation];
        return (double)total/cnt;
    }
private:
    unordered_map<int, pair<string, int>> m;
    unordered_map<string, pair<int, int>>stats;
};

/**
 * Your UndergroundSystem object will be instantiated and called as such:
 * UndergroundSystem* obj = new UndergroundSystem();
 * obj->checkIn(id,stationName,t);
 * obj->checkOut(id,stationName,t);
 * double param_3 = obj->getAverageTime(startStation,endStation);
 */
