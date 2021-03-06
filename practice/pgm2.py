def perfor_string():
	string='revansiddmore'
	index=0
	size=len(string)
	while index<size:
		print("The Forward Sliceing....")
		print(string[::],end='')
		index+=1
		print("________")		
		index=-1
		size=len(string)
		while index>=size:
			print(string[-1::],end='')
			index=index-1
if __name__ == '__main__':
	perfor_string()
	
	