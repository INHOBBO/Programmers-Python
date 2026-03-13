s = input()
answer = ''

for char in s:
    if char.isupper():
        answer += char.lower()        
    elif char.islower():
        answer += char.upper()
        
print(answer)