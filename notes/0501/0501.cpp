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
    vector<int> findMode(TreeNode* root) {
        inorder(root);
        return ans;
    }
private:
    int cnt = 0;
    int max_cnt = 0;
    vector<int> ans;
    int pre = -1;
    void inorder(TreeNode* root) {
        if(!root) return;
        inorder(root->left);
        if (root->val == pre) {
            cnt += 1;
        }
        else {
            cnt = 0;
            pre = root->val;
        }
        if (cnt > max_cnt) {
            max_cnt = cnt;
            ans.clear();
        }
        if (max_cnt == cnt) {
            ans.push_back(root->val);
        }
        inorder(root->right);
    }
};
