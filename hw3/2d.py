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