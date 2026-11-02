class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}
        for i, num in enumerate(nums):
            need = target - num
            if need in seen:
                if seen[need] < i:
                    return [seen[need], i]
                else:
                    return [i, seen[need]]
            else:
                seen[num] = i