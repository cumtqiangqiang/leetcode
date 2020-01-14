import sys
def reverse( x: int) -> int:
	flag = 1
	x = str(x)
	if int(x) < 0:
		flag = 0
		x = x[1:]
	length = len(x)
	num = 0
	for i in range(length):
		ch = x[i:i+1]
		ch = int(ch)
		p = ch *pow(10,i)
		num += p
	if flag == 0 : num = ~num+1
	if num > pow(2,31)-1 or num < -pow(2,31):num = 0

	return num


if __name__ == '__main__':
	a = reverse(-2147483648)
	print(a)


