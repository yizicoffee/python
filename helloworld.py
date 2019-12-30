M,OP,N = map(str,input().split())
#m=int(M)
#n=int(N)
if OP=="+":
    result = eval(M + N)
    print("{:.2f}".format(result))
elif OP=="-":
    result = eval(M - N)
    print("{:.2f}".format(result))
elif OP=="*":
    result = eval(M * N)
    print("{:.2f}".format(result))
elif OP=="/":
    result = eval(M / N)
    print("{:.2f}".format(result))
else:
    print("输入错误")
