s = input("Enter a string to check palindrome or not:")

if (s[::-1]) == (s[:]):
    print("Palindrome")
else:
    print("not palindrome")    


'''Program to ignore spaces
s = input("Enter a string: ")

s_no_space = s.replace(" ", "")

if s_no_space == s_no_space[::-1]:
    print("Palindrome")
else:
    print("Not Palindrome")
'''    