'''You are given a positive integer days representing the total number of days an employee is available for work (starting from day 1). You are also given a 2D array meetings of size n where, meetings[i] = [start_i, end_i] represents the starting and ending days of meeting i (inclusive).

Return the count of days when the employee is available for work but no meetings are scheduled.

Note: The meetings may overlap.

 

Example 1:

Input: days = 10, meetings = [[5,7],[1,3],[9,10]]

Output: 2

Explanation:

There is no meeting scheduled on the 4th and 8th days.

Example 2:

Input: days = 5, meetings = [[2,4],[1,3]]

Output: 1

Explanation:

There is no meeting scheduled on the 5th day.

Example 3:

Input: days = 6, meetings = [[1,6]]

Output: 0

Explanation:

Meetings are scheduled for all working days.

 

Constraints:

1 <= days <= 109
1 <= meetings.length <= 105
meetings[i].length == 2
1 <= meetings[i][0] <= meetings[i][1] <= days'''

class Solution:
    def countDays(self, days: int, meetings: List[List[int]]) -> int:
        meetings.sort(key=lambda x: x[0])
        print(meetings)
        count = meetings[0][0]-1
        prev_last = meetings[0][1]

        for i in range(1, len(meetings)):
            if(meetings[i][0] <= prev_last):
                prev_last = max(prev_last, meetings[i][1])
            else:
                free_day = meetings[i][0] - prev_last - 1
                count += free_day
                prev_last = meetings[i][1]
        count += days - prev_last
        return count



    def countDaysBrute(self, days: int, meetings: List[List[int]]) -> int:
        free_days = [i+1 for i in range(days)]
        # print("free_days", free_days)
        for row in meetings:
            for i in range(row[0], row[1]+1):
                if i in free_days:
                    free_days[i-1]=0
        # print("free_days",free_days)
        count = 0
        for i in free_days:
            if (i != 0):
                count+=1
        return count
        


