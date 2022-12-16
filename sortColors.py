class MySolution:
    def sortColors(self, nums):
        """
        Do not return anything, modify nums in-place instead.
        """
        count = {0: 0, 1: 0, 2: 0}
        for n in nums:
            count[n] += 1

        for i in range(len(nums)):
            if count[0]:
                nums[i] = 0
                count[0] -= 1
            elif count[1]:
                nums[i] = 1
                count[1] -= 1
            else:
                nums[i] = 2
                count[2] -= 1
            
                
        
def sortColors(self, nums):
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
