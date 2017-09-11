def calc(codeInString):
    print(codeInString)
    codeObejct = compile(codeInString, 'code', 'exec')
    print("-------------Output---------------")
    exec(codeObejct)

def add():
    codeInString = 'a={0}\nb={1}\nsum=a+b\nprint("sum =",sum)'.format(a,b)
    calc(codeInString)

def sub():
    codeInString = 'a={0}\nb={1}\nsum=a-b\nprint("sum =",sum)'.format(a,b)
    calc(codeInString)

def mul():
    codeInString = 'a={0}\nb = {1}\nsum = a*b\nprint("sum =",sum)'.format(a,b)
    calc(codeInString)

def div():
    codeInString = 'a={0}\nb={1}\nsum=a/b\nprint("sum =",sum)'.format(a,b)
    calc(codeInString)

def pow():
    codeInString = 'a={0}\nb={1}\nsum=a**b\nprint("sum =",sum)'.format(a,b)
    calc(codeInString)

a = int(input("enter first number: "))
b = int(input("enter second number: "))
print("choose any option from: ")
print(" add\t sub\t mul\t div\t pow")
func = input("enter the function: ")
print("=============Code=================")
if func == "add":
    add()
elif func =="sub":
    sub()
elif func == "mul":
    mul()
elif func =="div":
    div()
elif func == "pow":
    pow()
