class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        for i in range(len(board)):
            for j in range(len(board[0])):
                if self.dfs(board, word, i, j, 0):
                    return True
        return False
    
    def dfs(self, board: List[List[str]], word: str, i: int, j: int, s: int) -> bool:
        if i < 0 or i == len(board) or j < 0 or j == len(board[0]):
            return False
        if board[i][j] != word[s] or board[i][j] == '*':
            return False
        if s == len(word) - 1:
            return True
        
        cache = board[i][j]
        board[i][j] = '*'
        is_exist = self.dfs(board, word, i + 1, j, s + 1) or \
                   self.dfs(board, word, i - 1, j, s + 1) or \
                   self.dfs(board, word, i, j + 1, s + 1) or \
                   self.dfs(board, word, i, j - 1, s + 1)
        board[i][j] = cache
        
        return is_exist