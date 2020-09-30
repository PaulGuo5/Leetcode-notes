class Solution:
    def isPossible(self, nums: List[int]) -> bool:
        cnt = collections.Counter(nums)
        pre = collections.Counter()
        for n in nums:
            if cnt[n] == 0: continue
            elif pre[n] > 0:
                pre[n] -= 1
                pre[n+1] += 1
            elif cnt[n+1] > 0 and cnt[n+2] > 0:
                cnt[n+1] -= 1
                cnt[n+2] -= 1
                pre[n+3] += 1
            else:
                return False
            cnt[n] -= 1
        return True
