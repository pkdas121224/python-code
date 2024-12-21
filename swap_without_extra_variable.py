a = int(input("Enter the value a:"))
b = int(input("Enter the value b:"))

def fun_a(x,y):
    x = y
    return x
def fun_b(x,y):
    y = x
    return y

if __name__ == '__main__':
    print("a =", fun_a(a,b))
    print("b =", fun_b(a,b))