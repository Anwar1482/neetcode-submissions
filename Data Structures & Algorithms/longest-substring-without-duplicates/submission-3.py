class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s)==1:
            return 1

        maxS = 0
        l = 0
        r = 1
        while r <len(s):
            if s[r] in s[l:r]:
                maxS=max(maxS, len(s[l:r]))
                l+=1
            else:
                r+=1

        maxS = max(maxS, len(s[l:r]))
        return maxS

