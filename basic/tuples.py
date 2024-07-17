nums = (11,22,33)
print(nums[0]) # 11
print(nums[1]) # 22

# nums[1] = 222  # ❌ TypeError: 'tuple' object does not support item assignment

# 一个元素 少见但可以
my_t = (1,)
print(my_t) # (1,)

# 遍历所有元素
for num in nums:
    print(num) # 11 22 33


# 重写 可改
nums = (1, 2, 3)
print(nums) #  (1, 2, 3)