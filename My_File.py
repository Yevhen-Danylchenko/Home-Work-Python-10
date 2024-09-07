
class Math:
    def __init__(self, num1, num2):

        self.num1 = num1
        self.num2 = num2

    def showInfo(self):
        print(self.num1, self.num2)

    @staticmethod
    def Sum(a, b):
        return a + b
    @staticmethod
    def Subtrac(a, b):
        return a - b
    @staticmethod
    def Multiplic(a, b):
        return a * b
    @staticmethod
    def Division(a, b):
        if b == 0 :
            print('Ділити на ноль неможна!')
        else: return a / b

a = float(input('Введіть перше число: \t'))
b = float(input('Введіть друге число: \t'))

print(Math.Sum(a, b))
print(Math.Subtrac(a, b))
print(Math.Multiplic(a, b))
print(Math.Division(a, b))
