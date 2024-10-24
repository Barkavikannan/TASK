string = "abababab"
pattern = "aba"
result = []  
n = len(string)
m = len(pattern)
    
for i in range(n - m + 1):
    match = True
    for j in range(m):
        if string[i + j] != pattern[j]:
            match = False
            break
    if match:
        result.append(i)
print(result)
