

def cal(s):
        """
        :type s: str
        :rtype: int
        """
        new = []
        for k in s:
        	new.append(k)
        l = []
        num = 0
        op = '+'
        if len(new) == 0:
            return 0
        while len(new)>0:
            c = new.pop(0)
            if c.isdigit():
                num = 10*num + int(c)
            if c=='(':
            	num = cal(new)
            if (len(new)==0) or (c == '+' or c == '-' or c == '*' or c == '/' or c == ')'):
                if op=="+":
                    l.append(num)
                elif op=="-":
                    l.append(-num)
                elif op=="*":
                    l[-1] = l[-1]*num
                elif op=="/":
                    l[-1] = int(l[-1]/float(num))
                op = c
                num=0
                if op==')':
                    break

        return sum(l)

a = "2*(5+5*2)/3+(6/2+8)"
print(a[1:])
print(cal(a))
print(cal("1 + 1"))
print(cal(" 6-4 / 2 "))
print(cal("(2+6* 3+5- (3*14/7+2)*5)+3"))


