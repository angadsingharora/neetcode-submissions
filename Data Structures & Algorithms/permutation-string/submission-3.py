class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        #loop through all s1 length substrings in s2 and hashmap to see if equivalent?
        count = {}
        for i in range(len(s1)):
            count[s1[i]] = 1+count.get(s1[i],0)
        
        left = 0
        window = {}

        for right in range(len(s2)):
            window[s2[right]] = 1 + window.get(s2[right], 0)
            if right - left + 1 > len(s1):
                window[s2[left]]-=1
                if window[s2[left]] == 0:
                    del window[s2[left]]
                left+=1

            if window == count:
                    return True
        return False

