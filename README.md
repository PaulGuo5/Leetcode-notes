LeetCode solutions in Python3.
========


Table of Contents
=================

   * [LeetCode](#leetcode)
      * [Bit Manipulation](#bit-manipulation)
      * [Array](#array)
      * [Linked List](#linked-List)
      * [Stack](#stack)
      * [Recursion](#recursion)
      * [Queue](#queue)
      * [Binary Tree](#binary-tree)
      * [Hash Table](#hash-table)
      * [Sort](#sort)
      * [Heap](#heap)
      * [Math](#math)
      * [Binary Search](#binary-search)
      * [Binary Search Tree](#binary-search-tree)
      * [N-ary Tree](#n-ary-tree)
      * [Graph](#graph)
      * [BackTracking](#backtracking)
      * [Dynamic Programming](#dynamic-programming)


## Leetcode
[Leetcode website](https://leetcode.com/)      

## Complexity
[Time & Space Complexity](./classical_algorithm/TimeSpaceCpmlexity.md)





## Bit Manipulation
|NO.|Title|Solution|Note|Difficulty|Time|Space|Tag|
|---|-----|--------|----|----------|----|-----|---|
|No.136|[Single Number](https://leetcode.com/problems/single-number/)|[Solution](./0136/0136.py)|[Note](./0136/note0136.md)|Easy|O(n)|O(1)|Bit Manipulation|





## Array
|NO.|Title|Solution|Note|Difficulty|Time|Space|Tag|
|---|-----|--------|----|----------|----|-----|---|
|No.42|[Trapping Rain Water](https://leetcode.com/problems/trapping-rain-water/)|[Solution](./0042/0042.py)|[Note](./0042/note0042.md)|Hard|O(m)|O(1)|2 pointers|
|No.289|[Game of Life](https://leetcode.com/problems/game-of-life/)|[Solution](./0289/0289.py)|[Note](./0289/note0289.md)|Medium|O(nm)|O(1)|Bit|
|No.11|[Container With Most Water](https://leetcode.com/problems/container-with-most-water/)|[Solution](./0011/0011.py)|[Note](./0011/note0011.md)|Medium|O(n)|O(1)|2 pointers|
|No.560|[Subarray Sum Equals K](https://leetcode.com/problems/subarray-sum-equals-k/)|[Solution](./0560/0560.py)|[Note](./0560/note0560.md)|Medium|O(n)|O(n)|---|
|No.54|[Spiral Matrix](https://leetcode.com/problems/spiral-matrix/)|[Solution](./0054/0054.py)|[Note](./0054/note0054.md)|Medium|O(n)|O(n)|---|
|No.380|[Insert Delete GetRandom O(1)](https://leetcode.com/problems/insert-delete-getrandom-o1/)|[Solution](./0380/0380.py)|[Note](./0380/note0380.md)|Medium|O(n)|O(n)|---|
|No.79|[Word Search](https://leetcode.com/problems/word-search/)|[Solution](./0079/0079.py)|[Note](./0079/note0079.md)|Medium|O(nm)|O(nm)|---|
|No.78|[Subsets](https://leetcode.com/problems/subsets/)|[Solution](./0078/0078.py)|[Note](./0078/note0078.md)|Medium|O(2^n)|O(2^n)|iterative or dfs|
|No.90|[Subsets II](https://leetcode.com/problems/subsets-ii/)|[Solution](./0090/0090.py)|[Note](./0090/note0090.md)|Medium|O(2^n)|O(2^n)|iterative or dfs|
|No.1007|[Minimum Domino Rotations For Equal Row](https://leetcode.com/problems/minimum-domino-rotations-for-equal-row/)|[Solution](./1007/1007.py)|[Note](./1007/note1007.md)|Medium|O(n)|O(1)|---|

## String
|NO.|Title|Solution|Note|Difficulty|Time|Space|Tag|
|---|-----|--------|----|----------|----|-----|---|
|No.409|[Longest Palindrome](https://leetcode.com/problems/longest-palindrome/)|[Solution](./0409/0409.py)|[Note](./0409/note0409.md)|Easy|O(n)|O(n)|---|
|No.5|[Longest Palindromic Substring](https://leetcode.com/problems/longest-palindromic-substring/)|[Solution](./0005/0005.py)|[Note](./0005/note0005.md)|Medium|O(n^2)|O(1)|Greedy|
|No.3|[Longest Substring Without Repeating Characters](https://leetcode.com/problems/longest-substring-without-repeating-characters/)|[Solution](./0003/0003.py)|[Note](./0003/note0003.md)|Medium|O(n)|O(n)|slide window|
|No.15|[3Sum](https://leetcode.com/problems/3sum/)|[Solution](./0015/0015.py)|[Note](./0015/note0015.md)|Medium|O(n^2)|O(1)|2 pointers|
|No.301|[Remove Invalid Parentheses](https://leetcode.com/problems/remove-invalid-parentheses/)|[Solution](./0001/0301.py)|[Note](./0301/note0301.md)|Hard|O(2^(l+r))|O(n^2)|dfs|
|No.76|[Minimum Window Substring](https://leetcode.com/problems/minimum-window-substring/)|[Solution](./0076/0076.py)|[Note](./0076/note0076.md)|Hard|O(n))|O(n)|dfs|
|No.22|[Generate Parentheses](https://leetcode.com/problems/generate-parentheses/)|[Solution](./0001/0022.py)|[Note](./0022/note0022.md)|Medium|O(2^n))|O(n)|dfs|
|No.49|[Group Anagrams](https://leetcode.com/problems/group-anagrams/)|[Solution](./0049/0049.py)|[Note](./0049/note0049.md)|Medium|O(n))|O(n)|---|
|No.336|[Palindrome Pairs](https://leetcode.com/problems/palindrome-pairs/)|[Solution](./0336/0336.py)|[Note](./0336/note0336.md)|Hard|O(n^2))|O(n)|---|
|No.68|[Text Justification](https://leetcode.com/problems/text-justification/)|[Solution](./0068/0068.py)|[Note](./0068/note0068.md)|Hard|O(n))|O(n)|---|
|No.17|[Letter Combinations of a Phone Number](https://leetcode.com/problems/letter-combinations-of-a-phone-number/)|[Solution](./0017/0017.py)|[Note](./0017/note0017.md)|Medium|O(4^n))|O(4^n+n)|dfs|
|No.468|[Validate IP Address](https://leetcode.com/problems/validate-ip-address/)|[Solution](./0468/0468.py)|[Note](./0468/note0468.md)|Medium|O(n))|O(n)|---|
|No.937|[Reorder Data in Log Files](https://leetcode.com/problems/reorder-data-in-log-files/)|[Solution](./937/937.py)|[Note](./937/note937.md)|Easy|O(n))|O(n)|---|
|No.91|[Decode Ways](https://leetcode.com/problems/decode-ways/)|[Solution](./0091/0091.py)|[Note](./0091/note0091.md)|Medium|O(n))|O(n)|dp |


## Linked List
|NO.|Title|Solution|Note|Difficulty|Time|Space|Tag|
|---|-----|--------|----|----------|----|-----|---|
|No.82|[Remove Duplicates from Sorted List II](https://leetcode.com/problems/remove-duplicates-from-sorted-list-ii/)|[Solution](./0082/0082.py)|[Note](./0082/note0082.md)|Medium|O(n)|O(1)|---|
|No.21|[Merge Two Sorted Lists](https://leetcode.com/problems/merge-two-sorted-lists/)|[Solution](./0021/0021.py)|[Note](./0021/note0021.md)|Easy|O(n)|O(1)|Dummy node|
|No.24|[Swap Nodes in Pairs](https://leetcode.com/problems/swap-nodes-in-pairs/)|[Solution](./0024/0024.py)|[Note](./0024/note0024.md)|Medium|O(n)|O(1)|---|
|No.83|[Remove Duplicates from Sorted List](https://leetcode.com/problems/remove-duplicates-from-sorted-list/)|[Solution](./0083/0083.py)|[Note](./0083/note0083.md)|Easy|O(n)|O(1)|---|
|No.160|[Intersection of Two Linked Lists](https://leetcode.com/problems/intersection-of-two-linked-lists/)|[Solution](./0160/0160.py)|[Note](./0160/note0160.md)|Easy|O(n)|O(1)|---|
|No.203|[Remove Linked List Elements](https://leetcode.com/problems/remove-linked-list-elements/)|[Solution](./0203/0203.py)|[Note](./0203/note0203.md)|Easy|O(n)|O(1)|---|
|No.237|[Delete Node in a Linked List](https://leetcode.com/problems/delete-node-in-a-linked-list/)|[Solution](./0237/0237.py)|[Note](./0237/note0237.md)|Easy|O(1)|O(1)|---|
|No.234|[Palindrome Linked List](https://leetcode.com/problems/palindrome-linked-list/)|[Solution](./0234/0234.py)|[Note](./0234/note0234.md)|Easy|O(n)|O(n)|---|
|No.206|[Reverse Linked List](https://leetcode.com/problems/reverse-linked-list/)|[Solution](./0206/0206.py)|[Note](./0206/note0206.md)|Easy|O(n)|O(1)|---|
|No.92|[Reverse Linked List II](https://leetcode.com/problems/reverse-linked-list-ii/)|[Solution](./0092/0092.py)|[Note](./0092/note0092.md)|Medium|O(n)|O(1)|---|
|No.2|[Add Two Numbers](https://leetcode.com/problems/add-two-numbers/)|[Solution](./0002/0002.py)|[Note](./0002/note0002.md)|Medium|O(n)|O(n)|---|
|No.19|[Remove Nth Node From End of List](https://leetcode.com/problems/remove-nth-node-from-end-of-list/)|[Solution](./0019/0019.py)|[Note](./0019/note0019.md)|Medium|O(n)|O(1)|---|
|No.141|[Linked List Cycle](https://leetcode.com/problems/linked-list-cycle/)|[Solution](./0141/0141.py)|[Note](./0141/note0141.md)|Easy|O(n)|O(1)|fast slow pointers|
|No.142|[Linked List Cycle II](https://leetcode.com/problems/linked-list-cycle-ii/)|[Solution](./0142/0142.py)|[Note](./0142/note0142.md)|Easy|O(n)|O(1)|fast slow pointers|
|No.23|[Merge k Sorted Lists](https://leetcode.com/problems/merge-k-sorted-lists/)|[Solution](./0023/0023.py)|[Note](./0023/note0023.md)|Easy|O(nlogn)|O(nk)|---|
|No.61|[Rotate List](https://leetcode.com/problems/rotate-list/)|[Solution](./0061/0061.py)|[Note](./0061/note0061.md)|Medium|O(n)|O(1)|---|
|No.138|[Copy List with Random Pointer](https://leetcode.com/problems/copy-list-with-random-pointer/)|[Solution](./0138/0138.py)|[Note](./0138/note0138.md)|Medium|O(n)|O(n)|---|
|No.86|[Partition List](https://leetcode.com/problems/partition-list/)|[Solution](./0086/0086.py)|[Note](./0086/note0086.md)|Medium|O(n)|O(n)|---|
|No.143|[Reorder List](https://leetcode.com/problems/reorder-list/)|[Solution](./0143/0143.py)|[Note](./0143/note0143.md)|Medium|O(n)|O(n)|---|





## Stack
|NO.|Title|Solution|Note|Difficulty|Time|Space|Tag|
|---|-----|--------|----|----------|----|-----|---|
|No.56|[Merge Intervals](https://leetcode.com/problems/merge-intervals/)|[Solution](./0056/0056.py)|[Note](./0056/note0056.md)|Medium|O(n)|O(n)|---|
|No.20|[Valid Parentheses](https://leetcode.com/problems/valid-parentheses/)|[Solution](./0020/0020.py)|[Note](./0020/note0020.md)|Easy|O(n)|O(n)|---|
|No.224|[Basic Calculator](https://leetcode.com/problems/basic-calculator/)|[Solution](./0224/0224.py)|[Note](./0224/note0224.md)|Hard|O(n)|O(n)|---|



## Recursion
|NO.|Title|Solution|Note|Difficulty|Time|Space|Tag|
|---|-----|--------|----|----------|----|-----|---|





## Queue
|NO.|Title|Solution|Note|Difficulty|Time|Space|Tag|
|---|-----|--------|----|----------|----|-----|---|





## Binary Tree
|NO.|Title|Solution|Note|Difficulty|Time|Space|Tag|
|---|-----|--------|----|----------|----|-----|---|
|No.226|[Invert Binary Tree](https://leetcode.com/problems/invert-binary-tree/)|[Solution](./0226/0226.py)|[Note](./0226/note0226.md)|Easy|O(logn)|O(n)|---|
|No.538|[Convert BST to Greater Tree](https://leetcode.com/problems/convert-bst-to-greater-tree/)|[Solution](./0538/0538.py)|[Note](./0538/note0538.md)|Easy|O(logn)|O(n)|---|
|No.543|[Diameter of Binary Tree](https://leetcode.com/problems/diameter-of-binary-tree/)|[Solution](./0543/0543.py)|[Note](./0543/note0543.md)|Easy|O(logn)|O(n)|---|
|No.687|[Longest Univalue Path](https://leetcode.com/problems/longest-univalue-path/)|[Solution](./0687/0687.py)|[Note](./0687/note0687.md)|Easy|O(logn)|O(n)|---|
|No.897|[Increasing Order Search Tree](https://leetcode.com/problems/increasing-order-search-tree/)|[Solution](./0897/0897.py)|[Note](./0897/note0897.md)|Easy|O(n)|O(n)|---|
|No.617|[Merge Two Binary Trees](https://leetcode.com/problems/merge-two-binary-trees/)|[Solution](./0617/0617.py)|[Note](./0617/note0617.md)|Easy|O(n)|O(n)|---|
|No.606|[Construct String from Binary Tree](https://leetcode.com/problems/construct-string-from-binary-tree/)|[Solution](./0606/0606.py)|[Note](./0606/note0606.md)|Easy|O(n)|O(n)|---|
|No.572|[Subtree of Another Tree](https://leetcode.com/problems/subtree-of-another-tree/)|[Solution](./0572/0572.py)|[Note](./0572/note0572.md)|Easy|O(n)|O(n)|---|
|No.563|[Binary Tree Tilt](https://leetcode.com/problems/binary-tree-tilt/)|[Solution](./0563/0563.py)|[Note](./0563/note0563.md)|Easy|O(n)|O(n)|---|
|No.94|[Binary Tree Inorder Traversal](https://leetcode.com/problems/binary-tree-inorder-traversal/)|[Solution](./0094/0094.py)|[Note](./0094/note0094.md)|Medium|O(n)|O(n)|---|
|No.112|[Path Sum](https://leetcode.com/problems/path-sum/)|[Solution](./0112/0112.py)|[Note](./0112/note0112.md)|Easy|O(n)|O(n)|---|
|No.257|[Binary Tree Paths](https://leetcode.com/problems/binary-tree-paths/)|[Solution](./0257/0257.py)|[Note](./0257/note0257.md)|Easy|O(n)|O(n)|---|
|No.701|[Insert into a Binary Search Tree](https://leetcode.com/problems/insert-into-a-binary-search-tree/)|[Solution](./0701/0701.py)|[Note](./0701/note0701.md)|Medium|O(logn)|O(n)|---|
|No.1008|[Construct Binary Search Tree from Preorder Traversal](https://leetcode.com/problems/construct-binary-search-tree-from-preorder-traversal/)|[Solution](./1008/1008.py)|[Note](./1008/note1008.md)|Medium|O(logn)|O(n)|---|
|No.144|[Binary Tree Preorder Traversal](https://leetcode.com/problems/binary-tree-preorder-traversal/)|[Solution](./0144/0144.py)|[Note](./0144/note144.md)|Medium|O(n)|O(n)|---|
|No.814|[Binary Tree Preorder Traversal](https://leetcode.com/problems/binary-tree-pruning/)|[Solution](./0814/0814.py)|[Note](./0814/note814.md)|Medium|O(n)|O(n)|---|
|No.145|[Binary Tree Postorder Traversal](https://leetcode.com/problems/binary-tree-pruning/)|[Solution](./0145/0145.py)|[Note](./0145/note145.md)|Medium|O(n)|O(n)|---|
|No.102|[Binary Tree Level Order Traversal](https://leetcode.com/problems/binary-tree-level-order-traversal/)|[Solution](./0102/0102.py)|[Note](./0102/note102.md)|Medium|O(n)|O(n)|---|
|No.105|[Construct Binary Tree from Preorder and Inorder Traversal](https://leetcode.com/problems/construct-binary-tree-from-inorder-and-postorder-traversal/)|[Solution](./0105/0105.py)|[Note](./0105/note105.md)|Medium|O(n)|O(n)|---|
|No.106|[Construct Binary Tree from Inorder and Postorder Traversal](https://leetcode.com/problems/construct-binary-tree-from-preorder-and-inorder-traversal/)|[Solution](./0106/0106.py)|[Note](./0106/note106.md)|Medium|O(n)|O(n)|---|
|No.116|[Populating Next Right Pointers in Each Node](https://leetcode.com/problems/populating-next-right-pointers-in-each-node/)|[Solution](./0116/0116.py)|[Note](./0116/note116.md)|Medium|O(n)|O(n)|---|
|No.117|[Populating Next Right Pointers in Each Node II](https://leetcode.com/problems/populating-next-right-pointers-in-each-node-ii/)|[Solution](./0117/0117.py)|[Note](./0117/note117.md)|Medium|O(n)|O(n)|---|
|No.652|[Find Duplicate Subtrees](https://leetcode.com/problems/find-duplicate-subtrees/)|[Solution](./01652/0652.py)|[Note](./0652/note652.md)|Medium|O(n^2)|O(n)^2|---|
|No.104|[Maximum Depth of Binary Tree](https://leetcode.com/problems/maximum-depth-of-binary-tree/)|[Solution](./01104/0104.py)|[Note](./0104/note104.md)|Medium|O(n)|O(n)|---|
|No.655|[Print Binary Tree](https://leetcode.com/problems/print-binary-tree/)|[Solution](./01655/0655.py)|[Note](./0655/note655.md)|Medium|O(n)|O(n)|dfs/binary search|
|No.297|[Serialize and Deserialize Binary Tree](https://leetcode.com/problems/serialize-and-deserialize-binary-tree/)|[Solution](./0297/0297.py)|[Note](./0297/note297.md)|Hard|O(n)|O(n)|dfs/iter()/dequeue()|
|No.428|[Serialize and Deserialize N-ary Tree](https://leetcode.com/problems/serialize-and-deserialize-n-ary-tree/)|[Solution](./0428/0428.py)|[Note](./0428/note428.md)|Hard|O(n)|O(n)|dfs/dequeue()|
|No.124|[Binary Tree Maximum Path Sum](https://leetcode.com/problems/binary-tree-maximum-path-sum/)|[Solution](./0124/0124.py)|[Note](./0124/note124.md)|Hard|O(n)|O(n)|---|
|No.449|[Serialize and Deserialize BST](https://leetcode.com/problems/serialize-and-deserialize-bst/)|[Solution](./0449/0449.py)|[Note](./0449/note449.md)|Medium|O(n)|O(n)|---|
|No.103|[Binary Tree Zigzag Level Order Traversal](https://leetcode.com/problems/binary-tree-zigzag-level-order-traversal/)|[Solution](./0103/0103.py)|[Note](./0103/note103.md)|Medium|O(n)|O(n)|level traversal|
|No.119|[Binary Tree Right Side View](https://leetcode.com/problems/binary-tree-right-side-view/)|[Solution](./0119/0119.py)|[Note](./0119/note119.md)|Medium|O(n)|O(n)|level traversal|
|No.426|[Convert Binary Search Tree to Sorted Doubly Linked List](https://leetcode.com/problems/convert-binary-search-tree-to-sorted-doubly-linked-list/)|[Solution](./0426/0426.py)|[Note](./0426/note426.md)|Medium|O(n)|O(n)|inoder/mode|
|No.863|[All Nodes Distance K in Binary Tree](https://leetcode.com/problems/all-nodes-distance-k-in-binary-tree/)|[Solution](./0863/0863.py)|[Note](./0863/note863.md)|Medium|O(n)|O(n)|parent node/dfs|graph/bfs|
|No.96|[Unique Binary Search Trees](https://leetcode.com/problems/unique-binary-search-trees/)|[Solution](./0096/0096.py)|[Note](./0096/note096.md)|Medium|O(n^2)|O(n)|dp|
|No.987|[Vertical Order Traversal of a Binary Tree](https://leetcode.com/problems/vertical-order-traversal-of-a-binary-tree/)|[Solution](./0987/0987.py)|[Note](./0987/note987.md)|Medium|O(n)|O(n)|sort dict/map|
|No.222|[Count Complete Tree Nodes](https://leetcode.com/problems/count-complete-tree-nodes/)|[Solution](./0222/0222.py)|[Note](./0222/note222.md)|Medium|O(logn)|O(1)|binary search|
|No.450|[Delete Node in a BST](https://leetcode.com/problems/delete-node-in-a-bst/)|[Solution](./0450/0450.py)|[Note](./0450/note450.md)|Medium|O(h)|O(1)|recursion|
|No.99|[Recover Binary Search Tree](https://leetcode.com/problems/recover-binary-search-tree/)|[Solution](./0099/0099.py)|[Note](./0099/note099.md)|Hard|O(n)|O(n)|---|
|No.114|[Flatten Binary Tree to Linked List](https://leetcode.com/problems/flatten-binary-tree-to-linked-list/)|[Solution](./0114/0114.py)|[Note](./0114/note114.md)|Medium|O(n)|O(1)|recursion|


## Hash Table
|NO.|Title|Solution|Note|Difficulty|Time|Space|Tag|
|---|-----|--------|----|----------|----|-----|---|



## Sort
|NO.|Title|Solution|Note|Difficulty|Time|Space|Tag|
|---|-----|--------|----|----------|----|-----|---|
|No.973|[K Closest Points to Origin](https://leetcode.com/problems/k-closest-points-to-origin/)|[Solution](./0973/0973.py)|[Note](./0973/note973.md)|Medium|O(n)|O(n)|---|



## Heap
|NO.|Title|Solution|Note|Difficulty|Time|Space|Tag|
|---|-----|--------|----|----------|----|-----|---|



## Binary Search
|NO.|Title|Solution|Note|Difficulty|Time|Space|Tag|
|---|-----|--------|----|----------|----|-----|---|
|No.4|[Median of Two Sorted Arrays](https://leetcode.com/problems/median-of-two-sorted-arrays/)|[Solution](./0004/0004.py)|[Note](./0004/note0004.md)|Hard|O(log(m+n))|O(n)|---|
|No.33|[Search in Rotated Sorted Array](https://leetcode.com/problems/search-in-rotated-sorted-array/)|[Solution](./0033/0033.py)|[Note](./0033/note0033.md)|Medium|O(log(n))|O(1)|---|
|No.34|[Find First and Last Position of Element in Sorted Array](https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/)|[Solution](./0034/0034.py)|[Note](./0034/note0034.md)|Medium|O(log(n))|O(1)|---|

## Binary Search Tree
|NO.|Title|Solution|Note|Difficulty|Time|Space|Tag|
|---|-----|--------|----|----------|----|-----|---|



## N-ary Tree
|NO.|Title|Solution|Note|Difficulty|Time|Space|Tag|
|---|-----|--------|----|----------|----|-----|---|



## Math
|NO.|Title|Solution|Note|Difficulty|Time|Space|Tag|
|---|-----|--------|----|----------|----|-----|---|
|No.7|[Reverse Integer](https://leetcode.com/problems/reverse-integer/)|[Solution](./0007/0007.py)|[Note](./0007/note0007.md)|Easy|O(n)|O(1)|---|


## Graph
|NO.|Title|Solution|Note|Difficulty|Time|Space|Tag|
|---|-----|--------|----|----------|----|-----|---|
|No.200|[Number of Islands](https://leetcode.com/problems/number-of-islands/)|[Solution](./0200/0200.py)|[Note](./0200/note200.md)|Medium|O(mn)|O(1)|dfs|
|No.332|[Reconstruct Itinerary](https://leetcode.com/problems/reconstruct-itinerary/)|[Solution](./0332/0332.py)|[Note](./0332/note332.md)|Medium|O(nlogn)|O(n)|dfs|
|No.399|[Evaluate Division](https://leetcode.com/problems/evaluate-division/)|[Solution](./0399/0399.py)|[Note](./0399/note399.md)|Medium|O(n)|O(n)|dfs|

## Backtracking
|NO.|Title|Solution|Note|Difficulty|Time|Space|Tag|
|---|-----|--------|----|----------|----|-----|---|




## Dynamic Programming
|NO.|Title|Solution|Note|Difficulty|Time|Space|Tag|
|---|-----|--------|----|----------|----|-----|---|
|No.53|[Maximum Subarray](https://leetcode.com/problems/maximum-subarray/)|[Solution](./0053/0053.py)|[Note](./0053/note0053.md)|Medium|O(n)|O(n)|---|
|No.121|[Best Time to Buy and Sell Stock](https://leetcode.com/problems/best-time-to-buy-and-sell-stock/)|[Solution](./0121/0121.py)|[Note](./0121/note0121.md)|Easy|O(n)|O(1)|---|
|No.10|[Regular Expression Matching](https://leetcode.com/problems/regular-expression-matching/)|[Solution](./0010/0010.py)|[Note](./0010/note0010.md)|Hard|O(n*m)|O(n*m)|---|
|No.96|[Unique Binary Search Trees](https://leetcode.com/problems/unique-binary-search-trees/)|[Solution](./0096/0096.py)|[Note](./0096/note096.md)|Medium|O(n^2)|O(n)|tree|
|No.91|[Decode Ways](https://leetcode.com/problems/decode-ways/)|[Solution](./0091/0091.py)|[Note](./0091/note0091.md)|Medium|O(n))|O(n)|dp|