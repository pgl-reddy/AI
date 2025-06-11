def t_o_h(n, f, to, via):
    if n == 1:
        print("Move disk 1 from",f,"to",to)
    else:
        t_o_h(n-1, f, via, to)
        print("Move disk",n,"from",f,"to",to)
        t_o_h(n-1, via, to, f)
n = int(input("Enter the no.of disks: "))
f = 'A'
to = 'B'
via = 'C'
t_o_h(n, f, via, to)