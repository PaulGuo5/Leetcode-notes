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
    int maxAncestorDiff(TreeNode* root) {
        return dfs1(root, root->val, root->val);
    }
private:
    int dfs1(TreeNode* root, int max_, int min_) {
        if (!root) return max_-min_;
        
        int tmp_max = max(max_, root->val);
        int tmp_min = min(min_, root->val);
        int left = dfs1(root->left, tmp_max, tmp_min);
        int right = dfs1(root->right, tmp_max, tmp_min);
        return max(left, right);
    }
};
