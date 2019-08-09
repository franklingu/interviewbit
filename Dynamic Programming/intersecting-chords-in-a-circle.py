'''
Given a number N, return number of ways you can draw N chords in a circle with 2*N points such that no 2 chords intersect.
Two ways are different if there exists a chord which is present in one way and not in other.

For example,

N=2
If points are numbered 1 to 4 in clockwise direction, then different ways to draw chords are:
{(1-2), (3-4)} and {(1-4), (2-3)}

So, we return 2.
Notes:

1 ≤ N ≤ 1000
Return answer modulo 109+7.
'''

'''
1. All points on the circle are equal. We use point 1 to analyze.
2. For example 1 in 1 to 6, 1 can be connected with 2, or 4 or 6. For 2, there are two
subsets divided by that: 0 points and 4 points, there are 2 ways to dividing 4 points
which is obvious -- same thing for 1 - 6; for 1 - 4, we can get 2 points on each subsets.
In total we have 1 * 2 + 1 * 1 + 1 * 2.
3. And back to All points are equal -- if we do the same thing for 2 for example, we
will get all the duplicates.

If we do for 8 points, the idea is much similar.
'''



class Solution:
    # @param A : integer
    # @return an integer
    def chordCnt(self, A):
        if A == 0:
            return 0
        dp = [0] * (A + 1)
        for i in range(A + 1):
            if i == 0:
                dp[i] = 1
            elif i == 1:
                dp[i] = 1
            else:
                for j in range(0, i):
                    dp[i] += dp[i - j - 1] * dp[j]
        return dp[-1] % 1000000007
