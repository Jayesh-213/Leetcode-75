class Solution:
    def kidsWithCandies(self, candies: list[int], extraCandies: int) -> list[bool]:
        maximum = max(candies)
        res =[]
        for i in range(len(candies)):
            if candies[i] + extraCandies >= maximum:
                res.append(True)
            else:
                res.append(False)
        return res
