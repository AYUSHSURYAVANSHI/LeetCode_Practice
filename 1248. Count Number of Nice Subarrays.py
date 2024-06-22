class Solution:
    def numberOfSubarrays(self, nums: list[int], k: int) -> int:
        n = len(nums) # Get the length of the input array
        mpp = {0: 1} # Initialize dictionary to store prefix sums
        sum = 0 # Initialize sum to count odd numbers
        ans = 0 # Initialize answer to count subarrays with exactly 'k' odd numbers

        for num in nums: # Iterate through the array
            if num % 2 == 1: # Check if the current number is odd
                sum += 1 # Increment the sum if the number is odd
            diff = sum - k # Calculate the difference needed to form a subarray with 'k' odd numbers
            ans += mpp.get(diff, 0) # Add the count of subarrays found with the required difference
            mpp[sum] = mpp.get(sum, 0) + 1 # Update the dictionary with the current sum

        return ans # Return the total count of subarrays with exactly 'k' odd numbers
    