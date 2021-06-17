board = [10, 2, 8, 5]
n = len(board)
M = [0] + [None] * (n+1)
M_B = [0, ]

def OPT(l, r, n):
    if n <= 0: return 0
    if n == 1: return board[l]
    if n == 2: 
        return max(board[l]-board[r], board[r]-board[l])
    if M[n] != None: return M[n]
    else:
        M[n] = max(
            board[l] - OPT(l+1, r, n-1),
            board[r] - OPT(l, r-1, n-1))
        return M[n]


OPT(0, n-1, n)
print(M)

