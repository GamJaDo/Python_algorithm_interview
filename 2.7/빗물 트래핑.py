def trap(height):
    if not height:
        return 0

    volume = 0
    left, right = 0, len(height) - 1

    max_left, max_right = height[left], height[right]

    while left < right:
        max_left = max(max_left, height[left])
        max_right = max(max_right, height[right])

        if max_left < max_right:
            volume += max_left - height[left]
            left += 1
        else:
            volume += max_right - height[right]
            right -= 1

    return volume



height = [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]

print(trap(height))
