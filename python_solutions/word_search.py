class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        

        x_lim = len(board)
        y_lim = len(board[0])

        def rec(p1, p2,i, used):

            if i >= len(word):
                return True
            if p1 >= len(board) or p2 >= len(board[0]) or p1 < 0 or p2 < 0:
                return False
            if (p1,p2) in used:
                return False
            elif board[p1][p2] == word[i]:
                u = used.copy()
                u.add((p1,p2))
                return rec(p1 +1, p2, i +1,u ) or rec(p1 -1, p2, i + 1, u) or rec(p1, p2+1, i +1, u) or rec(p1, p2-1, i +1, u)

        for i in range(len(board)):
            for y in range(len(board[0])):
                if rec(i,y, 0, set()):
                    return True
                    
        return False
