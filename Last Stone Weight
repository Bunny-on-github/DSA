class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        while len(stones)>1:
            stones.sort()
            if stones[-2] == stones[-1]:
                stones = stones[:-2]
            else:
                x = stones[-1] - stones[-2]
                stones = stones[:-2]
                stones.append(x)
            stones.sort()
        return stones[0] if len(stones) == 1 else 0
        
