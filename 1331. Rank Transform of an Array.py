<<<<<<< HEAD
class Solution:
    def arrayRankTransform(self, arr: List[int]) -> List[int]:
        value_to_rank = {}  # Dictionary to store value-to-rank mapping
        sorted_unique_numbers = sorted(list(set(arr)))  # Remove duplicates and sort unique elements
        
        # Assign ranks to sorted unique elements
        for index in range(len(sorted_unique_numbers)): 
            value_to_rank[sorted_unique_numbers[index]] = index + 1
          
        # Replace each element in the original array with its rank
        for index in range(len(arr)): 
            arr[index] = value_to_rank[arr[index]]
        
=======
class Solution:
    def arrayRankTransform(self, arr: List[int]) -> List[int]:
        value_to_rank = {}  # Dictionary to store value-to-rank mapping
        sorted_unique_numbers = sorted(list(set(arr)))  # Remove duplicates and sort unique elements
        
        # Assign ranks to sorted unique elements
        for index in range(len(sorted_unique_numbers)): 
            value_to_rank[sorted_unique_numbers[index]] = index + 1
          
        # Replace each element in the original array with its rank
        for index in range(len(arr)): 
            arr[index] = value_to_rank[arr[index]]
        
>>>>>>> 7b6ba8e5995f96beee23a68d301843f134e054cf
        return arr  # Return the updated array