class MySolution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        
        read_vals = set()
        for i in nums:
            if i in read_vals:
                return True
            else:
                read_vals.add(i)
                
        return False

    