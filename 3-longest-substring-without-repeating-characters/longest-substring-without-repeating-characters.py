class Solution(object):
    def lengthOfLongestSubstring(self, s):
        set_char=set()
        l=0
        max_len=0
        for i in range(len(s)):
            while s[i] in set_char:
                set_char.remove(s[l])
                l+=1
            set_char.add(s[i])
            max_len=max(max_len,i-l+1)
        return max_len
       