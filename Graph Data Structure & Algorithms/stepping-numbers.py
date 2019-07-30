'''
Given N and M find all stepping numbers in range N to M

The stepping number:

A number is called as a stepping number if the adjacent digits have a difference of 1.
e.g 123 is stepping number, but 358 is not a stepping number

Example:

N = 10, M = 20
all stepping numbers are 10 , 12
Return the numbers in sorted order.
'''

class Solution:
    # @param A : integer
    # @param B : integer
    # @return a list of integers
    def stepnum(self, A, B):
        ret = set()
        visited = set()
        stack = list(range(10))
        while stack:
            curr = stack.pop()
            if A <= curr <= B:
                ret.add(curr)
            elif curr > B:
                continue
            last_digit = curr % 10
            targets = []
            if last_digit < 9:
                targets.append(curr * 10 + last_digit + 1)
            if last_digit > 0:
                targets.append(curr * 10 + last_digit - 1)
            for target in targets:
                if target not in visited:
                    stack.append(target)
        return sorted(ret)
