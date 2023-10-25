class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        def newString(str):
            fast = 0
            result = []
            while (fast < len(str)):
                if (str[fast] == '#'):
                    result = result[:-1]
                else:
                    result += [str[fast]]
                fast += 1
            return result
        return newString(s) == newString(t)
        