def reverse(temp):
    left = 0
    right = len(temp)-1

    while left < right:
        temp[left], temp[right] = temp[right], temp[left]

        left += 1
        right -= 1

    print(temp)
    
temp = list(input())
reverse(temp)

"""
temp = list(input())
temp.reverse()
print(temp)
"""
