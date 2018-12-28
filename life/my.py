def expandAroundCenter(s, left, right):
    L = left
    R = right
    while (L >= 0 and R < len(s) and s[L] == s[R]):
        L -= 1
        R += 1
    return R - L - 1


class Solution:
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        if (not s or len(s) < 1):
            return ""
        start = 0
        end = 0
        for i in range(len(s)):
            len1 = expandAroundCenter(s, i, i)
            len2 = expandAroundCenter(s, i, i + 1)
            lent = max(len1, len2)
            if (lent > end - start):
                start = i - (lent - 1) // 2
                end = i + lent // 2
        return s[start:end + 1]


