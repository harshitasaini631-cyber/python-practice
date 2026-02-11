s = input("Enter a string:")
vowels = "aeiouAEIOU"
result = ""

for char in s:
    if char in vowels:
        result += "*"
    else:
        result += char
print(result)            
