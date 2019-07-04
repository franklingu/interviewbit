'''
You are given an array A containing N integers. The special product of each ith integer in this array is defined as the product of the following:<ul>

LeftSpecialValue: For an index i, it is defined as the index j such that A[j]>A[i] (i>j). If multiple A[j]’s are present in multiple positions, the LeftSpecialValue is the maximum value of j. 

RightSpecialValue: For an index i, it is defined as the index j such that A[j]>A[i] (j>i). If multiple A[j]s are present in multiple positions, the RightSpecialValue is the minimum value of j.

Write a program to find the maximum special product of any integer in the array.

Input: You will receive array of integers as argument to function.

Return: Maximum special product of any integer in the array modulo 1000000007.

Note: If j does not exist, the LeftSpecialValue and RightSpecialValue are considered to be 0.

Constraints 1 <= N <= 10^5 1 <= A[i] <= 10^9
'''

'''
Use monotonic stack -- a stack in which elements are in order -- to find LeftSpecialValue and
RightSpecialValue. In this case the stack is decreasing, for any element, if the top of stack
is bigger than it, LeftSpecialValue is just the top; if top of stack is smaller, pop and compare
again. If some element A is popped, it is because a bigger number B right of it has been visited and
in stack. So elements after the bigger number B will never need to use A anymore as A < B.

Same thing for RightSpecialValue.
'''


class Solution:
    # @param A : list of integers
    # @return an integer
    def maxSpecialProduct(self, A):
        if len(A) < 3:
            return 0
        left, right = [], []
        stk = []
        for i, a in enumerate(A):
            while len(stk) > 0:
                val = A[stk[-1]]
                if val > a:
                    left.append(stk[-1])
                    break
                else:
                    stk.pop()
            if len(stk) == 0:
                left.append(0)
            stk.append(i)
        stk = []
        for i, a in enumerate(reversed(A)):
            while len(stk) > 0:
                val = A[stk[-1]]
                if val > a:
                    right.append(stk[-1])
                    break
                else:
                    stk.pop()
            if len(stk) == 0:
                right.append(0)
            stk.append(i)
        right = right[::-1]
        mm = 0
        print(left, right)
        for i, a in enumerate(A):
            mm = max(mm, left[i] * right[i])
        return mm % 1000000007
