class Solution:
    def floodFill(
        self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        rows, cols = len(image), len(image[0])
        pixel_color = image[sr][sc]
        print(pixel_color)

        def dfs(r, c, pixel_color):
            if r < 0 or c < 0 or r >= rows or c >= cols:
                return
            if image[r][c] == pixel_color:
                if image[r][c] == color:
                    return
                image[r][c] = color

                dfs(r, c - 1, pixel_color)
                dfs(r, c + 1, pixel_color)
                dfs(r - 1, c, pixel_color)
                dfs(r + 1, c, pixel_color)
            else:
                return

        dfs(sr, sc, pixel_color)
        return image


sol = Solution()
sol.floodFill(image=[[0, 0, 0], [0, 0, 0]], sr=0, sc=0, color=0)
