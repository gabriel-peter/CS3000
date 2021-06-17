n = 4
x = [0, 1, 10, 10, 1]
d = [0, 1, 2, 4, 8]
M = [0, min(d[1],x[1])] + [None] * (n-1)

# This function build the dp table getting 
# the max asteroid mass that can destroyed
# in `n` years
def OPT(n):
    for i in range(2,n+1):
        # subproblems = []
        best = 0
        for j in range(1, i+1):
            y = min(x[i], d[j]) + M[i-j]
            if y >= best:
                best = y
        M[i] = best

OPT(n)
print(M) # [0, 1, 2, 4, 5]

# This function retrieves the schedule
# to achieve the max asteroid destruction within
# `n` years
def FindSched(M, n):
    if n == 0: return ''
    else:
        for j in range(1, n+1):
            if M[n] - min(x[n], d[j]) == M[n-j]:
                return FindSched(M, n-j) + f'{n} '
        return FindSched(M, n-1)

print(FindSched(M, n)) # 3 4