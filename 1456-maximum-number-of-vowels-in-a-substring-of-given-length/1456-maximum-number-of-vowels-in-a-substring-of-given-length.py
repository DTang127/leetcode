class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        vowels, result = 0, 0

        for i in range(k):
            if s[i] == 'a' or s[i] == 'e' or s[i] == 'i' or s[i] == 'o' or s[i] == 'u':
                vowels += 1
        result = max(vowels, result)
        for i in range(k, len(s)):
            if s[i] == 'a' or s[i] == 'e' or s[i] == 'i' or s[i] == 'o' or s[i] == 'u':
                vowels += 1
            if s[i-k] == 'a' or s[i-k] == 'e' or s[i-k] == 'i' or s[i-k] == 'o' or s[i-k] == 'u':
                vowels -= 1
            result = max(vowels, result)

        return result
        