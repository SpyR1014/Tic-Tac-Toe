#My First Tic Tac Toe program
#Spyr1014

#GENERATE THE BOARD, triple """ maintain the formating and allow multi line strings
def display_board(current_positions):
	board = """
	{top left} | {top center} | {top right}
	---------
	{center left} | {center} | {center right}
	---------
	{bottom left} | {bottom center} | {bottom right}
	""".format(**current_positions)
	print board



def user_move(current_positions, current_player):
	possible_moves = []
	user_prompt = "Player "+ current_player + ", please type your move from the options below! \n"
	#Grab current possible moves
	for position in current_positions:
		if current_positions[position] == " ":
			possible_moves.append(position)
			user_prompt += "\n" + position
	user_prompt += '\n'
	#Wait for person to type shit in
	user_choice = raw_input(user_prompt).lower()
	while user_choice not in possible_moves:
		print '\n',"I DID NOT UNDERSTAND WHAT YOU TYPED IN!\n"
		display_board(current_positions)
		user_choice = raw_input(user_prompt).lower() #these are the options the person can type. And lower converts it to lower case
	current_positions[user_choice] = current_player #Puts player into that spot
	if current_player == "X":
		current_player = "O"
	else:
		current_player = "X" 
	return current_positions, current_player
#current_positions, current_player = user_move(current_positions, current_player) #this actually defines both

def is_game_over (current_positions):
	#Assuming only one winner
	winners = [["top left", "top center", "top right"],
			["center left", "center", "center right"], 
			["bottom left", "bottom center", "bottom right"], 
			["top left", "center left", "bottom left"], 
			["top center", "center", "bottom center"], 
			["top right", "center right", "bottom right"], 
			["top left", "center", "bottom right"], 
			["top right", "center", "bottom left"]]

	for winning_combo in winners:
		possible_winner = current_positions[winning_combo[0]] #will return first word of the outer list
		if possible_winner != " ":
			possibly_won = True
			for other_space in winning_combo:
				if current_positions[other_space] != possible_winner:
					possibly_won = False
					break
			if possibly_won:
				return possible_winner + " WINS!!!!"
	is_draw = True #Check if draw
	for position in current_positions:
		if current_positions[position] == " ":
			is_draw = False
			return False
	if is_draw:
		return "DRAW!"

def play_game():

	current_positions = {"top left": " ", "top center": " ", "top right": " ",
				"center left": " ", "center": " ", "center right": " ",
				"bottom left": " ", "bottom center": " ", "bottom right": " "}
	current_player = "X"
	result = False
<<<<<<< HEAD

	print "WELCOME TO TIC TAC TOE!!!!!", '\n \n', "Player", current_player, "starts!"

=======
	print "Welcome to Tic Tac Toe!"
>>>>>>> origin/master
	while not result:
		display_board(current_positions)
		current_positions, current_player = user_move(current_positions, current_player)
		result = is_game_over(current_positions)
		if result:
			display_board(current_positions)
			print "GAME OVER\n"
			print "Result: ", result

play_game()
