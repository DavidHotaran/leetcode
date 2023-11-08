class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        l = 0
        r = len(matrix) - 1
        p = 0

        while l <= r:
            mid = (r + l) // 2
            row = matrix[mid]

            if row[0] > target:
                r = mid - 1
            elif row[-1] < target:
                l = mid + 1
            else:
                p = mid
                break

        if not (l <= r):
            return False

        l = 0
        r = len(matrix[0]) - 1
        row = matrix[p]

        while l <= r:
            mid = (r + l) // 2

            if row[mid] > target:
                r = mid - 1
            elif row[mid] < target:
                l = mid + 1
            else:
                return True
        return False
