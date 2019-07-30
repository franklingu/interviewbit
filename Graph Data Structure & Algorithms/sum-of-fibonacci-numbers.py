'''
How many minimum numbers from fibonacci series are required such that sum of numbers should be equal to a given Number N?
Note : repetition of number is allowed.

Example:

N = 4
Fibonacci numbers : 1 1 2 3 5 .... so on
here 2 + 2 = 4
so minimum numbers will be 2
'''


class Solution:
    # @param A : integer
    # @return an integer
    def fibsum(self, A):
        def build_fib(A):
            res = [1, 2]
            while res[-1] + res[-2] <= A:
                res.append(res[-1] + res[-2])
            return res

        def find_min(A, arr, end):
            # print(A, end)
            if end < 0:
                return 0
            elif A == arr[end]:
                return 1
            target = A - arr[end]
            start = 0
            while start < end:
                mid = (start + end) / 2
                if arr[mid] == target:
                    return 2
                elif arr[mid] > target:
                    end = mid - 1
                else:
                    start = mid + 1
            if arr[end] > target:
                end -= 1
            return find_min(target, arr, end) + 1

        if A <= 2:
            return 1
        arr = build_fib(A)
        return find_min(A, arr, len(arr) - 1)

    def fibsum2(self, A):
        from bisect import bisect_right
        num1 = 1
        num2 = 1
        fib_list = [num1, num2]

        # Generates Fib numbers less than or equal to A
        while num1 < A:
            num1, num2 = num2, num1
            num1 += num2
            fib_list.append(num1)

        # Checks if last fib number generated is A
        if fib_list[-1] == A:
            return 1

        # Greedily add the highest values
        cur_sum = 0
        num_ele = 0
        while cur_sum != A:
            # bisect_right efficiently finds the index with value greater than (A-cur_sum)
            ptr = bisect_right(fib_list, A-cur_sum)
            cur_sum += fib_list[ptr-1]
            num_ele += 1

        return num_ele
