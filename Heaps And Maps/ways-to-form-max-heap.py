'''
Max Heap is a special kind of complete binary tree in which for every node the value present in that node is greater than the value present in it’s children nodes. If you want to know more about Heaps, please visit this link

So now the problem statement for this question is:

How many distinct Max Heap can be made from n distinct integers

In short, you have to ensure the following properties for the max heap :

Heap has to be a complete binary tree ( A complete binary tree is a binary tree in which every level, except possibly the last, is completely filled, and all nodes are as far left as possible. )
Every node is greater than all its children
Let us take an example of 4 distinct integers. Without loss of generality let us take 1 2 3 4 as our 4 distinct integers

Following are the possible max heaps from these 4 numbers :

         4
       /  \
      3   2
     /
    1
         4
       /  \
      2   3
     /
    1
        4
       /  \
      3   1
     /
    2
These are the only possible 3 distinct max heaps possible for 4 distinct elements.

Implement the below function to return the number of distinct Max Heaps that is possible from n distinct elements.

As the final answer can be very large output your answer modulo 1000000007

Input Constraints : n <= 100

 NOTE: Note that even though constraints are mentioned for this problem, for most problems on InterviewBit, constraints are intentionally left out. In real interviews, the interviewer might not disclose constraints and ask you to do the best you can do.
'''


class Solution:
    # @param A : integer
    # @return an integer
    def solve(self, A):
        def choose(n, k, nck):
            if k > n:
                return 0
            if n <= 1:
                return 1
            if k == 0:
                return 1
            if (n, k) in nck:
                return nck[(n, k)]
            ans = choose(n - 1, k - 1, nck) + choose(n - 1, k, nck)
            nck[(n, k)] = ans
            return ans

        def calculate(A, track, nck, acc):
            if A in track:
                return track[A]
            elif A <= 2:
                return 1
            elif A == 3:
                return 2
            val = A - 1
            right = (1 << (acc - 1)) - 1
            left = val - right
            if left < right:
                right = (1 << (acc - 2)) - 1
                left = val - right
            if left - right > (1 << (acc - 2)):
                left = right + (1 << (acc - 2))
                right = val - left
            # print(A, left, right, acc)
            ret = choose(val, left, nck)
            left_ret = calculate(left, track, nck, acc - 1)
            right_ret = calculate(right, track, nck, acc - 1)
            ret = ret * left_ret * right_ret
            track[A] = ret
            return ret

        track = {}
        nck = {}
        n = A - 1
        acc = 0
        while n != 0:
            n = n >> 1
            acc += 1
        return calculate(A, track, nck, acc) % 1000000007


MOD = 10**9+7

class Solution2:
    # @param A : integer
    # @return an integer

    def comb(self,r,n) :
        if 2*r > n :
            return self.comb(n-r,n)
        c = 1
        for i in range(r) :
            c = c*(n-i)//(i+1)
        return c

    def solve(self, A):
        ans,h = [1,1], 0
        for n in range(2,A+1) :
            if 2<<h <= n :
                h += 1
            m = n-(1<<h)+1
            l = (1<<(h-1))-1 + min(m,1<<(h-1))
            r = (1<<(h-1))-1 + max(0,m-(1<<(h-1)))
            ans.append((self.comb(l,n-1)*ans[l]*ans[r])%MOD)
        return ans[A]
