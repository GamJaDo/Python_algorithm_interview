import collections

def Palindrome(t):
    dq = collections.deque()

    for i in t:
        if i.isalnum():
            dq.append(i.lower())

    while len(dq)>1:
        if dq.popleft() != dq.pop():
            return False

    return True

temp = input()
print(Palindrome(temp))
