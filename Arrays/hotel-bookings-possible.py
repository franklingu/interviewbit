'''
A hotel manager has to process N advance bookings of rooms for the next season. His hotel has K rooms. Bookings contain an arrival date and a departure date. He wants to find out whether there are enough rooms in the hotel to satisfy the demand. Write a program that solves this problem in time O(N log N) .

Input:


First list for arrival time of booking.
Second list for departure time of booking.
Third is K which denotes count of rooms.

Output:

A boolean which tells whether its possible to make a booking. 
Return 0/1 for C programs.
O -> No there are not enough rooms for N booking.
1 -> Yes there are enough rooms for N booking.
Example :

Input : 
        Arrivals :   [1 3 5]
        Departures : [2 6 8]
        K : 1

Return : False / 0 

At day = 5, there are 2 guests in the hotel. But I have only one room.
'''

'''
View arrival and departure as stream of events. Event consists of time and is_arriving.
Sort events dnd make sure departure comes before arrival for the same time --
depending on the requirements, we may need to make arrival of the same time
comes first if the duration is inclusive. Maintain a counter and while iterating
from start to end of events, arrival add counter, departure substract counter.
Record the maximum counter ever. If the maximum count is big than K, we cannot
meet the requirement. The maximum is also number of rooms required.
'''


class Solution:
    # @param arrive : list of integers
    # @param depart : list of integers
    # @param K : integer
    # @return a boolean
    def hotel(self, arrive, depart, K):
        allpoints = sorted(
            [(a, True) for a in arrive] + [(a, False) for a in depart]
        )
        curr, prev = 0, None
        for a, is_arriving in allpoints:
            if prev is None:
                prev = a
                curr += 1
                continue
            if a != prev:
                if curr > K:
                    return 0
            if is_arriving:
                curr += 1
            else:
                curr -= 1
            prev = a
        return 1

