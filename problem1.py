#C:\Users\User\AppData\Local\Programs\Python\Python311
#calculator program
class addition:
    @staticmethod
    def add(x,y):
        print(x+y)


class subtraction:
    @staticmethod
    def sub(x,y):
        print(x-y)


class multiplication:
    @staticmethod
    def mul(x,y):
        print(x*y)


class division:
    @staticmethod
    def div(x,y):
        print(x/y)

class calculator(addition,subtraction,multiplication,division):
    pass

num=calculator()
num.add(5,6)
num.sub(6,5)
num.mul(6,5)
num.div(5,6)
