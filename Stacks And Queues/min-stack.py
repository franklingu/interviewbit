'''
Design a stack that supports push, pop, top, and retrieving the minimum element in constant time.

push(x) – Push element x onto stack.
pop() – Removes the element on top of the stack.
top() – Get the top element.
getMin() – Retrieve the minimum element in the stack.
Note that all the operations have to be constant time operations.

Questions to ask the interviewer :

Q: What should getMin() do on empty stack?
A: In this case, return -1.

Q: What should pop do on empty stack?
A: In this case, nothing.

Q: What should top() do on empty stack?
A: In this case, return -1
 NOTE : If you are using your own declared global variables, make sure to clear them out in the constructor.
'''


class MinStack:
    def __init__(self):
        self.stk = []
        self.mstk = []

    # @param x, an integer
    def push(self, x):
        self.stk.append(x)
        if not self.mstk:
            self.mstk.append(x)
        elif x <= self.mstk[-1]:
            self.mstk.append(x)

    # @return nothing
    def pop(self):
        if not self.stk:
            return
        val = self.stk.pop()
        if self.mstk and val == self.mstk[-1]:
            self.mstk.pop()
        return val

    # @return an integer
    def top(self):
        if not self.stk:
            return -1
        return self.stk[-1]

    # @return an integer
    def getMin(self):
        if not self.mstk:
            return -1
        return self.mstk[-1]
