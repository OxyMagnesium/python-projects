import secrets


rock = 1
paper = 2
scissors = 3

class Player:
    max_deviation = 0
    hands = [rock, paper, scissors]
    def __init__(self):
        self.score = 0
        self.hand = None

    def play(self):
        self.hand = secrets.choice(Player.hands)

    def win(self):
        self.score += 1
        if abs(self.score) > abs(Player.max_deviation):
            Player.max_deviation = self.score

    def lose(self):
        self.score -= 1
        if abs(self.score) > abs(Player.max_deviation):
            Player.max_deviation = self.score

    def compare_hand(self, player):
        if player.hand == self.hand:
            pass
        elif player.hand == rock:
            if self.hand == paper:
                self.win()
                player.lose()
            else:
                player.win()
                self.lose()
        elif player.hand == scissors:
            if self.hand == rock:
                self.win()
                player.lose()
            else:
                player.win()
                self.lose()
        elif player.hand == paper:
            if self.hand == scissors:
                self.win()
                player.lose()
            else:
                player.win()
                self.lose()

def main():
    players = [Player() for x in range(3)]
    cycles = int(input("Enter cycles to run for: "))
    while cycles > 0:
        for player in players:
            player.play()
        players[0].compare_hand(players[1])
        players[1].compare_hand(players[2])
        players[2].compare_hand(players[0])
        cycles -= 1
    print("Final scores:\nPlayer 1: {0}\nPlayer 2: {1}\nPlayer 3: {2}".format(players[0].score,
                                                                              players[1].score,
                                                                              players[2].score))
    print(f"Maximum deviation: {Player.max_deviation}")

main()
