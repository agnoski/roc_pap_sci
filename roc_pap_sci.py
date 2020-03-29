from random import choice

class Game:

	def __init__(self):
		self.moves = {
			"rock" : ("scissor", "lizard"),
			"scissor" : ("paper", "lizard"),
			"paper" : ("rock", "spock"),
			"lizard" : ("paper"),
			"spock" : ("rock", "scissor")
		}

		self.n = 0
		self.n_rounds = 5
		self.n_rounds_to_win = int(self.n_rounds/2 + 1)
		self.cpu_score = 0
		self.player_score = 0

		self.gestures = list(self.moves.keys())

	def fcpu_move(self):
		return choice(self.gestures)

	def fplayer_move(self):
	    player_move = None
	    while  player_move not in self.gestures:
	        player_move = input('Choose between ' + str(self.gestures) + '\n')
	    return player_move

	def fround_win(self, player_move, cpu_move):
		if player_move == cpu_move:
			return 0
		if player_move in self.moves[cpu_move]:
			return 1
		else:
			return 2

	def fround_winner(self, player_move, cpu_move):
	    print('cpu choice:  ', cpu_move)
	    print('player choice:  ', player_move)
	    round_winner = self.fround_win(player_move , cpu_move) 
	    if round_winner==0:
	        print('tie')
	    elif round_winner==1:
	        print('cpu won')
	        self.cpu_score+=1
	    else:
	        print('player won')
	        self.player_score+=1
	    
	    self.n+=1

	    print('cpu score:  ', self.cpu_score)
	    print('player score:  ', self.player_score)
	    print('round played: ', self.n)

	def fplay(self):
		while ((self.cpu_score < self.n_rounds_to_win) and (self.player_score < self.n_rounds_to_win) and (self.n < self.n_rounds)):
			print('-------------------------------------')
			player_move = self.fplayer_move()
			computer_move = self.fcpu_move()
			self.fround_winner(player_move,computer_move)

game = Game()
game.fplay()