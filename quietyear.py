class Player():
    def __init__(self, user):
        self.name = user.name
        self.id = user.id

class World()

class Location

class Game():
    def __init__(self):
        self.players = []


    async def send(self, message):
        commands = message.content[1:].strip().split(' ')
        if len(commands) > 0:
            command = commands[0]

            if len(commands) > 1:
                param = commands[1]
            else:
                param = None
            
            if command == "help":
                await message.channel.send("Commands:\n**join** - join the game\n**list players** lists players in the game ")
            elif command == "join":
                self.players.append(Player(message.author))
                await message.channel.send(message.author.name + " has joined the current game")
            elif command == "new":
                if param = "game":
                    self.players = []
                    self.world = ""
                else:
                    await message.channel.send("New what?")
            elif command == "list":
                if param == "players":
                    output = "Current players:\n"
                    for player in self.players:
                        output += player.name + '\n'

                    if len(players) == 0:
                        output += "None"
                    await message.channel.send(output)
                else:
                    await message.channel.send("List what?")

            elif command == "inv" or command == "inventory":
                await message.channel.send("You are a dog, you are not sure you have pockets.")
            elif command == "xyzzy":                
                await message.channel.send("What do you think this is, *Zork?*")
            
            else:
                await message.channel.send("That is not a valid command")
