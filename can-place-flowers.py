class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        if n == 0: return True

        if len(flowerbed) == 1 and flowerbed[0] == 0:
            return True
        elif len(flowerbed) == 1 and flowerbed[0] == 1:
            return False

        # check if current spot is 0
        # check if spot to the left is 0 (not 1)
        # check if spot to the right is 0 (not 1)
        # if we are at pos=0, don't check left
        # if we are pos=len(s)-1, don't check right
        for i, el in enumerate(flowerbed):
            if el == 0:
                if i == 0:
                    if flowerbed[i+1] == 0:
                        flowerbed[i] = 1
                        n -=1
                elif i == len(flowerbed)-1:
                    if flowerbed[i-1] == 0:
                        flowerbed[i] = 1
                        n -=1
                else:
                    if flowerbed[i-1] == 0 and flowerbed[i+1] == 0:
                        flowerbed[i] = 1
                        n -= 1
            if n == 0:
                return True
            #print(flowerbed, i, flowerbed[i])
        return n == 0