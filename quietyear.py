class Player():
    def __init__(self, user):
        self.name = user.name
        self.id = user.id
        self.contempt = 0

class World()
    def __init__(self):
        resources = []
        npcs = []

class Resource()
    def __init__(self, name):
        self.name = name
        self.isScarce = True

class Question()
    def __init__(self, cardnumber, Q1, Q2):
        self.cardnumber = cardnumber
        self.Q1 = Q1
        self.Q2 = Q2

#class Location

class Game():
    def __init__(self):
        self.players = []
        self.questions = [Question("AH", "What group has the highest status in the community?", "Are there distinct family units in the community?"]

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
                if param == "game":
                    self.players = []
                    self.world = ""
                if param == "resource":
                    self.resource += Resource(commands[2])
                else:
                    await message.channel.send("New what?")
            elif command == "list":
                if param == "players":
                    output = "Current players:\n"
                    for player in self.players:
                        output += player.name + '\n'

                    if len(self.players) == 0:
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
