class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        res = 0
        cursum =0
        ps = {0 : 1}
        for n in nums:
            cursum += n
            diff = cursum-k
            res += ps.get(diff, 0)
            ps[cursum] = ps.get(cursum, 0) + 1
        return res
