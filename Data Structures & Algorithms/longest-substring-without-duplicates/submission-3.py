class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s:
            return 0

        n = len(s)

        if n == 1:
            return 1

        l, r = 0, 1
        hm = {}
        hm[s[l]] = 1
        l_ss = 0

        while r < n:
            while (s[r] in hm):
                del hm[s[l]]
                l += 1
            
            hm[s[r]] = 1

            if l_ss < r - l + 1:
                l_ss = r - l + 1

            r += 1

        print(r)
        print(l)

        return l_ss         

