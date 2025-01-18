"""without function call for string reverse"""
txt = str(input("Enter the string value:"))[::-1]
print(txt)

"""with function create for string reverse"""
def myfun(x):
    return x[::-1]

y = str(input("Enter the 2nd string value:"))
txt = myfun(y)

print(txt)
