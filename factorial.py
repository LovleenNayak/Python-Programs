#Factorial of a number

class fact:
    def factorial(self,number):
        result = 1
        i = 1
        while i <= number:
            result = i * result
            i = i+1
        print ("Factorial of {} is {}".format(number,result))



fact = fact()
num = int(input("Please enter a number : "))
fact.factorial(num)
