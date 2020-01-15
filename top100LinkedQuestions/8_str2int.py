def myAtoi(str: str) -> int:
	str = str.lstrip()
	index = 0
	subStr = ''
	result = 0
	isNeg = False
	if len(str) == 0: return 0
	if  not str[index].isdigit() and str[index] is not '+' and  str[index] is not '-' : return 0
	if str[index] is '+':
		index+=1
	elif str[index] is '-' :
		index += 1
		isNeg = True
	str = str[index:]
	for ch in str:
		if ch.isdigit():
			subStr += ch
			result = int(subStr)
		else:
			break
	result = -result if isNeg else result
	if result > pow(2, 31) - 1 :
		result = pow(2, 31) - 1
	if result < -pow(2, 31):
		result = -pow(2, 31)
	return int(result)


if __name__ == '__main__':
	a = myAtoi('  +-2')
	print(a)
