class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anag = defaultdict(list)
        for s in strs:
            sortedChars = sorted(s)
            sortedS = ''.join(sortedChars)
            anag[sortedS].append(s)
        return list(anag.values())


