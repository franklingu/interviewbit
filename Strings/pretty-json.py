'''
Pretty print a json object using proper indentation.

Every inner brace should increase one indentation to the following lines.
Every close brace should decrease one indentation to the same line and the following lines.
The indents can be increased with an additional ‘\t’
Example 1:

Input : {A:"B",C:{D:"E",F:{G:"H",I:"J"}}}
Output :
{
    A:"B",
    C:
    {
        D:"E",
        F:
        {
            G:"H",
            I:"J"
        }
    }
}
Example 2:

Input : ["foo", {"bar":["baz",null,1.0,2]}]
Output :
[
    "foo",
    {
        "bar":
        [
            "baz",
            null,
            1.0,
            2
        ]
    }
]
[] and {} are only acceptable braces in this case.

Assume for this problem that space characters can be done away with.

Your solution should return a list of strings, where each entry corresponds to a single line. The strings should not have “\n” character in them.
'''


class Solution:
    # @param A : string
    # @return a list of strings
    def prettyJSON(self, A):
        ret = []
        level = 0
        stack = []
        for i, c in enumerate(A):
            if c == ' ':
                continue
            elif c == '[':
                if ret and ret[-1] and ret[-1][-1] and ret[-1][-1][-1] == '\t':
                    ret[-1].append(c)
                else:
                    ret.append(['\t' * level + c])
                stack.append(c)
                level += 1
                ret.append(['\t' * level])
            elif c == ']':
                del stack[-1]
                level -= 1
                ret.append(['\t' * level + c])
            elif c == '{':
                if ret and ret[-1] and ret[-1][-1] and ret[-1][-1][-1] == '\t':
                    ret[-1].append(c)
                else:
                    ret.append(['\t' * level + c])
                stack.append(c)
                level += 1
                ret.append(['\t' * level])
            elif c == '}':
                del stack[-1]
                level -= 1
                ret.append(['\t' * level + c])
            elif c == '"':
                if not ret:
                    ret.append([])
                ret[-1].append(c)
                if stack and stack[-1] != c:
                    stack.append(c)
                else:
                    del stack[-1]
            elif c == ',':
                if stack and stack[-1] != '"':
                    ret[-1].append(c)
                    ret.append(['\t' * level])
                else:
                    ret[-1].append(c)
            else:
                ret[-1].append(c)
        return [''.join(e) for e in ret]
