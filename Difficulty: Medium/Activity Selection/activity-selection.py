class Solution:
    def activitySelection(self, start: list[int], finish: list[int]) -> int:
        # Combine start and finish times and sort by finish time
        activities = sorted(zip(start, finish), key=lambda x: x[1])
        
        count = 0
        last_finish = -1
        
        for s, f in activities:
            # If the current activity starts strictly after the last selected one finishes
            if s > last_finish:
                count += 1
                last_finish = f
                
        return count