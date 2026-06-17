class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s = s.replace(" ","")
        t = t.replace(" ","")
        freqTable_s = {}
        freqTable_t = {}

        if len(s) != len(t): 
            return False

        for i, c in enumerate(s):
            freqTable_s[c] = freqTable_s.get(c, 0) + 1

            try: 
                if t[i]:
                    freqTable_t[t[i]] = freqTable_t.get(t[i], 0) + 1
                else: 
                    return False
            except IndexError:
                return False

        return freqTable_s == freqTable_t

        