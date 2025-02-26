from typing import List

class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:

        # return True if "a" < "c" else False  #python could directly compare letters based on their alphabetical order! 

        left, right = 0, len(letters) - 1
        
        while left <= right:
            mid = (left + right) // 2
            if letters[mid] > target:
                right = mid - 1
            else:
                left = mid + 1  # Move right to find a greater letter
        
        # If no greater letter is found, return the first letter (circular array behavior)
        return letters[left] if left < len(letters) else letters[0]
