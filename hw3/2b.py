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