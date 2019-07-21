import discord
import random
import socket
import asyncio

from tysongame import Game

game = Game()

client = discord.Client()

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_member_join(member):
    for channel in member.server.channels:
        if channel.name == 'general':
            await client.send_message(channel, 'Bork! Bork! I think {} is a burglar. Bork!'.format(member.name))


@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('$book'):
        await message.channel.send('The current story is "The Doctor\'s Case" by Stephen King.')

    if message.content.startswith('$bite'):
        await message.channel.send('*Aims for your jugular but misses. He is very smol.*')

    if message.content.startswith('$sit') or message.content.startswith('Tyson sit'):
        await message.channel.send('*Tyson sits on the couch. But not because you told him to.*')

    if message.content.startswith('$stay') or message.content.startswith('Tyson stay'):
        await message.channel.send('*Tyson looks up at you and resumes napping.*')

    if message.content.startswith('$come') or message.content.startswith('Tyson stay'):
        await message.channel.send('*Tyson ignores you.*')

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
    
    if message.content.startswith('>'):
        response = game.send(message.content[1:])
        await message.channel.send(response)

    if message.content.startswith('$roll'):
        words = message.content.split(' ')
        if len(words) > 1 and 'd' in words[1]:
            words2 = words[1].split('d')
            if words2[0].isdigit() and words2[1].isdigit():
                dice = min(int(words2[0]), 20)
                size = min(int(words2[1]), 1000)
                output = '('
                for i in range(dice):
                    output += str(random.randint(1, size)))
                    if i < dice-1:
                        output += ', '
                output += ')'
                await message.channel.send(output)
            else:
                await message.channel.send('Invalid input! Bork.')

        else:
            await message.channel.send('Invalid input! Bork.')

    if 'chicken' in message.content.lower():
        await message.channel.send('Tyson Chicken Nugget!')

    if 'good boy' in message.content.lower():
        await message.channel.send('<:happytyson:601457297302093844>')

    if 'bad dog' in message.content.lower():
        await message.channel.send('<:happytyson:601457297302093844>')

    if 'blep' in message.content.lower():
        await message.add_reaction('<:happytyson:601457297302093844>')

    if 'tyson' in message.content.lower():
        await message.add_reaction('<:angrytyson:593509277705044181>')



client.run(open("apikey.txt",'r').read().strip())
