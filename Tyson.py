import discord
import random

client = discord.Client()

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('$book'):
        await message.channel.send('The current story is "The Doctor\'s Case" by Stephen King.')

    if message.content.startswith('$bark'):
        output = ''
        for i in range(len(message.content.split(' '))):
            output += 'Bork! '
        await message.channel.send(output)

    if message.content.startswith('$yip'):
        output = ''
        for i in range(len(message.content.split(' '))):
            output += 'Yap! '
        await message.channel.send(output)
    
    if message.content.startswith('$roll'):
        words = message.content.split(' ')
        print(words)
        if len(words) > 1 and 'd' in words[1]:
            words2 = words[1].split('d')
            print(words2)
            if words2[0].isdigit() and words2[1].isdigit():
                output = '('
                for i in range(int(words2[0])):
                    output += str(random.randint(1, int(words2[1])))
                    if i < int(words2[0])-1:
                        output += ', '
                output += ')'
                print(output)
                await message.channel.send(output)
            else:
                await message.channel.send('Invalid input! Bork.')

        else:
            await message.channel.send('Invalid input! Bork.')

    if 'chicken' in message.content.lower():
        await message.channel.send('Tyson Chicken Nugget!')

    if 'good boy' in message.content.lower():
        await message.channel.send('<:happytyson:601457297302093844>')

    if 'tyson' in message.content.lower():
        await message.add_reaction('<:angrytyson:593509277705044181>')

client.run(open("apikey.txt",'r').read().strip())
