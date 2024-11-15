class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        arrays are sorted in ascending order, merge both into nums1
        nums1= num1 + [0]*len(nums2)

        Test case
            nums1 = [1,2,3,0,0,0] nums2=[2,5,6] || nums1 = [1,2,2,3,5,6]
            nums1 = [1,2,3,0,0,0,0] nums2=[2,5,6,7] || nums1 = [1,2,2,3,5,6,7]
        """

        # Apporach 1: Time O(m+n)

        # In Nums1, move the numbers to the end O(m)
        # nums1 = m + n
        for i in range(m+n-1,n-1,-1):
            nums1[i] = nums1[i-n]


        #  using three pointers, iterate through all values and put them in nums1 O(m+n)
        nums1_pointer = n
        nums2_pointer = 0
        merge_pointer = 0
        while nums1_pointer <m+n or nums2_pointer < n:
            if nums2_pointer==n:
                nums1[merge_pointer] = nums1[nums1_pointer]
                merge_pointer += 1
                nums1_pointer += 1

            elif nums1_pointer == m+n:
                nums1[merge_pointer] = nums2[nums2_pointer]
                merge_pointer += 1
                nums2_pointer += 1

            elif nums1[nums1_pointer] < nums2[nums2_pointer]:
                nums1[merge_pointer] = nums1[nums1_pointer]
                merge_pointer += 1
                nums1_pointer += 1
            else:
                nums1[merge_pointer] = nums2[nums2_pointer]
                merge_pointer += 1
                nums2_pointer += 1


        




        return

