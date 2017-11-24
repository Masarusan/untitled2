def average(*nums):
    sum = 0
    for n in nums:
        sum+=n
    return sum / len(nums)
print(average(1,10,100))