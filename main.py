import random
def read_data(name):
    
    filename = "TestData/" + name
    f = open(filename)
    return f.readlines()

def point_counter(string,lst):
	point_list = []
	for player in string[1:-1]:
		point_list.append(player.split("\t"))
	dict_point = {}
	for i in point_list:
		dict_point[string[1]] = random.randint(0,1000)
	total = 0
	i = 0
	for i in range(len(lst)):
		if lst[i] in dict_point:
			total += dict_point.get(lst[i])
	return total
	
def main():
	lst = read_data("Football1.txt")
	new_list =[]
	for player in lst[1:-1]:
		new_list.append(player.split("\t"))
	dictionary = {}
	for lst in new_list:
		dictionary[lst[1]] = 1
	
	team = [] 
	while len(team) < 11:
		selector = input("Enter a player: ")
		if selector in dictionary:
			if dictionary[selector] != 1:
				print("This player is not available.")
			else:
				dictionary[selector] -= 1
				team.append(selector)
	print(team)
	print(point_counter(lst,team))
			
if __name__ == "__main__":
    main()
