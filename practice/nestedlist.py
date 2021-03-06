def nested_list():
	player_list=[[10,'sachin','IND'],[14,'pointing','AUS']]
	print()

	for row in range(len(player_list)):
		for coloum in range(len(player_list[row])):
			print(player_list[row][coloum],end='\t')



if __name__ == '__main__':
	nested_list()