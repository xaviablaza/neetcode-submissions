class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        res = 0
        curSum = 0
        prefixsums = {0: 1}
        for n in nums:
            curSum += n
            diff = curSum - k
            res += prefixsums.get(diff, 0)
            prefixsums[curSum] = prefixsums.get(curSum, 0) + 1
        return res