class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        answer = [[], []]
        s1 = set()
        s2 = set()

        for num in nums1:
            s1.add(num)
        for num in nums2:
            s2.add(num)

        for num in s1:
            if num not in s2:
                answer[0].append(num)

        for num in s2:
            if num not in s1:
                answer[1].append(num)
        return answer
