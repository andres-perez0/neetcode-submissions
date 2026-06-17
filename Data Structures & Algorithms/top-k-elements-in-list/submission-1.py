class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq_table = {}
        return_list = []

        for n in nums:
            freq_table[n] = freq_table.get(n, 0) + 1

        freq_table_sort = sorted(freq_table.items(), key=lambda a: a[1], reverse=True)
        
        for n in freq_table_sort:
            if k <= 0: break
            return_list.append(n[0])
            k -= 1

        return return_list
            