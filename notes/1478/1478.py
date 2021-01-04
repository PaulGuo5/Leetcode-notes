class Solution:
    def minDistance(self, houses: List[int], k: int) -> int:
#         dp[i][k] be a minimum total distance when we use i houses and only k mailboxes.
#         The idea is when we add new mailbox, undersand, how many houses it can cover.
# How we can evaluate dp[i][k]? We need to look for all smaller j at the element dp[j][k-1] and also we need to know what distance we need to add for houses between j and i with only one mailbox.

# Good idea is to precalculate all possible costs[i][j]: total distances to cover all houses between number i and number j. I used idea of @hiepit, who did it in O(n^3) elegant way: we need to put mailbox into the median of our points. Note, that this part can be improved to O(n^2), but it is not worth it, because we have bigger terms.

# Now, all we need to do is to iterate over all n houses and over all k mailboxes and update all table dp, let us do it on example houses = [1,4,8,10,20]. Here by # I denoted elements which are in fact should be zeros: number of houses is less or equal than number of mailboxes. However it is not neccesary to see what is inside, because we never use these elements. We also define the first row of our dp table with costs[0][:], because it is exactly total minimum distance for 1 mailbox.

# time complexity is O(n^3 + n^2k) = O(n^3), space complexity is O(nk).
        n = len(houses)
        houses = sorted(houses)
        costs = [[0] * n for _ in range(n)]
        
        # for i, j in product(range(n), range(n)):
        for i in range(n):
            for j in range(n):
                median = houses[(i + j) // 2]
                for t in range(i, j + 1):
                    costs[i][j] += abs(median - houses[t])
                    
        print(costs)
        dp = [[float('inf')] * k for _ in range(n)]
        for i in range(n): dp[i][0] = costs[0][i]
        
        for k_it in range(1, k):
            for i_1 in range(n):
                for i_2 in range(i_1):
                    dp[i_1][k_it] = min(dp[i_1][k_it], dp[i_2][k_it-1] + costs[i_2+1][i_1])
        print(dp)
        return dp[-1][-1]
