def reverse_string():
	string=input("enter")
	string_list=string.split()
	output=''
	index=0
	size=len(string_list)-1
	ans_list=[]
	while index<=size:
		if index%2==0:
			ans_list.append(string_list[index])
		else:
			ans_list.append(string_list[::-1])
			index+=1

			print(''.join(output))
if __name__ == '__main__':
	reverse_string()