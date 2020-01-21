from typing import List
def longestCommonPrefix(strs: List[str]) -> str:
	if len(strs) == 0 : return ""
	str = strs[0]
	comm_sub_str = str
	length = len(comm_sub_str)
	for i,value in enumerate(strs):

		while value.find(comm_sub_str) != 0 and len(comm_sub_str) !=  0:
			length -= 1
			comm_sub_str = comm_sub_str[0:length ]

	return comm_sub_str

if __name__ == '__main__':
	s = longestCommonPrefix([])
	print("str==" + s)
