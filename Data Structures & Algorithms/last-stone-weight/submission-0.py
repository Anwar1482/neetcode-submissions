import heapq
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        for i in range(len(stones)):
            stones[i] = -stones[i]
        heapq.heapify(stones)
        while len(stones) > 1:
            val = (heapq.heappop(stones)-heapq.heappop(stones))
            if val !=0:
                heapq.heappush(stones, val)
        if len(stones) == 0:
            return 0
        return -stones[0]
