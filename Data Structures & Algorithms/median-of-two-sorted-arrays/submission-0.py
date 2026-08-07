class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        A = nums1 if len(nums1) <= len(nums2) else nums2
        B = nums2 if len(nums1) <= len(nums2) else nums1
        total = len(nums1) + len(nums2)
        half = total // 2

        lo, hi = 0, len(A) - 1
        while True:
            midA = (lo + hi) // 2
            midB = half - midA - 2

            leftA = A[midA] if midA >= 0 else float("-inf")
            rightA = A[midA + 1] if (midA + 1) < len(A) else float("inf")
            leftB = B[midB] if midB >= 0 else float("-inf")
            rightB = B[midB + 1] if (midB + 1) < len(B) else float("inf")

            if leftA <= rightB and leftB <= rightA:
                if total % 2:
                    return min(rightA, rightB)
                return (max(leftA, leftB) + min(rightA, rightB)) / 2
            elif leftA > rightB:
                hi = midA - 1
            else:
                lo = midA + 1
