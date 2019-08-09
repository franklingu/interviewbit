'''
You are climbing a stair case. It takes n steps to reach to the top.

Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?

Example :

Input : 3
Return : 3

Steps : [1 1 1], [1 2], [2 1]
'''


class Solution:
    # @param A : integer
    # @return an integer
    def climbStairs(self, A):
        def climb(steps, track):
            if steps <= 2:
                return steps
            if steps in track:
                return track[steps]
            return climb(steps - 1, track) + climb(steps - 2, track)

        track = {}
        return climb(A, track)
