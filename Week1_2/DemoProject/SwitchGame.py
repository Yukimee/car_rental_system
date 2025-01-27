#Swith Game Class
class Switch:

    #constructor
    def __init__(self, player, game_type):

        self.player = player
        self.game_type = game_type

    #method start
    def start(self):
        print(f"The {self.player} starting game for {self.game_type}")

    #method pause:
    def pause(self):
        print(f"The {self.player} pause game for {self.game_type}")

#Create Objects (instances) of the Switch class
player_one = Switch("Lee", "Dance")
player_two = Switch("Jason", "Boxing")

player_one.start()
player_two.pause()