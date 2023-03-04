'''

2444. Count Subarrays With Fixed Bounds

You are given an integer array nums and two integers minK and maxK.
A fixed-bound subarray of nums is a subarray that satisfies the following conditions:
The minimum value in the subarray is equal to minK.
The maximum value in the subarray is equal to maxK.
Return the number of fixed-bound subarrays.
A subarray is a contiguous part of an array.

Example 1:
Input: nums = [1,3,5,2,7,5], minK = 1, maxK = 5
Output: 2
Explanation: The fixed-bound subarrays are [1,3,5] and [1,3,5,2].

Example 2:
Input: nums = [1,1,1,1], minK = 1, maxK = 1
Output: 10
Explanation: Every subarray of nums is a fixed-bound subarray. There are 10 possible subarrays.

'''

class Solution:
    def countSubarrays(self, nums: List[int], minK: int, maxK: int) -> int:
        out, mn, mx = -1, -1, -1
        res = 0
        for i, n in enumerate(nums):
            if n < minK or n > maxK:
                out = i
                continue
            if n == minK:
                mn = i
            if n == maxK:
                mx = i
            if min(mn,mx)-out >= 0:
                res += (min(mn,mx)-out)

        return res