'''
There are N children standing in a line. Each child is assigned a rating value.

 You are giving candies to these children subjected to the following requirements:
Each child must have at least one candy.
Children with a higher rating get more candies than their neighbors.
What is the minimum candies you must give?

Sample Input :

Ratings : [1 2]
Sample Output :

3
The candidate with 1 rating gets 1 candy and candidate with rating cannot get 1 candy as
 1 is its neighbor. So rating 2 candidate gets 2 candies. In total, 2+1 = 3 candies need
  to be given out.
'''



class Solution:
    # @param A : list of integers
    # @return an integer
    def candy(self, A):
        res = [1 for _ in xrange(len(A))]
        for i, a in enumerate(A):
            if i == 0:
                continue
            if A[i - 1] == A[i]:
                continue
            elif A[i] > A[i - 1] and res[i] <= res[i - 1]:
                res[i] = res[i - 1] + 1
            else:
                j = i - 1
                while j >= 0 and A[j] > A[j+1] and res[j] <= res[j+1]:
                    res[j]= res[j+1]+1
                    j -= 1
        return sum(res)

    def candy2(self, A):
        if len(A) <= 1:
            return len(A)
        val = [1 for _ in range(len(A))]
        for i in range(1 , len(A)):
            if A[i] > A[i-1]:
                val[i] = max(val[i] , val[i-1] + 1)

        for i in range( len(A)-2 , -1 , -1):
            if A[i] > A[i+1]:
                val[i] = max(val[i] , val[i+1] +1)
        return sum(val)