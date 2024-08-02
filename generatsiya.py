nums = CustomRange(1, 10)
for num in nums:
    print(num)

class Nums:
    def __init__(self, nums, divisible_num):
        self.nums = nums
        self.divisible_num = divisible_num
        self.index = -1

    def __iter__(self):
        return self

    def __next__(self):
        while self.index < len(self.nums) - 1:
            self.index += 1
            if self.nums[self.index] % self.divisible_num == 0:
                return self.nums[self.index]
        raise StopIteration


num = Nums([1, 2, 3, 4, 5], 5)
for i in num:
    print(i)