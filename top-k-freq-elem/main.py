class Solution(object):
    def topKFrequent(self, nums, k):
        counts = {}
        answer = []
        unique = set(nums)
        for i in unique:
            counts[i] = 0
        
        for i in nums:
            counts[i] += 1

        highest = max(counts.values())
        while len(answer) < k:
            for key, value in counts.items():
                if value == highest:
                    answer.append(key)
            highest -=1

        return answer


        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """