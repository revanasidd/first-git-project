def alicing_opertions():
	first_list=[20,30,40,50]

	second_list=first_list
	print(id(first_list))
	print(id(second_list))

	print()

	first_list[2]='dhoni'
	print(first_list)
	print(second_list)
if __name__ == '__main__':
	alicing_opertions()