#checking for Armstrong number

class Armstrong:
    def arm(self,number):
        sum = 0
        while number > 0:
            remainder = number % 10
            sum = (remainder ** 3) + sum
            number = int(number / 10)
        return sum

armstrong = Armstrong()
num = int(input("Please enter a number : "))
result = armstrong.arm(num)
if num == result:
    print("Armstrong")
else:
    print("OOPS !!!Not Armstrong")