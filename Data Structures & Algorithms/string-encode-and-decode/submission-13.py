class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ""
        for s in strs:
            for char in s:
                asNum = ord(char)
                res += str(asNum)
                res += '.'
            res += '!'

        return res

    def decode(self, s: str) -> List[str]:
        newList = []
        arr = s.split('!')

        for i in arr[:-1]:
            parts = i.split('.')
            word = ""

            for p in parts:
                if p == "":
                    continue

                backToChar = chr(int(p))
                word += backToChar

            newList.append(word)

        return newList