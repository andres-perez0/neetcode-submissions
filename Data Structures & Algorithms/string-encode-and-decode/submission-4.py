class Solution:

    def encode(self, strs: List[str]) -> str:
        list_length = 0
        word_lengths = []
        return_string = ""
        for string in strs:
            list_length += 1
            word_lengths.insert(0, str(len(string)))
            return_string += string
        return_string += ("," + ",".join(word_lengths) + "," + str(list_length))
        ### HelloWorld552
        return return_string 

    def decode(self, s: str) -> List[str]:
        # print(s)
        return_list = []
        list_length = ""
        while s[-1] != ",":
            list_length = s[-1] + list_length
            s = s[:-1]
        list_length = int(list_length)
        s = s[:-1]

        for n in range(list_length):
            # print(s)
            word_length = ""
            while s[-1] != ",":
                word_length = s[-1] + word_length
                s = s[:-1]
            s = s[:-1] # to account for the "," at the end

            word_length = int(word_length)

            if word_length == 0:
                return_list.append("")
            else:
                word = s[0:word_length]
                return_list.append(word)

            s = s[word_length:]                

        return return_list

