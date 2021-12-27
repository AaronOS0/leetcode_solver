#!/usr/bin/env python

"""
Description: Activity selection to reach the maximum number of activities
args:
    activities: time[start, end) in a list
return:
    plan: the activity plan
"""


class Solution:
    def activity_selection(self, activities: list[tuple]) -> list[tuple]:
        # sort activities by the end time; the activity that end earlier belong to the optimized solution
        activities.sort(key=lambda x: x[1])
        plan = [activities[0]]
        for i in range(1, len(activities)):
            # the current start time >= the last activity end time of plan
            if activities[i][0] >= plan[-1][1]:
                plan.append(activities[i])
        return plan


activities = [(1, 4), (3, 5), (0, 6), (5, 7), (3, 9), (5, 9), (6, 10), (8, 11), (8, 12), (2, 14), (12, 16)]
res = Solution().activity_selection(activities)
print(res)
