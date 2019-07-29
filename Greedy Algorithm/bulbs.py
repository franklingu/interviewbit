'''
N light bulbs are connected by a wire. Each bulb has a switch associated with it, however due to faulty wiring, a switch also changes the state of all the bulbs to the right of current bulb. Given an initial state of all bulbs, find the minimum number of switches you have to press to turn on all the bulbs. You can press the same switch multiple times.

Note : 0 represents the bulb is off and 1 represents the bulb is on.

Example:

Input : [0 1 0 1]
Return : 4

Explanation :
	press switch 0 : [1 0 1 0]
	press switch 1 : [1 1 0 1]
	press switch 2 : [1 1 1 0]
	press switch 3 : [1 1 1 1]
'''

'''
For the current and all on the right, if current is on, move on to next without
anything; if current is not on, switch on current, and all the right ones' on
state will be flipped(in fact all the right ones' state is flipped but it is
same as redefining the on state)
'''


class Solution:
    # @param A : list of integers
    # @return an integer
    def bulbs(self, A):
        count = 0
        on = 1
        for a in A:
            if a != on:
                count += 1
                on = on ^ 1
        return count