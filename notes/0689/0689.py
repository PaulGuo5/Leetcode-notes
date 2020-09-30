class Solution:
    def maxSumOfThreeSubarrays(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)
        left, right = [0]*n, [n-k]*n
        prefix_sum = [0]
        cnt = 0
        for i in range(n):
            cnt += nums[i]
            prefix_sum.append(cnt)
        
        total = prefix_sum[k] - prefix_sum[0]
        for i in range(k, n):
            if total < prefix_sum[i+1] - prefix_sum[i-k+1]:
                total = prefix_sum[i+1] - prefix_sum[i-k+1]
                left[i] = i-k+1
            else:
                left[i] = left[i-1]
        
        total = prefix_sum[n] - prefix_sum[n-k]
        for i in range(n-k-1, -1, -1):
            if total <= prefix_sum[i+k] - prefix_sum[i]:
                total = prefix_sum[i+k] - prefix_sum[i]
                right[i] = i
            else:
                right[i] = right[i+1]
        
        mx = -float('inf')
        res = [0, 0, 0]
        for i in range(k, n-2*k+1):
            l, r = left[i-1], right[i+k]
            l_val = prefix_sum[l+k] - prefix_sum[l]
            r_val = prefix_sum[r+k] - prefix_sum[r]
            m_val = prefix_sum[i+k] - prefix_sum[i]
            if mx < l_val+m_val+r_val:
                mx = l_val+m_val+r_val
                res = [l, i, r]
        return res
