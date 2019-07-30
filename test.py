class Solution:
    def twoSum(self, nums, target):
        #print("target = ", target)
        nums_len = len(nums)
        nums_count = 0

        for nums_count in range(nums_len):
            x = nums[nums_count:nums_len]
            print("x = ", x)
            #print("nums_len = ", nums_len)
            x_len = len(x)
            for x_count in range(1, x_len, 1):
                #print("x_count = ", x_count)
                my_target = x[0] + x[x_count]

                print("my_target = {}".format(my_target))
                if my_target == target:
                    return [nums_count, x_count+nums_count]

if __name__ == "__main__":
    my_solution = Solution
    my_output = my_solution().twoSum([-1,-2,-3,-4,-5], -8)
    print(my_output)
