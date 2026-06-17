class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams_list = []
        saved_anagrams = {}
        anagram_index = -1
        for string in strs:
            freq_string = {}

            for c in string:
                freq_string[c] = freq_string.get(c, 0) + 1

            # print(freq_string)
            tup_freq_string = tuple(sorted(freq_string.items()))
            # print(tup_freq_string)

            if tup_freq_string not in saved_anagrams.keys():
                anagram_index += 1
                saved_anagrams[tup_freq_string] = anagram_index
                anagrams_list.append([string])
            else:
                current_bucket = saved_anagrams.get(tup_freq_string)
                anagrams_list[current_bucket].append(string)

        return anagrams_list
                
