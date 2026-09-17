import random

def partition(nums, x, n):
    i, j, k = 0, 0, 0
    while k < n:
        if nums[k] == x:
            temp = nums[j]
            nums[j] = nums[k]
            nums[k] = temp
            j += 1
        elif nums[k] < x:
            temp = nums[k]
            nums[k] = nums[j]
            nums[j] = nums[i]
            nums[i] = temp
            j += 1
            i += 1
        k += 1
    
    return [i, j]

def quiksort(nums, n):
    if n == 1 or n == 0: return nums
    x = nums[random.randrange(0, n-1)]
    i, j = partition(nums, x, n)
    temp = quiksort(nums[:i], len(nums[:i]))
    for idx in range(len(temp)):
        nums[idx] = temp[idx]
        
    temp = quiksort(nums[j:], len(nums[j:]))
    for idx in range(len(temp)):
        nums[j+idx] = temp[idx]
    return nums

def main():
    n = int(input())
    nums = list(map(int, input().split()))
    nums = quiksort(nums, n)
    print(" ".join([str(v) for v in nums]))
main()
