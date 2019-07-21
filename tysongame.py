class Game():
    def __init__(self):
        self.rooms = { "Tavern": {
                            "description": "You are in a cozy tavern warmed by an open **fire**. There is a door going **outside**.",
                            "items": {"fire" : "The fire crackles, with firewood recently being added."},
                            "exits": {"outside" : "Outside"}},
                        "Outside": {
                            "description": "You see a large **tree** and some **grass**. The weather is nice. There is a door going **inside** the tavern.",
                            "items": {"tree": "It looks like an old oak tree, at least 50 years old", "grass": "The grass looks green and soft."},
                            "exits": {"inside" : "Tavern"}}}
        self.position = "Tavern"

    def send(self, commandString):
        commands = commandString.strip().split(' ')
        if len(commands) > 0:
            command = commands[0]
            currentroom = self.rooms[self.position]
            
            if command == "help":
                return "Commands:\n**look** - examines the surroundings\n**go** <exit> - takes you to a different room"
            elif command == "look":
                if len(commands) == 1:
                    return currentroom["description"]
                else:
                    if commands[1].lower() in currentroom["items"]:
                        return currentroom["items"][commands[1].lower()]
                    else:
                        return "That item isn't here"
            elif command == "go":
                if len(commands) == 1:
                    return "Go where?"
                else:
                    if commands[1].lower() in currentroom["exits"]:
                        self.position = currentroom["exits"][commands[1].lower()]
                        return "You go "+commands[1]
                    else:
                        return "That is not a valid exit."
            elif command == "inv" or command == "inventory":
                return "You are a dog, you are not sure you have pockets."
            elif command == "xyzzy":
                return "What do you think this is, *Zork?*"
            
            else:
                return "That is not a valid command"


        else:
            return ''
