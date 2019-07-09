'''
Validate if a given string is numeric.

Examples:

"0" => true
" 0.1 " => true
"abc" => false
"1 a" => false
"2e10" => true
Return 0 / 1 ( 0 for false, 1 for true ) for this problem

Clarify the question using “See Expected Output”

Is 1u ( which may be a representation for unsigned integers valid?
For this problem, no.
Is 0.1e10 valid?
Yes
-01.1e-10?
Yes
Hexadecimal numbers like 0xFF?
Not for the purpose of this problem
3. (. not followed by a digit)?
No
Can exponent have decimal numbers? 3e0.1?
Not for this problem.
Is 1f ( floating point number with f as prefix ) valid?
Not for this problem.
How about 1000LL or 1000L ( C++ representation for long and long long numbers )?
Not for this problem.
How about integers preceded by 00 or 0? like 008?
Yes for this problem
'''


class Solution:
    # @param A : string
    # @return an integer
    def isNumber(self, A):
        seen_parts = False
        seen_sign = False
        seen_nums = False
        seen_e = False
        should_follow = False
        skip_next = False
        A = A.strip()
        if len(A) < 1:
            return 0
        for i, e in enumerate(A):
            if skip_next:
                skip_next = False
                continue
            if should_follow and not (ord('0') <= ord(e) <= ord('9')):
                return 0
            if e == '-':
                if not seen_sign:
                    seen_sign = True
                    seen_parts = True
                    should_follow = True
                    continue
                else:
                    return 0
            elif e == '+':
                if not seen_sign:
                    seen_sign = True
                    seen_parts = True
                    should_follow = True
                    continue
                else:
                    return 0
            elif ord('0') <= ord(e) <= ord('9'):
                seen_parts = True
                seen_nums = True
                should_follow = False
            elif e == '.':
                if seen_e:
                    return 0
                should_follow = True
                continue
            elif e == 'e':
                if not seen_nums:
                    return 0
                seen_e = True
                if i >= len(A) - 1:
                    return 0
                if A[i + 1] == '-' or A[i + 1] == '+':
                    skip_next = True
                should_follow = True
            else:
                return 0
        if should_follow:
            return 0
        return 1
