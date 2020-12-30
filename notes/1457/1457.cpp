/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode() : val(0), left(nullptr), right(nullptr) {}
 *     TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
 *     TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
 * };
 */
class Solution {
public:
    int pseudoPalindromicPaths (TreeNode* root) {
        vector<int> path;
        int ans = 0;
        dfs(root, path, ans);
        return ans;
    }
private:
    void dfs(TreeNode* root, vector<int>& path, int& ans) {
        if (!root) return;
        path.push_back(root->val);
        if (!root->left && !root->right && isPalindromic(path)) 
            ans++;
        dfs(root->left, path, ans);
        dfs(root->right, path, ans);
        path.pop_back();
    }
    bool isPalindromic(vector<int>& path) {
        unordered_map<int, int> m;
        for(auto c: path) {
            m[c]++;
        }
        int odd = 0;
        for(auto p: m) {
            if (p.second%2==1) odd++;
            if (odd>1) return false;
        }
        return true;
    }
};
