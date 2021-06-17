C = [0, 25, 54, 37, 19, 40]
B = [0, 30, 33, 70, 35, 30]
S = 15

M_B = [0, B[1]] + [None] * (len(B)-2)
M_C = [0, C[1]] + [None] * (len(C)-2)

def OPT_C(n):
    if M_C[n] != None:
        return M_C[n]
    else:
        M_C[n] = C[n] + max(OPT_C(n-1), OPT_B(n-1)-S)
        return M_C[n]

def OPT_B(n):
    if M_B[n] != None:
        return M_B[n]
    else:
        M_B[n] =  B[n] + max(OPT_B(n-1), OPT_C(n-1)-S)
        return M_B[n]

def FindOpt(M_C, M_B, n, current_team):
    if n == 0:
        return []
    celtics_choice = M_C[n]
    bruins_choice = M_B[n]
    if current_team == 'Celtics':
        bruins_choice = M_B[n] - S
    else:
        celtics_choice = M_C[n] - S
    if celtics_choice > bruins_choice:
        return FindOpt(M_C, M_B, n-1, 'Celtics') + ['Celtics']
    else:
        return FindOpt(M_C, M_B, n-1, 'Bruins') + ['Bruins']

OPT_B(5)
OPT_C(5)
print(M_C, M_B)
print(FindOpt(M_C, M_B, 5, 'Bruins'))