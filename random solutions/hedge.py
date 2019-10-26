def Solutions(list1):
    num = []
    for i in list1:
        i = i.split(",")
        num.append(i)
    trans = [i[1] for i in num]
    diction = {}
    #print(num)
    for item in num:
        if item[0] in diction.keys():
            diction[item[0]] += int(item[1])
        else:
            diction[item[0]]=int(item[1])
    print(diction)
    return 0

dfa = {
    1 : {'a': 1, 'b': 2},
    2: {'a':2 , 'b': 3},
    3: { 'a':3, 'b':1}
}
def accept(dfa, initial, acc, string):
    if len(string)==0:
        return "reject"
    state = initial
    #print("initial", initial)
    for c in string:
        state = dfa[state][c]
        #print("c", state)

    if state in acc:
        return "accept"
    else:
        return "reject"

if __name__ == "__main__":
    string = str(input())
    ans = accept(dfa, 1, {3}, string)
    print(ans)


import fileinput 
#import numpy as np
# Enter your code here. Read input from STDIN. Print output to STDOUT
import math
def percentile(N, percent, key=lambda x:x):
   
    if not N:
        return None
    k = (len(N)-1) * percent
    f = math.floor(k)
    c = math.ceil(k)
    if f == c:
        return key(N[int(k)])
    d0 = key(N[int(f)]) * (c-k)
    d1 = key(N[int(c)]) * (k-f)
    return d0+d1

def Solutions(list1):
    num = []
    for i in list1:
        i = i.split(",")
        num.append(i)
    num = sorted(num, key = lambda i:i[0])
    #print(num)
    idc = {}
    total = []
    for i in range(len(num)):
        if i==0:
            total.append([int(num[i][0]), int(num[i][1])])
        else:
            su = int( num[i][1]) + int(total[i-1][1])
            total.append([int(num[i][0]),su ])
    for i in total:
        idc[i[0]]=i[1]
    #print(idc)
    #print(total)
    newtot = [i[1] for i in total]
    #print(newtot)
    perc = percentile(newtot, 0.8)
    #print(perc)
    
    for k in range(1,len(total)):
        
        prev = total[k-1][1]
        if perc < total[k][1] and perc > total[k-1][0] :
            return total[k-1][0]
        
    return total[-1][0] 
 

if __name__ == "__main__":
    inp = []
    for line in fileinput.input():
        inp.append(str(line.rstrip()))
    ans = Solutions(inp)
    print(ans)
    
