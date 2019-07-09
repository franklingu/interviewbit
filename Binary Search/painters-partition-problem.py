'''
You have to paint N boards of length {A0, A1, A2, A3 … AN-1}. There are K painters available and you are also given how much time a painter takes to paint 1 unit of board. You have to get this job done as soon as possible under the constraints that any painter will only paint contiguous sections of board.

2 painters cannot share a board to paint. That is to say, a board
cannot be painted partially by one painter, and partially by another.
A painter will only paint contiguous boards. Which means a
configuration where painter 1 paints board 1 and 3 but not 2 is
invalid.
Return the ans % 10000003

Input :
K : Number of painters
T : Time taken by painter to paint 1 unit of board
L : A List which will represent length of each board

Output:
     return minimum time to paint all boards % 10000003
Example

Input : 
  K : 2
  T : 5
  L : [1, 10]
Output : 50
'''

'''
What is the fastest solution in theory? Each worker is responsible for 1 board
and the time taken is max(C)
What is the slowest solution in theory? Only one worker and the time is sum(C)

Now we do binary search to find the smallest possible time with A workers.
'''


class Solution:
    # @param A : integer
    # @param B : integer
    # @param C : list of integers
    # @return an integer
    def paint(self, A, B, C):
        def requiredWorkers(arr, target):
            total = 0
            workers = 1
            for a in arr:
                total += a
                if total > target:
                    total = a
                    workers += 1
            return workers
            
        low, high = max(C), sum(C)
        while low < high:
            mid = (high + low) / 2
            num = requiredWorkers(C, mid)
            if num <= A:
                high = mid
            else:
                low = mid + 1
        return low * B % 10000003
