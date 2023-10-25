class Solution:
    def successfulPairs(
        self, spells: List[int], potions: List[int], success: int
    ) -> List[int]:
        potions.sort()
        ret = []

        for spell in spells:
            l = 0
            r = len(potions) - 1
            temp = len(potions)

            while l <= r:
                mid = (l + r) // 2
                if potions[mid] * spell >= success:
                    temp = mid
                    r = mid - 1
                if potions[mid] * spell < success:
                    l = mid + 1

            ret.append(len(potions) - temp)

        return ret
