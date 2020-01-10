print('单引号')
print("双引号")
print('''三
单引
号''')
print('金木水火土'[0])
print('金木水火土'[-1])
print('金木水火土'[1:-1])
print('金木水火土'[1:])
print('金木水火土'[:-1])
#步长切片
print("1234567890"[1:9:3])
#逆序排列
print("1234567890"[::-1])
#转义符\b回退\n换行（光标移动到下行行首）\r回车（光标移动到本行首）
print("123\n321")
print("123\r321")
#x+y连接字符串，x*n复制n此字符串x，x in s 如果x是s的子串则返回True否则返回False
print("你"+"好")
print("不"*3)
print("你好" in "你好啊")
#星期对应
weekStr="一二三四五六日"
weekId=eval(input("请输入星期数字（1-7）："))
print("星期"+weekStr[weekId-1])
#字符串长度和转换
strLen=len("你好啊")
print(strLen)
print(str(1.11))
print(str.lower("ASDFG"),str.upper("asdfg"))
print("ASDFG".lower(),"asdfg".upper())
print("114.112.33.121".split("."))
print("aabaa".count("a"))
print("linux".replace("l","un"))
print("readme".center(20,"="))
print("abcdefg".strip("aced"))
print(",".join("12345"))
print("{1} name is {0}".format("Tom","my"))
# 填充=、对齐（<左对齐、>右对齐，^居中对齐），宽度20
print("{0:=^20}".format("Tom"))
# 控制精度
print("{0:.2f}".format(3.1415926))