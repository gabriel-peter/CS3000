def OptS(w, t, n):
    X = [[i, t[i], w[i]] for i in range(n)] #1
    S = []
    while len(S) < len(X): #2
        max_w = X[0][2] #3
        sub_sols = [X[0]] 
        for i in range(n): #4
            if i+1 in S: continue
            x = X[i] 
            w = x[2]
            if w >= max_w: #5
                if w == max_w:
                    sub_sols.append(x)
                else:
                    max_w = w
                    sub_sols = [x]
        best = min(sub_sols, key=lambda x: x[1]) # 6
        S.append(best[0]+1)

    return S