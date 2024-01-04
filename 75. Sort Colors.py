class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        red, white, blue = 0, 0, len(nums)-1
    
        while white <= blue:
            if nums[white] == 0:
                nums[red], nums[white] = nums[white], nums[red]
                white += 1
                red += 1
            elif nums[white] == 1:
                white += 1
            else:
                nums[white], nums[blue] = nums[blue], nums[white]
                blue -= 1
        # p0 = curr = 0
        # p2 = len(nums) -1 
        # mid = 0
        # while curr <= p2:
        #     if nums[curr] == 0:
        #         ## Swap nums[curr] and nums[0]
        #         nums[p0],nums[curr] == nums[curr],nums[p0]
        #         p0 +=1
        #         curr += 1
        #     elif nums[mid] == 1:
        #         mid += 1
            
        #     else:
        #         nums[curr], nums[p2] = nums[p2] , nums[curr]
        #         p2 -= 1
        # return nums