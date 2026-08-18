class Solution:
    def minWindow(self, s: str, t: str) -> str:

        #build hash map of frequency in string t
        #sliding window, iterate right and build frequency hash map until count of each letter greater than or equal to hashmap of string t. 
        #set that as min, move left pointer until hashmap invalid, and build hashmap. compare to min and update if neccessary
        #if iterates through whole string and cant find all characters return ""
        left = 0
        count = {}
        for char in t:
            count[char] = 1 + count.get(char,0)

        window = {}
        have = 0
        need = len(count)
        answer = ""

        for right in range(len(s)):
            c= s[right]
            window[c] = 1+ window.get(c,0)

            if c in count and window[c] == count[c]:
                have +=1
            while have == need:
                current = s[left:right+1]
                if answer == "" or len(current) < len(answer):
                    answer = current
                window[s[left]]-=1
                if s[left] in count and window[s[left]] < count[s[left]]:
                    have-=1
                left+=1
        return answer
            