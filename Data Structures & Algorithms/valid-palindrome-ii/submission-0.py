class Solution:
    def validPalindrome(self, s: str) -> bool:
        def isPalindrome(A):
            i = 0
            j = len(A) - 1

            while (i < j):
                if A[i] != A[j]:
                    return False
                else:
                    i = i + 1
                    j = j - 1
            return True

        i, j = 0, len(s) - 1
        while i < j:
            if s[i] != s[j]:
                return isPalindrome(s[:i] + s[i+1:]) or isPalindrome(s[:j] + s[j+1:])
            i = i + 1
            j = j - 1
        return True