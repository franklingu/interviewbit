'''
Given two sorted integer arrays A and B, merge B into A as one sorted array.

 Note: You have to modify the array A to contain the merge of A and B. Do not output anything in your code.
TIP: C users, please malloc the result into a new array and return the result.
If the number of elements initialized in A and B are m and n respectively, the resulting size of array A after your code is executed should be m + n

Example :

Input :
         A : [1 5 8]
         B : [6 9]

Modified A : [1 5 6 8 9]
'''


class Solution:
    # @param A : list of integers
    # @param B : list of integers
    def merge(self, A, B):
        i, j = 0, 0
        ret = []
        while i < len(A) and j < len(B):
            a, b = A[i], B[j]
            if a < b:
                ret.append(a)
                i += 1
            else:
                ret.append(b)
                j += 1
        while i < len(A):
            a = A[i]
            ret.append(a)
            i += 1
        while j < len(B):
            b = B[j]
            ret.append(b)
            j += 1
        print(' '.join([str(e) for e in ret]) + ' ')
