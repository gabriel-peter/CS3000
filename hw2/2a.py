# gets longest prefix of two words
def longest(a, b):
    i = 0
    while i < min(len(a), len(b)):
        if a[i] == b[i]:
            i +=1
        else:
            break        
    return a[:i]   

# gets longest prefix of list of words
def prefix_finder(words):
    if len(words) % 2 == 1:
        words.append(words[-1])
    if len(words) == 2:
        return longest(words[0], words[1])
    else:
        n = len(words)/2
        return max(prefix_finder(words[:n]), prefix_finder(words[n:]))
