class Solution {
public:
		string frequencySort(string s) {
		if(s.size()==0) return "";
		unordered_map<int, int> m;
		for (auto c: s) {
		m[c]++;
		}
		sort(s.begin(), s.end(), [&](char a, char b){return m[a] > m[b] || (m[a]==m[b]&&a>b);});
		return s;
		}
    // string frequencySort(string s) {
    //     if(s.size()==0) return "";
    //     unordered_map<char, int> freq;
    //     for (auto c: s) {
    //         freq[c]++;
    //     }
    //     map<int, string> m;
    //     for(auto p: freq) {
    //         char ch = p.first;
    //         int num = p.second;
    //         m[num] += string(num, ch);
    //     }
    //     string res;
    //     for(auto it=m.rbegin();it!=m.rend();it++) {
    //         res += it->second;
    //     }
    //     return res;
    // }
};
