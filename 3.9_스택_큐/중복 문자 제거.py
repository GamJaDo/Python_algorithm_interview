import collections

"""
def removeDuplicateLetters(s):

    for char in sorted(set(s)):
        suffix = s[s.index(char):]
        
        if set(s) == set(suffix):
            
            return char + removeDuplicateLetters(suffix.replace(char, ''))

    return ''
"""

def removeDuplicateLetters(s):
    counter, seen, stack = collections.Counter(s), set(), []
    #print(counter)
    for char in s:
        counter[char] -= 1
        if char in stack:
            continue

        while stack and char<stack[-1] and counter[stack[-1]]>0:
            #seen.remove(stack.pop())
            stack.pop()
        stack.append(char)
        #seen.add(char)

    return ''.join(stack)

s = "ecbac"
print(removeDuplicateLetters(s))
