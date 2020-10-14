# Adding two numbers using python

class program:
    def addition(self,first_num, second_num):
        self.first_num = first_num
        self.second_num = second_num
        result = first_num + second_num
        print ("Addtion of {} and {} is : {}".format(first_num,second_num,result))

first_num = int(input("Enter 1st number : "))
second_num = int(input("Enter 2nd number : "))
program = program()
program.addition(first_num,second_num)
