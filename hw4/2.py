# import sys
# stdin = sys.stdin.readlines()
# s = int(stdin[0])
# t = int(stdin[1])
# n = int(stdin[2])
# staff = [(int(m.split(' ')[0]), int(m.split(' ')[1])) for m in stdin[3:]]
# # print(s, t, n, staff)

# def greedySol(S, start, end):
#     best_start = 0
#     best_start_idx = None
#     for idx in range(len(staff)):
#         if idx+1 in S:
#             continue
#         member = staff[idx]
#         start_time = member[0]
#         if start_time <= start and start_time >= best_start: # add another condition for shortest length?
#             best_start = start_time
#             best_start_idx = idx
#     S.append(best_start_idx+1)
#     # THINK OF CONDITION WHERE THERE IS NOT CONSECUTIVE SEGEMENT FOR JUST FOUND SOLUTION SEGMENT
#     latest_end = staff[best_start_idx][1]
#     # staff.remove(staff[best_start_idx]) # optimization?
#     if latest_end >= end:
#         return S
#     else:
#         return greedySol(S, staff[best_start_idx][1], end)
            
# sol = greedySol([], s, t)
# sol.sort()
# for i in range(len(sol)):
#     print(str(sol[i]), end=' ')

import sys
stdin = sys.stdin.readlines()
s = int(stdin[0])
t = int(stdin[1])
n = int(stdin[2])

S =[]
staff = []
for i in range(n):
    m = stdin[i+3].split(' ')
    staff.append([i+1, int(m[0]), int(m[1])])
# print(s, t, n, staff)

def length(member):
    return member[2] - member[1]

# def greedySol(S, start, end):
while s <= t:
    best_m = [0,0,0]
    i = 0
    while i < len(staff):
        member = staff[i]
        start_time = member[1]
        end_time = member[2]
                
        if start_time <= s:
            if end_time >= best_m[2]:
            # if start_time > best_m[1]
            # if length(member) > length(best_m):
                best_m = member.copy()
                # best_m_idx = i
            staff.pop(i)
            i -=1
        i += 1
    S.append(best_m[0])
    s = best_m[2]
            
S.sort()
for i in range(len(S)):
    print(str(S[i]), end=' ')