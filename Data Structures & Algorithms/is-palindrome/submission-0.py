class Solution:
    def isPalindrome(self, s: str) -> bool:
        text = s.lower()
        i = 0
        j = len(text) - 1

        while i < j:
            if not text[i].isalnum():
                i += 1
            elif not text[j].isalnum():
                j -= 1
            else: 
                if text[i] == text[j]:
                    i += 1
                    j -= 1
                    print(j)
                else:
                    return False
        return True
        