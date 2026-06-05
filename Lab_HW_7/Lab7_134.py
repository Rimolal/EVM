from typing import List
class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        n = len(gas)
        final_gas = 0
        final_cost = 0
        tank = 0
        start = 0
        for i in range(n):
            final_gas += gas[i]
            final_cost += cost[i]
            tank += gas[i] - cost[i]
            if tank < 0:
                start = i + 1
                tank = 0
        return start if final_gas >= final_cost else -1