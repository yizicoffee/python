W = input("请输入金额：")
C = len(W)
A = ''
for n in range(0,C):
    if W[n] == "1":
        A += '壹' 
    elif W[n] == "2":
        A += '贰'
    elif W[n] == "3":
        A += '叁'
    elif W[n] == "4":
        A += '肆'
    elif W[n] == "5":
        A += '伍'
    elif W[n] == "6":
        A += '陆'
    elif W[n] == "7":
        A += '柒'
    elif W[n] == "8":
        A += '捌'
    elif W[n] == "9":
        A += '玖'
    elif W[n] == "0":
        if n == 0:
            A += ''
        else:
            A += '零'
    print(A)
    if A[-1] == '零':
        print('cool')
    #else:
    if n == eval('C - 16'):
        A += '仟'
    elif n == eval('C - 15'):
        A += '佰'
    elif n == eval('C - 14'):
        A += '拾'
    elif n == eval('C - 13'):
        A += '兆'
    elif n == eval('C - 12'):
        A += '仟'
    elif n == eval('C - 11'):
        A += '佰'
    elif n == eval('C - 10'):
        A += '拾'
    elif n == eval('C - 9'):
        A += '亿'
    elif n == eval('C - 8'):
        A += '仟'
    elif n == eval('C - 7'):
        A += '佰'
    elif n == eval('C - 6'):
        A += '拾'
    elif n == eval('C - 5'):
        A += '万'
    elif n == eval('C - 4'):
        A += '仟'
    elif n == eval('C - 3'):
        A += '佰'
    elif n == eval('C - 2'):
        A += '拾'
    elif n == eval('C - 1'):
        A += '圆整'
    #else:
    #    print("你输入的是神马东西啊，看不懂")
    
print(A)
