class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        
        m = len(matrix)
        n = len(matrix[0])

        bot = 0
        top = m*n
        
        found = False
        while not found:
            current = (top + bot)//2
            current_n = current%n 
            current_m = (current) // n

            current_value = matrix[current_m][current_n]

            if current_value == target:
                return True
            elif top - bot <= 1:
                return False
            elif current_value > target:
                top = current
            elif current_value < target:
                bot = current
