class Solution:
    def isPalindrome(self, s: str) -> bool:
        A = s.casefold()
        B = "".join(char for char in A if char.isalnum())
        i = 0
        j = len(B) - 1

        while (i < j):
            if B[i] != B[j]:
                return False
            else:
                i = i + 1
                j = j - 1
        return True