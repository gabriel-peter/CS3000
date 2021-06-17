n = 6
v = [0,3,5,7,6,13,3,8]
M = [0, v[0]] + [-1] * 6
p = [0,0,1,0,2,1,4,3]
# print(M)
def FindOpt(n):
    # print(M, f'FindOpt({n})')
    if M[n] != -1: 
        return M[n]
    else:
        M[n] = max(FindOpt(n-1), v[n] + FindOpt(p[n]))
        return M[n]

FindOpt(7)

def FindSched(M,n):
    if n == 0: 
        return []
    elif n == 1: 
        return [1]
    elif (v[n] + M[p[n]] > M[n-1]):
        return [n] + FindSched(M, p[n])
    else:
        return FindSched(M,n-1)

for i in range(7, -1, -1):
    print(f'FindSched({i})', FindSched(M,i))