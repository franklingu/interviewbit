'''
Evaluate the value of an arithmetic expression in Reverse Polish Notation.

Valid operators are +, -, *, /. Each operand may be an integer or another expression.

Examples:

  ["2", "1", "+", "3", "*"] -> ((2 + 1) * 3) -> 9
  ["4", "13", "5", "/", "+"] -> (4 + (13 / 5)) -> 6
'''


class Solution:
    # @param A : list of strings
    # @return an integer
    def evalRPN(self, A):
        def calculateResult(r1, r2, op):
            if op == '+':
                return r2 + r1
            elif op == '-':
                return r2 - r1
            elif op == '*':
                return r2 * r1
            else:
                return r2 / r1

        stack = []
        ops = set(('+', '-', '*', '/'))
        for e in A:
            if e in ops:
                r1 = stack.pop()
                r2 = stack.pop()
                stack.append(calculateResult(r1, r2, e))
            else:
                stack.append(int(e))
        return stack.pop()
