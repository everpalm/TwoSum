class Solution:
    def twoSum(self, nums, target):
        for nums_count in range(len(nums)):
            for x_count in range(nums_count+1, len(nums), 1):
                if target == nums[x_count] + nums[nums_count]:
                    return [nums_count, x_count]

if __name__ == "__main__":
    my_solution = Solution
    my_output = my_solution().twoSum([-1,-2,-3,-4,-5], -8)
    print(my_output)
