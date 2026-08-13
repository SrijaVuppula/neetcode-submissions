class Solution:
    def isValid(self, s: str) -> bool:
        a = []

        pairs = {
            ")": "(",
            "]": "[",
            "}": "{"
        }

        for char in s:
            if char in "([{":
                a.append(char)

            else:
                if not a:
                    return False

                if a[-1] == pairs[char]:
                    a.pop()
                else:
                    return False

        return len(a) == 0