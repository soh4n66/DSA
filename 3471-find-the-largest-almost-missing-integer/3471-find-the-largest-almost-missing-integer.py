class Solution:
    def largestInteger(self, nums: List[int], k: int) -> int:
        subArrays = []
        freq = {}
        len_one=[]
        if len(nums)<k:
            return -1

        for i in range(len(nums) - k + 1):
            subArrays.append(nums[i:i+k])

        for arr in subArrays:
            for i in set(arr):
                if i in freq:
                    freq[i]+=1
                else:
                    freq[i]=1

        for i in freq:
            if freq[i] == 1:
                len_one.append(i)
        
        if len(len_one) == 0:
            return -1

        return max(len_one)