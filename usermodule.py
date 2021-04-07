def read_data(name):
    """"""
    filename = "TestData/" + name
    f = open(filename)
    return f.readlines()


def main():
	lst = read_data("Football1.txt")
	dic = {}
	for player in lst:
		new_list=(player.split("\t"))
	dictionary = {}
	for lst in new_list:
		dictionary[lst[1]] = 0
		print(dictionary)
	
		
if __name__ == "__main__":
    main()
