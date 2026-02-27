class Solution:
    def constructRectangle(self, area: int) -> List[int]:
        # area must be satisfied
        # l >= w
        # ideally |(l - w)| = 0

        # idea, start w perfect square, increase l until a perfect square is matched

        # find next square increasing l and return first

        l = math.ceil(math.sqrt(area))

        while area % l != 0:
            l += 1
        
        # Once found, calculate W
        w = area // l
        
        return [l, w]
