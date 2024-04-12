class Solution:
    def trap(self, height: List[int]) -> int:
        # Arrays to store the maximum height to the left and right of each bar
        leftMax = []
        rightMax = []
        result = 0  # Result to store the total amount of trapped water
        max_lh = 0  # Variable to store the maximum height from the left
        max_rh = 0  # Variable to store the maximum height from the right

        # Build the leftMax array
        for i in range(len(height)):
            if i == 0:
                leftMax.append(0)  # There is no left bar for the first element
                max_lh = max(max_lh, height[i])
            else:
                leftMax.append(max_lh)
                max_lh = max(max_lh, height[i])
        
        # Build the rightMax array from the end of the list
        for j in range(len(height)-1, -1, -1):
            if j == len(height)-1:
                rightMax.append(0)  # There is no right bar for the last element
                max_rh = max(max_rh, height[j])
            else:
                rightMax.append(max_rh)
                max_rh = max(max_rh, height[j])
        rightMax.reverse()  # Reverse to match the original list's order

        # Calculate the water trapped above each bar
        for i in range(len(leftMax)):
            # Water trapped on the current bar is the min of max heights minus the height of the bar
            val = min(leftMax[i], rightMax[i]) - height[i]
            result += val if val > 0 else 0  # Only add positive values

        return result