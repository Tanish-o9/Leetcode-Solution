class Solution:
    def floodFill(self, image: List[List[int]], r: int, c: int, color: int) -> List[List[int]]:
        
        old_color = image[r][c]

        if old_color == color:
            return image
        
        row = len(image)
        col = len(image[0])

        def dfs(r, c):
            if r < 0 or r >= row or c < 0 or c >= col:
                return

            if old_color != image[r][c]:
                return

            image[r][c] = color

            dfs(r-1, c)
            dfs(r+1, c)
            dfs(r, c-1)
            dfs(r, c+1)

        dfs(r, c)

        return image