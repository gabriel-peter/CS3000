# t1+t3+t2= 5 + 7 + 2 = 14, 
# t1+t3= 5 + 7 = 12,
# t1+t3+t2+t4= 5 + 7 + 2 + 4 = 18
# 5∗1 + 14∗3 + 12∗2 + 18∗2 = 5 + 42 + 24 + 36 = 107.


# w1=1, w2=3, w3= 2, w4= 2. 
# t1= 5, t2= 2, t3= 7, t4= 4
n = 4
w = [1,3,2,2]
t = [5,2,7,4]

# TODO make Optimal S here 
# 84 is best so far!!!
# i = (i, t_i * w_i)
# def OptS(w, t):
#     w_ordered = sorted([(i, y+(t[i])) for i, y in enumerate(w)], key=lambda x: x[1])
#     w_idxs = [x[0]+1 for x in w_ordered]
#     return w_idxs

def OptS(w, t):
    X = [[i, t[i], w[i]] for i in range(n)]
    S = []
    print(X)
    while len(S) < len(X):
        max_w = X[0][2]
        sub_sols = [X[0]]
        for i in range(n):
            if i+1 in S: continue
            x = X[i] 
            w = x[2]
            if w >= max_w:
                if w == max_w:
                    sub_sols.append(x)
                else:
                    max_w = w
                    sub_sols = [x]
        best = min(sub_sols, key=lambda x: x[1])
        S.append(best[0]+1)

    return S

S = [2,4,3,1]
S = OptS(w.copy(), t.copy(),)
print(S)
def getSum(S, n):
    return sum(t[x-1] for x in S[:n])

acc = 0
for i in range(len(S)):
    value = getSum(S, S.index(i+1)+1)
    acc += value * w[i]
    print(f'{value} * {w[i]}', end=' + ')
print('=', acc)