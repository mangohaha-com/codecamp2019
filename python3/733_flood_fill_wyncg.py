class Solution:
    def floodFill(self, image, sr, sc, newColor):
        """
        :type image: List[List[int]]
        :type sr: int
        :type sc: int
        :type newColor: int
        :rtype: List[List[int]]
        """
        if len(image) == 0:
            return image
        
        originalColor = image[sr][sc]
        if newColor == originalColor:
            return image
        
        totalRow = len(image)
        totalCol = len(image[0])
        
        def paint(row, col):
            """
            :type row: int
            :type column: int
            """
            if image[row][col] == originalColor:
                image[row][col] = newColor
                if row - 1 >= 0:
                    paint(row - 1, col)
                if row + 1 < totalRow:
                    paint(row + 1, col)
                if col - 1 >= 0:
                    paint(row, col - 1)
                if col + 1 < totalCol:
                    paint(row, col + 1)
                    
        paint(sr, sc)
        
        return image