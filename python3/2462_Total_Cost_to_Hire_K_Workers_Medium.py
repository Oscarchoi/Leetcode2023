# 2462. Total Cost to Hire K Workers

from queue import PriorityQueue

class Solution:
    def totalCost(self, costs: List[int], k: int, candidates: int) -> int:
        count = 0

        N = len(costs)
        if N < 2 * candidates + k:
            costs.sort()
            return sum(costs[0:k])
        
        front = PriorityQueue()
        front_cursor = candidates - 1
        for cost in costs[0:candidates]:
            front.put(cost)
        
        rear = PriorityQueue()
        rear_cursor = N-candidates
        for cost in costs[N-candidates:N]:
            rear.put(cost)

       
        lhs = front.get()
        rhs = rear.get()
        for i in range(k):
            if lhs <= rhs:
                count += lhs
                front_cursor += 1
                front.put(costs[front_cursor])
                lhs = front.get()
            else:
                count += rhs
                rear_cursor -= 1
                rear.put(costs[rear_cursor])
                rhs = rear.get()
            
        return count