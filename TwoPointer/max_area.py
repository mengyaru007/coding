"""盛最多水的容器"""

def max_area(height):
    n = len(height)
    left, right = 0, n - 1
    area = 0
    while left != right:
        current_area = (right - left) * min(height[left], height[right])
        print(f"当前面积={current_area}")
        area = max(area, current_area)
        if height[left] < height[right]: left += 1
        else: right -= 1
    return area

max_area([1,8,6,2,5,4,8,3,7])