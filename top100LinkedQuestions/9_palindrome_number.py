def isPalindrome( x: int) -> bool:
	x =str(x)
	return x.isdigit() and x == x[::-1]


if __name__ == '__main__':
	a = isPalindrome(12321)
	print(a)