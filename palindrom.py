#Checking a number is palindrom or not

class palindrom:
    def palindrom(self,num):
        i = 0
        count = 0
        while i >= num:
            rem = num / i
            if rem is 0:
                count = count + 1
            else:
                pass
            i = i+1
            return int(count)
        

pal = int(input("Number Please : "))
palin = palindrom()
count = palin.palindrom(pal)
if count -ge 2:
    print("Palindrom")
else:
    print("OOPS !!! Not Palindrom")