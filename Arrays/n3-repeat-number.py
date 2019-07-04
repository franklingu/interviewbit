'''
You’re given a read only array of n integers. Find out if any integer occurs more than n/3 times in the array in linear time and constant additional space.

If so, return the integer. If not, return -1.

If there are multiple solutions, return any one.

Example :

Input : [1 2 3 1 1]
Output : 1 
1 occurs 3 times which is more than 5/3 times.
'''

'''
If try to find the element with more than half of occurrances, we try to guess
one element. Now we try to guess two elements.
'''


class Solution:
    # @param A : tuple of integers
    # @return an integer
    def repeatedNumber(self, A):
        first, second = None, None
        count1, count2 = 0, 0
        for a in A:
            if a == first:
                count1 += 1
            elif a == second:
                count2 += 1
            elif count1 == 0:
                first = a
                count1 += 1
            elif count2 == 0:
                second = a
                count2 += 1
            else:
                count1 -= 1
                count2 -= 1
        count1, count2 = 0, 0
        for a in A:
            if a == first:
                count1 += 1
            elif a == second:
                count2 += 1
        if count1 > len(A) / 3:
            return first
        if count2 > len(A) / 3:
            return second
        return -1
