class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left = 0
        right = 0
        charSet = set()
        maxx = 0

        while right<len(s):
            while s[right] in charSet:
                charSet.remove(s[left])
                left+=1
            charSet.add(s[right])
            maxx=max(maxx,right-left+1)
            right+=1
        return maxx        