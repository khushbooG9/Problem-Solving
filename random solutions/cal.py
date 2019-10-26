

#Just ran a loop from 0 to 999, check if the nth number is divisible by 3 or 5
# If it is divisible by 3 or 5, just added to the summ variable
def cal():
    summ = 0
    for n in range(1000):
        if n%3 == 0 or n%5==0 :
            summ+=n
    print(summ)

cal()
