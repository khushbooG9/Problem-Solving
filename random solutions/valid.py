def process(line):
    try:
        num = int(line[0: 6], 16)
    except:
        return "INVALID"

    num = int(line[0: 6], 16)
    summ = 0
    while num != 0:
        summ = summ + num % 10
        num = num // 10

    compare = (str(hex(summ))[2:]).upper()
    if line[6:] == compare:
        return "VALID"
    return "INVALID"



def validate(line):
    output = []
    for item in line:
        num = int(item[0:6],16)
        summ = 0
        while num!=0:
            summ = summ + num%10
            num = num//10
        comp = (str(hex(summ))[2:]).upper()
        if item[6:] == comp:
            output.append("VALID")
        else:
            output.append("INVALID")
    return output

line = ["8BADF00D", "C0FFEE1C"]
print(validate(line))
