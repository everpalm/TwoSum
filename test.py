class Solution:
    def twoSum(self, nums, target):
        complement={}
        for nums_count in range(len(nums)):
            if (target-nums[nums_count]) not in complement:
                #print("complement =", complement)
                #print(target, "- nums[",nums_count,"] = ", target-nums[nums_count])
                complement[nums[nums_count]]=nums_count
            #print("1. ","complement[",nums[nums_count],"] = ", nums_count)
            else:
                #print(target, "- nums[",nums_count,"] = ", target-nums[nums_count])
                #print("2. ","dic[",target-nums[nums_count],"] = ", nums_count)
                return [complement[target-nums[nums_count]],nums_count]

if __name__ == "__main__":
    my_solution = Solution
    my_output = my_solution().twoSum([1,2,3], 3)
    print(my_output)

