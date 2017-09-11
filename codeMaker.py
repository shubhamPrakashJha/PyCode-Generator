def add():
    codeInString = 'a={0}\nb={1}\nsum=a+b\nprint("sum =",sum)'.format(a,b)
    print(codeInString)
    codeObejct = compile(codeInString,'code', 'exec')
    print("-------------Output---------------")
    exec(codeObejct)

def sub():
    codeInString = 'a={0}\nb={1}\nsum=a-b\nprint("sum =",sum)'.format(a,b)
    print(codeInString)
    codeObejct = compile(codeInString,'code', 'exec')
    print("-------------Output---------------")
    exec(codeObejct)

def mul():
    codeInString = 'a={0}\nb = {1}\nsum = a*b\nprint("sum =",sum)'.format(a,b)
    print(codeInString)
    codeObejct = compile(codeInString,'code', 'exec')
    print("-------------Output---------------")
    exec(codeObejct)

def div():
    codeInString = 'a={0}\nb={1}\nsum=a/b\nprint("sum =",sum)'.format(a,b)
    print(codeInString)
    codeObejct = compile(codeInString,'code', 'exec')
    print("-------------Output---------------")
    exec(codeObejct)

a = int(input("enter first number: "))
b = int(input("enter second number: "))
print("choose any option from: ")
print(" add\t sub\t mul\t div")
func = input("enter the function: ")
print("=============Code=================")
if func == "add":
    add()
elif func =="sub":
    sub()
if func == "mul":
    mul()
elif func =="div":
    div()
