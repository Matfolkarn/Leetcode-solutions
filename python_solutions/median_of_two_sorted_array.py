class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        total = len(nums1) + len(nums2)
        half = total //2

        if len(nums1) < len(nums2):
            A, B = nums1, nums2
        else:
            A, B = nums2, nums1

        l, r = 0, len(A) - 1
        while True:
            m = (l + r) // 2
            m_b = half - m - 2

            lp_a = A[m] if m >= 0 else float("-infinity")
            rp_a = A[m+1] if (m + 1) < len(A) else float("infinity")
            
            lp_b = B[m_b] if m_b >= 0 else float("-infinity")
            rp_b = B[m_b + 1] if (m_b+1) < len(B) else float("infinity")


            if lp_a <= rp_b and lp_b <= rp_a:
                if total % 2:
                    return min(rp_a,rp_b)
                else:
                    return (max(lp_a,lp_b) + min(rp_a , rp_b ) )/ 2
            elif lp_a > rp_b:
                r = m - 1
            else:
                l = m + 1
