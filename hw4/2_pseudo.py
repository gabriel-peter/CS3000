# Variable init(s)
s = None, t = None, n = None
S =[], staff = []

# Preprocessing step allows for original index
# to stay consistent regardless of array manipulations.
for i in range(n):
    m = stdin[i+3].split(' ')
    staff.append([i+1, int(m[0]), int(m[1])])

# Loops until solution is made 
# (i.e. a final shift is added to extend past `t`)
while s < t:
    best_m = [0,0,0]
    i = 0
    # Iterated through all staff members still
    # under consideration
    while i < len(staff):
        member = staff[i]
        start_time = member[1]
        end_time = member[2]

        # Rule 1: the solution can only be considered
        # if it doesn't allow a gap with the previous       
        if start_time <= s:  
            # Rule 2: The longest that prevents overlap
            # is the prioritized shift in the Solution.
            if end_time >= best_m[2]:
                best_m = member.copy()
            # Crucial! Removes elements that are included
            # or will never be included in the Solution.
            staff.pop(i) # A!!
            i -=1
        i += 1
    S.append(best_m[0])
    # new interation now considers the overlap
    # with best found shift's end time...
    s = best_m[2] 
            
S.sort()
for i in range(len(S)): # printing formatics of the array
    print(str(S[i]), end=' ')