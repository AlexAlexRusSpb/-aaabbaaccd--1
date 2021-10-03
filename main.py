def recur(string)->str:
    for i,s in enumerate(string):
        if s != string[0]:
            return ''.join(string[0]+str(i)+recur(string[i:]))
    if string: return ''.join(string[0]+str(len(string)))
    return ''

print(recur('aaabbaaccd'))