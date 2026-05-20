class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        nums1.sort()
        nums2.sort()

        i = 0
        p = 0
        nlist = []

        while i < len(nums1) and p < len(nums2):
            if nums1[i] == nums2[p]:
                if not nlist or nlist[-1] != nums1[i]:
                    nlist.append(nums1[i])
                i += 1
                p += 1

            elif nums1[i] < nums2[p]:
                i += 1

            else:
                p += 1

        return nlist