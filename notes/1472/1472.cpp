class BrowserHistory {
public:
    BrowserHistory(string homepage):history(5000,"") {
        cur = top = 0;
        history[cur] = homepage;
    }
    
    void visit(string url) {
        cur++;
        top = cur;
        history[top] = url;
    }
    
    string back(int steps) {
        cur = max(0, cur-steps);
        return history[cur];
    }
    
    string forward(int steps) {
        cur = min(top, cur+steps);
        return history[cur];
    }
private:
    vector<string> history; //string history[5000];
    int cur, top;
};

/**
 * Your BrowserHistory object will be instantiated and called as such:
 * BrowserHistory* obj = new BrowserHistory(homepage);
 * obj->visit(url);
 * string param_2 = obj->back(steps);
 * string param_3 = obj->forward(steps);
 */
