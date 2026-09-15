class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        r = 0
        s = 0
        ps = {0: 1}
        for n in nums:
            s+=n
            d=s-k
            r+=ps.get(d,0)
            ps[s] = ps.get(s, 0)+1
        return r